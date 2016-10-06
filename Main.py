from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtCore import *

from WebLayout import *

import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.webLayout = WebLayout()
        self.webLayoutWidget = QWidget()
        self.webLayoutWidget.setLayout(self.webLayout)

        self.setWindowTitle("Web Browser")
        self.setCentralWidget(self.webLayoutWidget)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Main()
    window.show()
    window.raise_()
    application.exec_()