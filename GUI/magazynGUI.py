from PySide2.QtWidgets import *
from PySide2.QtGui import QFont, QIcon

from GUI.config import CONFIGAPP
from GUI.mainwindow import Main
from Magazyn.Database import database


class Widgets(QWidget):

    def __init__(self):
        super(Widgets, self).__init__()

        self.setGeometry(300, 200, 500, 400)
        self.Layout()
        self.setLayout(self.grid)
        self.addButton()
        self.db = database()
        self.db.dowlaod_all()
    def addwidget(self, widget, row: int, columns: int) -> None:
        self.grid.addWidget(widget, row, columns)

    def seeItem(self):
        self.Clear()
        id = self.listcombobox.currentText()
        order = self.db.DownloadOrderData_One_ID(id)
        btn = QPushButton("Zobacz zamówienie")
        btn.clicked.connect(self.seeItem)
        self.addwidget(btn, 3, 2)
        self.config(btn, 20, 60)
        row = 5
        label = QLabel("Zamówienie składa się z: ")
        label_list = QLabel()
        self.config(label, 18)
        self.config(label_list, 18)
        self.addwidget(label, 4, 2)
        for key, item in order.items():
            txt = f"{key}: {item} {self.db.dictionary_with_unit[key]}."
            label_list.setText(txt)
            self.addwidget(label_list, row, 2)

    def seeItems(self):
        re  = self.db.DownloadOrderData()
        self.listcombobox = QComboBox()
        self.listcombobox.addItems(re)

        btn = QPushButton()
        btn.setText("Zobacz zamówienie")
        btn.clicked.connect(self.seeItem)
        self.addwidget(self.listcombobox, 2, 2)
        self.addwidget(btn, 3, 2)
        self.config(btn, 20, 60)
        self.config(self.listcombobox, 19)

    def Clear(self):
        index = 4
        print(self.grid.count())
        if self.grid.count() > 4:

            # self.grid.itemAt(2).layout()
            for i in range(self.grid.count()):
                try:
                    print(self.grid.itemAt(index).widget())
                    self.grid.itemAt(index).widget().deleteLater()
                    index += 1
                except:
                    ...

    def config(self,widget, point: int, weight: int=50 ):
        font = QFont()
        font.setPixelSize(point)
        font.setWeight(weight)
        widget.setFont(font)

    def checking(self) -> bool:
        if self.entry.text() != "" and self.entry_weight.text() != "" and  self.entry_unit.text() != "":
            return True
        return False

    def AddItem(self):
        true_or_false =self.checking()
        msg = QMessageBox()
        product = []
        resultat = self.db.GetProductNnames()
        self.listcombobox = QComboBox()
        self.listcombobox.addItems(resultat)
        self.addwidget(self.listcombobox, 2, 2)
        self.config(self.listcombobox, 19)
        if true_or_false:
            product_tupla = self.entry.text(), self.entry_weight.text(), self.entry_unit.text(), self.entry_pents.text()
            product.append(product_tupla)
            print(product)
            self.db.add(product)
            msg.setText("Dodałeść nowy produkt")
            msg.exec()
        else:
            msg.setText("Nie podałeść wszystkich danych")
            msg.exec()

    def EditingProducts(self):
        resultat  = self.db.GetProductNnames()
        self.listcombobox = QComboBox()
        self.listcombobox.addItems(resultat)
        self.addwidget(self.listcombobox, 2, 2)
        self.config(self.listcombobox, 19)
        btn = QPushButton("Edytuj")
        btn.clicked.connect(self.Edit)
        self.addwidget(btn, 3,2)
    def Edit(self):
        self.name = self.listcombobox.currentText()
        resultat = self.db.DownloadOrderData_One_Name(self.name)
        self.entry_name = QLineEdit()
        self.entry_name.setText(str(resultat[1]))
        self.grid.addWidget(self.entry_name, 4,2)
        label = QLabel("Nazwa produktu")


        self.entry_weight = QLineEdit()
        self.entry_weight.setText(str(resultat[2]))

        self.entry_unit = QLineEdit()
        self.entry_unit.setText(str(resultat[3]))

        self.entry_price = QLineEdit()
        self.entry_price.setText(str(resultat[4]))

        btn = QPushButton("Zmień")
        row = 4
        list_ = [self.entry_name, self.entry_weight, self.entry_unit, self.entry_price]
        # self.tuple = tuple([self.entry_name.text(), float(self.entry_weight.text()), self.entry_unit.text(), float(self.entry_price.text())])
        label_list = ["Nazwa produktu", "Liczebność", "Jednostka", "Cena za 1 jednostkę"]
        for i, item in enumerate(list_):
            self.grid.addWidget(item, row, 2)
            label = QLabel(label_list[i])
            self.grid.addWidget(label, row, 1)
            self.config(item ,19)
            self.config( label,19)
            row += 1
        self.grid.addWidget(btn, row, 2)
        btn.clicked.connect(self.send)


    def send(self):
        self.tuple = tuple(
            [self.entry_name.text(), float(self.entry_weight.text()), self.entry_unit.text(), float(self.entry_price.text())])
        for item in self.tuple:
            print(item)
        self.db.UpdeteProduct(name=self.tuple[0], weight=self.tuple[1],
                              unit=self.tuple[2], price=self.tuple[3], name_chane=self.name)

    def AddingProducts(self):
        row = 2
        self.entry = QLineEdit()
        self.entry_weight = QLineEdit()
        self.entry_unit = QLineEdit()
        self.entry_pents = QLineEdit()

        self.config(self.entry, 19)
        self.config(self.entry_weight, 19)
        self.config(self.entry_unit, 19)
        self.config(self.entry_pents, 19)

        self.grid.addWidget(self.entry, 2, 2)
        self.grid.addWidget(self.entry_weight, 3, 2)
        self.grid.addWidget(self.entry_unit, 4, 2)
        self.grid.addWidget(self.entry_pents, 5, 2)
        lista = ['Nazwa produktu', "Wartość", "Jednostka", "Cena za 1 jednostkę"]
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
        See_orders = QPushButton("Zobacz zamówienia")
        self.config(See_orders, 25, 60)
        See_orders.clicked.connect(self.Clear)
        See_orders.clicked.connect(self.seeItems)

        Adding_products = QPushButton("Dodawanie produktów")
        Adding_products.size().setWidth(1000)
        Adding_products.setMaximumWidth(1000)
        print(Adding_products.size().width())
        Adding_products.clicked.connect(self.Clear)
        Adding_products.clicked.connect(self.AddingProducts)
        self.config(Adding_products, 25, 60)
        #
        btn = QPushButton("Edycja produktów")
        btn.clicked.connect(self.Clear)
        btn.clicked.connect(self.EditingProducts)
        self.config(btn, 25, 60)
        btn_ = QPushButton("Sprawdź stan magazunu")
        self.config(btn_, 25, 60)
        btn_.clicked.connect(self.Clear)
        btn_.clicked.connect(self.CheckTheStockLevel)


        self.grid.addWidget(See_orders, 1, 1)
        self.grid.addWidget(btn_, 1, 4)
        self.grid.addWidget(Adding_products, 1, 2)
        self.grid.addWidget(btn, 1, 3)

    def CheckTheStockLevel(self):
        resultat = self.db.dowlaod_all()

        tableWidget = QTableWidget()

        tableWidget.setRowCount((len(resultat) +1))
        tableWidget.setColumnCount(4)
        label_list = ["Nazwa", "Liczebność", "Jednostka", "Cena"]
        columns = 0
        for items in label_list:
            name = QTableWidgetItem(items)
            tableWidget.setHorizontalHeaderItem(columns, name)
            columns +=1

        size_table = tableWidget.size()

        layout = QHBoxLayout()
        layout.addWidget(tableWidget)

        # self.grid.addLayout(layout, 2, 2)
        self.grid.addWidget(tableWidget, 2,2)
        size_mimum = 500
        self.grid.setColumnMinimumWidth(2, size_mimum)
        setRowMinimumHeight = (len(resultat) + 1) * 37
        self.grid.setRowMinimumHeight(2, setRowMinimumHeight)
        self.config(tableWidget, 23)

        row = 1
        print(len(resultat))
        for items in resultat:
            # print(items)
            name = QTableWidgetItem(str(items[1]))
            weight = QTableWidgetItem(str(items[2]))
            unit = QTableWidgetItem(str(items[3]))
            price = QTableWidgetItem(str(items[4]))
            tableWidget.setItem(row, 0, name)
            tableWidget.setItem(row, 1, weight)
            tableWidget.setItem(row, 2, unit)
            tableWidget.setItem(row, 3, price)
            row +=1

    def Layout(self):
        self.grid = QGridLayout()