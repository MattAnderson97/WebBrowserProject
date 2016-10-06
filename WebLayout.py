from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

from Stack import *


class WebLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.previousPage = Stack()
        self.nextPage = Stack()

        self.previousPage.size(50)
        self.nextPage.size(50)

        self.homePage = "https://www.google.co.uk"

        self.createLayouts()

        self.urlBar.returnPressed.connect(self.goToPage)
        self.webView.loadFinished.connect(self.updateView)
        self.backButton.clicked.connect(self.goBackPage)
        self.forwardButton.clicked.connect(self.goForwardPage)

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
            self.previousPage.push(self.webView.url())
            self.loadPage(QUrl(self.urlBar.text()))
        else:
            self.loadPage(QUrl(self.homePage))
            self.urlBar.setText(self.homePage)

    def loadPage(self, url):
        self.webView.load(url)
        self.urlBar.setText(url.toString())

    def goBackPage(self):
        if not self.previousPage.isEmpty():
            url = self.previousPage.pop()
            self.nextPage.push(self.webView.url())
            self.loadPage(url)

    def goForwardPage(self):
        if not self.nextPage.isEmpty():
            url = self.nextPage.pop()
            self.previousPage.push(self.webView.url())
            self.loadPage(url)

    def updateView(self):
        self.webView.page().mainFrame()
        print(self.webView.title())