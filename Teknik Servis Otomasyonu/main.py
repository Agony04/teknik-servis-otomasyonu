from PyQt5.QtWidgets import QApplication
from login import LoginPage

import sqlite3


baglanti = sqlite3.connect("NewAriza.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("create table if not exists urun (musteriAd text, tel int, adres text)")
baglanti.commit()

app =QApplication([])
pencere =LoginPage()
pencere.show()
app.exec_()