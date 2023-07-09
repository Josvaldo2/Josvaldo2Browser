from PyQt5 import QtWidgets as qw
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from os.path import dirname
from urllib.parse import urlparse

def arquivoRelativo(f):
    return f"{dirname(__file__)}/{f}"

class JonsoBrowser(qw.QMainWindow):
    def __init__(self):
        super(JonsoBrowser, self).__init__()

        self.janela = qw.QWidget()
        self.janela.setWindowTitle("Josvaldo Browser")
        self.janela.setWindowIcon(QIcon(arquivoRelativo("EpicFace.png")))

        self.layout = qw.QVBoxLayout()
        self.horizontal = qw.QHBoxLayout()

        self.barraUrl = qw.QPlainTextEdit()
        self.barraUrl.setMaximumHeight(30)

        self.irBotao = qw.QPushButton('ir')
        self.irBotao.setMaximumHeight(30)

        self.voltarBotao = qw.QPushButton('<')
        self.voltarBotao.setMaximumHeight(30)

        self.avancarBotao = qw.QPushButton('>')
        self.avancarBotao.setMaximumHeight(30)

        for i in (self.barraUrl, self.irBotao, self.voltarBotao, self.avancarBotao):
            self.horizontal.addWidget(i)
        
        self.telaSite = QWebEngineView()

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.telaSite)
        self.telaSite.setUrl(QUrl.fromLocalFile(arquivoRelativo("JosvaldoSearch.html")))

        def mudarDeSite(self):
            url = self.barraUrl.toPlainText()
            urlP = urlparse(url)
            if not urlP.scheme:
                url = f"https://google.com/search?q={url}"
            self.telaSite.setUrl(QUrl(url))
        
        self.janela.setLayout(self.layout)
        self.janela.show()

        self.irBotao.clicked.connect(lambda: mudarDeSite(self))
        self.voltarBotao.clicked.connect(self.telaSite.back)
        self.avancarBotao.clicked.connect(self.telaSite.forward)

aplicativo = qw.QApplication([])
JonsoBrowser()

aplicativo.exec_()