"""_summary_
"""
import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    """_summary_

    Args:
        QMainWindow (_type_): _description_
    """

    def __init__(self):
        super(MyWindow, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi(os.path.join(
            os.path.dirname(__file__), 'ui', 'main.ui'), self)  # Load the .ui file
        self.show()  # Show the GUI


def window():
    """_summary_
    """
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec()


window()
