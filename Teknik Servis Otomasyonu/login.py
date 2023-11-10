from PyQt5.QtWidgets import*
from login_python import Ui_Form
from arizaBilgi import ArizaPage

import sqlite3

#connection = sqlite3.connect("login.db")

class LoginPage(QWidget):
    baglanti = sqlite3.connect("login.db")
    islem = baglanti.cursor()
    table = islem.execute("create table if not exists urun (arizaAciklama text, marka text, kategori text)")
    baglanti.commit()
    
    def __init__(self)-> None:
        super().__init__()
        self.loginform=Ui_Form()
        self.loginform.setupUi(self)
        self.arizaac = ArizaPage()
        self.loginform.btnkayit.clicked.connect(self.GirisYap)
    def GirisYap(self):
        musteriAdSoyad =self.loginform.lineEdit.text()
        telefon =self.loginform.lineEdit_3.text()
        adres = self.loginform.lineEdit_4.text()
        tarih =self.loginform.dateEdit.text()
        print(musteriAdSoyad," ",telefon," ",adres," ",tarih)
        
        self.hide ()
        self.arizaac.show()