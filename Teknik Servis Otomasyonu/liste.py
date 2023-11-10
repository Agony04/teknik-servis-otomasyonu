#from PyQt5.QtWidgets import*
#from main_python import Ui_MainWindow


#class ListelePage(QMainWindow):
    #def __init__(self)-> None:
   #     super().__init__()
  #      self.listeform =Ui_MainWindow()
 #       self.listeform.setupUi(self)
#        self.hide ()
 #       self.show()
       

from PyQt5.QtWidgets import*
from liste_python import Ui_Form

import sqlite3

class ListelePage(QWidget):
    baglanti = sqlite3.connect("liste.db")
    islem = baglanti.cursor()
    table = islem.execute("create table if not exists urun (musteriAd text, urunAdi text, tel int, adres text, arizaAciklama text, marka text, kategori text)")
    baglanti.commit()
    def __init__(self) ->None:
        super().__init__()
        self.urunlisteleform = Ui_Form()
        self.urunlisteleform.setupUi(self)
        