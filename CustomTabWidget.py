from PyQt4.QtGui import *

from WebLayout import *

class Trace_Tabs(QTabWidget):

    def __init__(self):
        QTabWidget.__init__(self)
        self.setTabsClosable(True)
        self._build_tabs()
        self.setTabShape(QTabWidget.Rounded)

    def _build_tabs(self):
        self.setUpdatesEnabled(True)

        initialTabLayout = WebLayout()
        initialTabWidget = QWidget()
        initialTabWidget.setLayout(initialTabLayout)

        self.insertTab(0,initialTabWidget, initialTabLayout.urlBar.text())
        self.insertTab(1,QWidget(),'  +  ')
        self.tabBar().setTabButton(1, QTabBar.RightSide, None)

        self.currentChanged.connect(self._add_trace)
        self.tabCloseRequested.connect(self._close_tab)

    def _add_trace(self, index):
        '''last tab was clicked'''
        if index == self.count()-1 :
            '''add tab'''
            newTabLayout = WebLayout()
            newTabWidget = QWidget()
            newTabWidget.setLayout(newTabLayout)

            self.insertTab(index, newTabWidget, "New Tab")
            self.setCurrentIndex(index)

    def _close_tab(self, index):
        if self.count() > 2:
            if index != 0:
                if self.currentIndex() == index:
                    self.setCurrentIndex(index-1)
                self.removeTab(index)
            else:
                if self.currentIndex() == index:
                    self.setCurrentIndex(index+1)
                self.removeTab(index)