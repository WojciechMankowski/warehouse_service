from PySide2.QtWidgets import *
from PySide2.QtGui import QFont, QIcon
from Client.Client import Client
from Magazyn.Database import database
import re

class Widgets(QWidget):

    def __init__(self):
        super(Widgets, self).__init__()
        self.icon = QIcon('IMG/warehouse.png')
        QMainWindow().setWindowIcon(self.icon)
        tray = QSystemTrayIcon()
        tray.setIcon(self.icon)
        tray.show()

        self.Layout()
        self.setLayout(self.grid)
        self.addButton()

        self.db = database()
        self.db.dowlaod_all()

    def seeItem(self):
        self.Clear()
        id = self.listcombobox.currentText()
        order = self.db.DownloadOrderData_One_ID(id)
        btn = QPushButton()
        btn.setText("Zobacz zamówienie")
        btn.clicked.connect(self.seeItem)
        self.grid.addWidget(btn, 3, 2)
        self.config(btn, 20, 60)
        row = 5
        label = QLabel()
        label_list = QLabel()
        label.setText("Zamówienie składa się z: ")
        self.config(label, 18)
        self.config(label_list, 18)
        self.grid.addWidget(label, 4, 2)
        for key, item in order.items():
            txt = f"{key}: {item} {self.db.dictionary_with_unit[key]}."
            label_list.setText(txt)
            self.grid.addWidget(label_list, row, 2)

    def seeItems(self):
        re  = self.db.DownloadOrderData()
        # print(re)
        self.listcombobox = QComboBox()
        self.listcombobox.addItems(re)
        self.grid.addWidget(self.listcombobox, 2, 2)

        btn = QPushButton()
        btn.setText("Zobacz zamówienie")
        btn.clicked.connect(self.seeItem)
        self.grid.addWidget(btn, 3, 2)

        self.config(btn, 20, 60)
        self.config(self.listcombobox, 19)

    def Clear(self):
        if self.grid.count() > 3:
            index = 3
            for i in range(self.grid.count()):
                try:
                    self.grid.itemAt(index).widget().deleteLater()
                    index += 1
                except:
                    print()

    def config(self,widget, point: int, weight: int=50 ):
        font = QFont()
        font.setPixelSize(point)
        font.setWeight(weight)
        widget.setFont(font)

    def checking(self) -> bool:
        print(self.entry.text())
        txt = self.entry_weight.text()
        print(type(txt))
        if self.entry.text != "":
            if self.entry_weight != "":
                if self.entry_unit != "":
                    return True
        return False

    def AddItem(self):
        self.checking()

    def AddingProducts(self):
        row = 2
        self.entry = QLineEdit()
        self.entry_weight = QLineEdit()
        self.entry_unit = QLineEdit()
        self.config(self.entry, 19)
        self.grid.addWidget(self.entry, 2, 2)
        self.config(self.entry_weight, 19)
        self.config(self.entry_unit, 19)
        self.grid.addWidget(self.entry_unit, 4, 2)
        self.grid.addWidget(self.entry_weight, 3, 2)
        lista = ['Nazwa produktu', "Wartość", "Jednostka"]
        for item in lista:
            label = QLabel()
            label.setText(item)
            self.config(label, 19)
            self.grid.addWidget(label, row, 1)
            row += 1
        btn = QPushButton("Dodaj")
        self.grid.addWidget(btn, row, 2)
        self.config(btn, 25, 60)
        btn.clicked.connect(self.AddItem)

    def addButton(self):
        btn_add = QPushButton("Zobacz zamówienia")
        self.config(btn_add, 25, 60)
        btn_add.clicked.connect(self.Clear)
        btn_add.clicked.connect(self.seeItems)

        btn_summary = QPushButton("Dodawanie produktów")
        btn_summary.clicked.connect(self.Clear)
        btn_summary.clicked.connect(self.AddingProducts)
        self.config(btn_summary, 25, 60)
        #
        # btn = QPushButton("Złóż zamówienie")
        # btn.clicked.connect(self.Clear)
        # btn.clicked.connect(self.PlacingAnOrder)
        # self.config(btn, 25, 60)
        self.grid.addWidget(btn_add, 1, 1)
        self.grid.addWidget(btn_summary, 1, 2)
        # self.grid.addWidget(btn, 1, 3)

    def Layout(self):
        self.grid = QGridLayout()