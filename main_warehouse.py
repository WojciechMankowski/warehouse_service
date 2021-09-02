from GUI.config import CONFIGAPP
from GUI.magazynGUI import Widgets
from GUI.mainwindow import Main
from Magazyn.warehouse_staff import warehouse_staff

def run():
    app = CONFIGAPP()
    main = Main()
    widgets = Widgets()
    widgets.show()
    app.exec_()


if __name__ == '__main__':
    # warehouse_staff().DownloadOrderData()
   run()
