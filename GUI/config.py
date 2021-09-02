from PySide2.QtWidgets import QApplication, QSystemTrayIcon
from PySide2.QtGui import QIcon
from PySide2.QtGui import QWindow
class CONFIGAPP(QApplication):
    def __init__(self):
        super(CONFIGAPP, self).__init__()
        self.setApplicationName("Składanie zamówień")
        icon = QIcon('IMG/warehouse.png')
        self.setWindowIcon(icon)
