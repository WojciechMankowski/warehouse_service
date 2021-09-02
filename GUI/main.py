from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QSystemTrayIcon

from GUI.mainwindow import Main

from GUI.widgets import Widgets
from GUI.config import CONFIGAPP



def RUNING():
    app = CONFIGAPP()
    main = Main()
    widgets = Widgets()
    widgets.show()
    app.exec_()



if __name__ == '__main__':
    RUNING()