from typing import List
from .Database import database
from collections import Counter, defaultdict
from dataclasses import dataclass

@dataclass
class Order:
    def __init__(self, ID_order):
        self.ID = ID_order
        self.product_weight_list = []
        self.list_of_products = []

    def add_products(self, name: str):
        self.list_of_products.append(name)
        print(self.list_of_products)
    def add_product_weight(self, weight: int):
        self.product_weight_list.append(weight)
        print(self.product_weight_list)
    def returnOrder(self):
        return {self.list_of_products: self.product_weight_list}

class warehouse_staff:
    def __init__(self):
        self.db = database()
        self.inf_client = Counter()
        self.order_clients = defaultdict(dict)
        self.list_id = []
        self.lsit = []
    def DownloadOrderData3(self):
        resultat = self.db.DownloadOrderData()

        for item in resultat:
            self.inf_client[item[0]] = item[1]
            # .returnOrder()
            for id in self.list_id:
                if id != item[0]:
                    self.order_clients[item[0]] = client
            if not item[0] in self.list_id:
                self.list_id.append(item[0])
                client = Order(item[0])
            elif item[0] in self.list_id:
                client.add_products(item[2])
                client.add_product_weight(item[3])

            # order = {item[0]  : {item[2]: item[3]}}
            # self.order_clients.update(order)
        print(self.inf_client)
        print("-"*20)
        print(self.order_clients)
        for keys in self.order_clients.keys():
            item = self.order_clients[keys]
            print(item.product_weight_list)
                # print(item)
                # print(item.product_weight_list)

    def DownloadOrderData(self):
        resultat = self.db.DownloadOrderData()
        orders_tupla = tuple()
        self.searchingTheList("marchew", 15)
        self.searchingTheList("marchew", 5)
        self.searchingTheList("pomidor", 15)

    def searchingTheList(self, name: str, weight: float):
        if name in self.lsit:
            self.lsit.index(name)
            print(self.lsit.index(name))
        else:
            print(name)
            self.lsit.append(name)


        #     orders = [item[2], item[3]]
        #     orders_tupla += (orders,)
        #     orders_dict[item[0]] = orders_tupla
        #     if not item[0] in orders_dict.keys():
        #         orders_tupla = tuple()
        #     # for key in orders_dict.keys():
        # for key, value in orders_dict.items():
        #     print(key, value)





#  pobranie danych o zamówieniach +
# wysyłanie maili do klientów
#  dodawanie nowych produktów +
#  dodawanie liczby produktów +
# zmianna cenny +

if __name__ == '__main__':
    warehouse_staff().DownloadOrderData()