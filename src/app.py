"""_summary_
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    """_summary_

    Args:
        QMainWindow (_type_): _description_
    """

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 200, 200)
        self.initUI()

    def initUI(self):
        """_summary_
        """
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label")
        self.label.move(50, 50)


def window():
    """_summary_
    """
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec()


window()
