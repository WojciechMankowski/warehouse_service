from PySide2.QtGui import QWindow
class Main(QWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.resize(1025,1450)
        self.setGeometry(1025, 900, 800, 400)

