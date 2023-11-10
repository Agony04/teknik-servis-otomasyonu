from PyQt5.QtWidgets import*
from main_python import Ui_MainWindow
from liste import ListelePage

import sqlite3

#connection = sqlite3.connect("Ariza.db")

class ArizaPage(QMainWindow):
    baglanti = sqlite3.connect("Ariza.db")
    islem = baglanti.cursor()
    table = islem.execute("create table if not exists urun (musteriAd text, urunAdi text, tel int, adres text, arizaAciklama text, marka text, kategori text)")
    baglanti.commit()
    def __init__(self)-> None:
        super().__init__()
        self.arizaform =Ui_MainWindow()
        self.arizaform.setupUi(self)
        self.listeac = ListelePage()
        self.arizaform.btnekle.clicked.connect(self.KayitYap)
    def KayitYap(self):
        urun =self.arizaform.cmbUrun.currentText()
        marka =self.arizaform.cmbMarka.currentText()
        arizaAciklama =self.arizaform.lineEditArizaAciklama.text()
        print(urun," ",marka," ",arizaAciklama)
        self.hide ()
        self.listeac.show()