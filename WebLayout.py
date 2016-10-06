from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *


class WebLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.previousPage = ""
        self.nextPage = ""
        self.homePage = "https://www.google.co.uk"

        self.createLayouts()

        self.urlBar.returnPressed.connect(self.goToPage)
        self.webView.loadFinished.connect(self.resultAvailable)

    def createLayouts(self):
        self.backButton = QPushButton("←")
        self.forwardButton = QPushButton("→")
        self.refreshButton = QPushButton("↻")
        self.urlBar = QLineEdit(self.homePage)

        self.urlBarLayout = QHBoxLayout()
        self.urlBarLayout.addWidget(self.backButton)
        self.urlBarLayout.addWidget(self.forwardButton)
        self.urlBarLayout.addWidget(self.refreshButton)
        self.urlBarLayout.addWidget(self.urlBar)

        self.webView = QWebView()
        self.webView.load(QUrl(self.homePage))
        self.addLayout(self.urlBarLayout)
        self.addWidget(self.webView)

    def goToPage(self):
        if(self.urlBar.text() != ""):
            self.webView.load(QUrl(self.urlBar.text()))
        else:
            self.webView.load(QUrl(self.homePage))
            self.urlBar.setText(self.homePage)

    def resultAvailable(self):
        frame = self.webView.page().mainFrame()
        print(frame.toHtml().encode('utf-8'))
