import sqlite3
from collections import Counter
from typing import Union, Any
from dataclasses import dataclass

class database:
    def __init__(self):
        self.conn = sqlite3.connect('goods.db')
        self.cursor = self.conn.cursor()
        self.name_tabel = 'stock'

        self.price_dictionary = {} #cena
        self.dictionary_with_weight = Counter({}) #waga
        self.dictionary_with_unit = {} #jendostki

    def CreatingTabels(self):
        query = '''CREATE TABLE orders (id text,
                mail text, order_ware_name text, order_ware_heft float)'''
        self.cursor.execute(query)
        self.conn.commit()

    def add(self, lista: list[Union[str, int, Any]]) -> None:
        for item in lista:
            query = f"""INSERT OR REPLACE INTO {self.name_tabel} (name, scales, unit, price) 
                VALUES ('{item[0]}', '{item[1]}', '{item[2]}','{item[3]}')"""
            self.cursor.execute(query)

        self.conn.commit()

    def dowlaod_all(self):
        # self.cursor.fetchone() pojedyńczy wynik
        print('db')
        tuple__ = tuple()
        resultat = self.cursor.execute(f'SELECT * FROM {self.name_tabel}')
        for item in resultat:
            tuple_ = tuple([item])
            tuple__ = tuple__ + tuple_
            self.dictionary_with_weight[item[1]] = item[2]
            self.dictionary_with_unit[item[1]] = item[3]
            self.price_dictionary[item[1]] = item[4]
        return  tuple__

    def order_add(self, name_user: str, email_user: str, order: dict[str, dict[str, str]]) -> None:
        for key in order.keys():
            for Key, item in order[key].items():
                query = f"""INSERT OR REPLACE INTO orders  
                                VALUES ('{key}', '{email_user}', '{Key}', '{item}')"""

                self.cursor.execute(query)
        self.conn.commit()


    def returnDICT(self, names_return: str):
        if names_return == 'pice':
            return self.price_dictionary
        elif names_return == "unit":
            return self.dictionary_with_unit
        elif names_return == "weight":
            return self.dictionary_with_weight
        elif names_return == "lista":
            return [key for key in self.dictionary_with_unit.keys()]

    def UPDATE_WEIGHT(self, name: str, weight: int):
        Weight = self._update(name, weight)
        query = f"UPDATE {self.name_tabel} SET scales = '{Weight}'  WHERE name = '{name}'"
        self.cursor.execute(query)
        self.conn.commit()

    def updete(self, order):
        for id in order.keys():
            for keys, item in order[id].items():
                self.UPDATE_WEIGHT(keys, item)

    def subtraction(self, name, weight):
        self.dictionary_with_weight.subtract({f"{name}": weight})

    def __del__(self):
        self.conn.close()

    def _update(self, name, weight):
        self.dictionary_with_weight.subtract({name: weight})
        return self.dictionary_with_weight[name]

    def DownloadOrderData(self) -> list[str]:
        lista_id = []
        self.cursor.execute(f'SELECT * FROM orders')
        resultat = self.cursor.fetchall()
        for item in resultat:
            if not item in lista_id:
                lista_id.append(item[0])
        lista_id = list(set(lista_id))
        return lista_id

    def DownloadOrderData_One_ID(self, id: str) -> Counter[str, int]:
        order = Counter()
        self.cursor.execute(f"SELECT * FROM orders WHERE id = '{id}'")
        resultat = self.cursor.fetchall()
        for item in resultat:
            order[item[2]] = item[3]
        return order

    def DownloadOrderData_One_Name(self, name: str) -> tuple[str, int, Any]:
        self.cursor.execute(f"SELECT * FROM {self.name_tabel} WHERE name = '{name}'")
        resultat = self.cursor.fetchall()[0]
        return resultat

    def UpdeteProduct(self, name: str, weight: float, unit: str, price: float, name_chane: str) -> None:
        query = f"UPDATE {self.name_tabel} SET name = '{name}', scales = '{weight}'" \
                f", unit = '{unit}', price = '{price}'  WHERE name = '{name_chane}'"
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()
        self.conn = sqlite3.connect('goods.db')
        self.cursor = self.conn.cursor()
    def GetProductNnames(self):
        Resultat = []
        self.cursor.execute(f'SELECT name FROM {self.name_tabel}')
        resultat = self.cursor.fetchall()
        for item in resultat:
            Resultat.append(item[0])
        return Resultat

if __name__ == '__main__':
    db = database()
    # db.CreatingTabels()
    food = [
        ("Kapusta", 55.0, 'kg', 3.0),
        ("Marchew", 30, 'kg', 2.74),
        ("Maliny", 35, "szt/opk", 18)
    ]
    db.dowlaod_all()


