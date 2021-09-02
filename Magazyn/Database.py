import sqlite3
from collections import Counter
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

    def add(self, lista):
        for item in lista:
            query = f"""INSERT OR REPLACE INTO {self.name_tabel} (name, scales, unit, price) 
                VALUES ('{item[0]}', '{item[1]}', '{item[2]}','{item[3]}')"""
            self.cursor.execute(query)

        self.conn.commit()

    def dowlaod_all(self):
        # self.cursor.fetchone() pojedyńczy wynik
        resultat = self.cursor.execute(f'SELECT * FROM {self.name_tabel}')
        for item in resultat:
            # item # tupla  trzy elementowa
            self.dictionary_with_weight[item[1]] = item[2]
            self.dictionary_with_unit[item[1]] = item[3]
            self.price_dictionary[item[1]] = item[4]


    def order_add(self, name_user: str, email_user: str, order: dict[str, dict[str, str]]) -> None:
        for key in order.keys():
            for Key, item in order[key].items():
                print(Key, item)
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
        print(query)
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
        print(self.dictionary_with_weight)
        self.dictionary_with_weight.subtract({name: weight})
        print(self.dictionary_with_weight)
        return self.dictionary_with_weight[name]

    def DownloadOrderData(self):
        lista_id = []
        self.cursor.execute(f'SELECT * FROM orders')
        resultat = self.cursor.fetchall()
        for item in resultat:
            # print(item[0])
            # print(not item in lista_id)
            if not item in lista_id:
                lista_id.append(item[0])
        lista_id = list(set(lista_id))
        return lista_id

    def DownloadOrderData_One_ID(self, id: str):
        order = Counter()
        self.cursor.execute(f"SELECT * FROM orders WHERE id = '{id}'")
        resultat = self.cursor.fetchall()
        for item in resultat:
            order[item[2]] = item[3]
        return order
if __name__ == '__main__':
    db = database()
    # db.CreatingTabels()
    food = [
        ("Kapusta", 55.0, 'kg', 3.0),
        ("Marchew", 30, 'kg', 2.74),
        ("Maliny", 35, "szt/opk", 18)
    ]
    db.dowlaod_all()


