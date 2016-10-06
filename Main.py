from CustomTabWidget import *

import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = CustomTabWidget()

        self.setWindowTitle("Web Browser")
        self.setCentralWidget(self.tabs)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Main()
    window.show()
    window.raise_()
    application.exec_()