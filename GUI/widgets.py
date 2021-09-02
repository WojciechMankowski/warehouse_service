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

        self.client = Client()
        self.db = database()
        self.db.dowlaod_all()

    def PlacingAnOrder(self):
        label_name = QLabel("Podaj nazwę firmy")
        label_email = QLabel("Podaj adres email")

        self.entry_name = QLineEdit()
        self.entry_email = QLineEdit()
        btn = QPushButton("Złóż zamówienie")
        btn.clicked.connect(self.Clear)
        btn.clicked.connect(self.PlacingAnOrderBTN)
        self.config(btn, 18)
        self.config(label_name, 18)
        self.config(self.entry_name, 18)
        self.config(label_email, 18)
        self.config(self.entry_email, 18)


        self.grid.addWidget(self.entry_name, 2, 2)
        self.grid.addWidget(self.entry_email, 3, 2)
        self.grid.addWidget(label_name, 2, 1)
        self.grid.addWidget(label_email, 3, 1)
        self.grid.addWidget(btn, 4, 2)

    def CheckingTheEmail(self, email: str) -> bool:
        templet = re.compile(r"\w{2,}@\w{1,}\.+\w{2,}")
        search = templet.match(email)
        if search != None:
           return True
        else:
            return False

    def PlacingAnOrderBTN(self):
        msg = QMessageBox()
        self.config(msg, 18)
        order_submit = self.client.SubmitAnOrder()
        name = self.entry_name.text()
        email= self.entry_email.text()
        bool = self.CheckingTheEmail(email)
        if bool:
            msg.setText("Wysłałem Twoje zamówienie do magazynu")
            self.db.order_add(name, email, order_submit)
            self.db.updete(order_submit)
        else:
            msg.setText("Podałeść błędny adres e-email")


    def Addorder(self):
        msg = QMessageBox()
        self.config(msg, 18)
        ProductName = self.list_items.currentText()
        ProductNamber = float(self.entry.text())
        boolen = self.client.BoolenWeight(ProductName, ProductNamber, self.db.returnDICT("weight"))
        if boolen:
            self.client.SaveInDict(ProductName, ProductNamber)
            msg.setText("Dodałem produkt do Twojego zamówienia")
            msg.exec()
        else:
            msg.setText("Niestety nie ma wystarczarocej liczby produktów!!")
            msg.exec()

    def addItem(self):
        self.db.dowlaod_all()
        self.list_items =QComboBox()
        self.list_items.addItems(self.db.returnDICT('lista'))
        self.config(self.list_items, 18)
        self.entry = QLineEdit()
        self.config(self.entry, 18)

        btn_send = QPushButton("Dodaj")
        btn_send.clicked.connect(self.Addorder)
        self.config(btn_send, 18)
        label_name = QLabel("Wybiecz produkt z listy: ")
        label_weight = QLabel("Wpisz wagę/liczbę sztuk np: 2.5, 3, 5.8")
        self.config(label_weight, 18, 55)
        self.config(label_name, 18, 55)
        self.grid.addWidget(self.list_items, 2, 2)
        self.grid.addWidget(label_name, 2, 1)
        self.grid.addWidget(self.entry, 3, 2)
        self.grid.addWidget(label_weight, 3, 1)
        self.grid.addWidget(btn_send, 4, 2)

    def summary(self):
        row = 3
        lebel_start = QLabel("Twoje podsumowanie: ")
        self.grid.addWidget(lebel_start, 2,1)
        self.config(lebel_start, 20)
        for item in self.client.OrderSummary(unit=self.db.returnDICT("unit"), price=self.db.returnDICT('pice')):
            label = QLabel()
            label.setText(item)
            self.config(label, 18, 55)
            self.grid.addWidget(label, row, 2)
            row += 1

    def Clear(self):
        if self.grid.count() > 3:
            index = 3
            for i in range(self.grid.count()):
                try:
                    self.grid.itemAt(index).widget().deleteLater()
                    index += 1
                except:
                    ...

    def config(self,widget, point: int, weight: int=50 ):
        font = QFont()
        font.setPixelSize(point)
        font.setWeight(weight)
        widget.setFont(font)

    def addButton(self):
        btn_add = QPushButton("&Dodaj produkt do zamówienia")
        self.config(btn_add, 25, 60)
        btn_add.clicked.connect(self.Clear)
        btn_add.clicked.connect(self.addItem)

        btn_summary = QPushButton("Podsumowanie zamówienia")
        btn_summary.clicked.connect(self.Clear)
        btn_summary.clicked.connect(self.summary)
        self.config(btn_summary, 25, 60)

        btn = QPushButton("Złóż zamówienie")
        btn.clicked.connect(self.Clear)
        btn.clicked.connect(self.PlacingAnOrder)
        self.config(btn, 25, 60)
        self.grid.addWidget(btn_add, 1, 1)
        self.grid.addWidget(btn_summary, 1, 2)
        self.grid.addWidget(btn, 1, 3)

    def Layout(self):
        self.grid = QGridLayout()