# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liste.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(902, 618)
        self.cmbislem = QtWidgets.QComboBox(Form)
        self.cmbislem.setGeometry(QtCore.QRect(260, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cmbislem.setFont(font)
        self.cmbislem.setObjectName("cmbislem")
        self.cmbislem.addItem("")
        self.cmbislem.addItem("")
        self.cmbislem.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 841, 461))
        self.tableWidget.setRowCount(25)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.btnDurum = QtWidgets.QPushButton(Form)
        self.btnDurum.setGeometry(QtCore.QRect(510, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnDurum.setFont(font)
        self.btnDurum.setObjectName("btnDurum")
        self.lneislemDurumu = QtWidgets.QLabel(Form)
        self.lneislemDurumu.setGeometry(QtCore.QRect(40, 20, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lneislemDurumu.setFont(font)
        self.lneislemDurumu.setObjectName("lneislemDurumu")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cmbislem.setItemText(0, _translate("Form", " Seçiniz"))
        self.cmbislem.setItemText(1, _translate("Form", "Yapıldı"))
        self.cmbislem.setItemText(2, _translate("Form", "Yapılmadı"))
        self.btnDurum.setText(_translate("Form", "Durum Listele"))
        self.lneislemDurumu.setText(_translate("Form", "İşlem Durumu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())