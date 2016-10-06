from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtCore import *

from WebLayout import *
from CustomTabWidget import *

import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tab1 = WebLayout()
        self.tab1Widget = QWidget()
        self.tab1Widget.setLayout(self.tab1)

        self.tab2 = WebLayout()
        self.tab2Widget = QWidget()
        self.tab2Widget.setLayout(self.tab2)

        self.tabs = Trace_Tabs()

        self.setWindowTitle("Web Browser")
        self.setCentralWidget(self.tabs)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Main()
    window.show()
    window.raise_()
    application.exec_()