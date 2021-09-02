from typing import Protocol, Union
from Magazyn.Database import database


class Men(Protocol):
    def download_information(self):
        ...

    def displaying_the_menu(self):
        ...


# class MenuClient:
#     def __init__(self):
#         self.excit: bool = True
#         self.db = database()
#         self.db.dowlaod_all()
#
#     def download_information(self):
#         self.db.dowlaod_all()
#
#     def displaying_the_menu(self):
#         self.download_information()
#         index = 1
#
#         for item in self.menu:
#             print(f"{index}. {item}")
#             index += 1
#         choice = int(input("Jakie działanie wybieracz? "))
#         return choice
#
#     def AddProduct(self) -> Union[str, float]:
#         lista = self.db.returnDICT("lista")
#         print("W magazynie mamy dostępne następujące produkty")
#         number = 1
#         for item in lista:
#             print(f"{number}. {item}")
#             number += 1
#         name = input("Jaki produkt mam dodać? ")
#         number_user = float(input("Ile kiligramów, sztuk? "))
#         return name, number_user

class Menu:
    def __init__(self):
        self.menu = [
            "Dodaj produkt do zamówienia",
            "Podsumowanie zamówienia",
            "Złożenie zamówienia",
            "Wyjście",
        ]

    def printMenu(self):
        index = 1
        for item in self.menu:
            print(f"{index}. {item}")
            index += 1

if __name__ == "__main__":
    menu = MenuClient()
    menu.displaying_the_menu()
