from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Browser(QMainWindow):
    
    def __init__(self) -> None:
        super(Browser, self).__init__()
        
        self.engineView : QWebEngineView = QWebEngineView()
        self.engineView.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.engineView)
        self.showMaximized()
        
        navigation : QToolBar = QToolBar()
        self.addToolBar(navigation)
        
        previous : QAction = QAction("Previous page", self)
        previous.triggered.connect(self.engineView.back)
        navigation.addAction(previous)
        
        forward : QAction = QAction("Forward page", self)
        forward.triggered.connect(self.engineView.forward)
        navigation.addAction(forward)
        
        refresh : QAction = QAction("Refresh page", self)
        refresh.triggered.connect(self.engineView.reload)
        navigation.addAction(refresh)
        
        home : QAction = QAction("Home page", self)
        home.triggered.connect(self.HomePage)
        navigation.addAction(home)
        
        self.searchBar : QLineEdit = QLineEdit()
        self.searchBar.returnPressed.connect(self.LoadUrl)
        navigation.addWidget(self.searchBar)
        
        self.engineView.urlChanged.connect(self.UpdateUrl)
        pass
    
    def HomePage(self) -> None:
        self.engineView.setUrl(QUrl("https://google.com"))
        pass
    
    def LoadUrl(self) -> None:
        url : str = self.searchBar.text()
        self.engineView.setUrl(QUrl(url))
        self.show()
        pass
    
    def UpdateUrl(self, url : QUrl) -> None:
        self.searchBar.setText(url.toString())
        pass

app : QApplication = QApplication(sys.argv)
QApplication.setApplicationName("Simple Web Browser")

browser : Browser = Browser()
app.exec_()