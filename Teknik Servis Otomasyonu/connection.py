# Veritabanı işlemleri
import sqlite3

baglanti = sqlite3.connect("Ariza.db")
baglanti = sqlite3.connect("liste.db")
baglanti = sqlite3.connect("login.db")
baglanti = sqlite3.connect("NewAriza.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("create table if not exists urun (musteriAd text, urunAdi text, tel int, adres text, arizaAciklama text, marka text, kategori text)")
baglanti.commit()