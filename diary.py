# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Juan-pc\Desktop\Agenda\agenda.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import datetime
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAtras = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtras.setGeometry(QtCore.QRect(10, 260, 41, 31))
        self.btnAtras.setObjectName("btnAtras")
        self.btnAdelante = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdelante.setGeometry(QtCore.QRect(760, 260, 41, 31))
        self.btnAdelante.setObjectName("btnAdelante")
        self.txtCuerpo = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCuerpo.setGeometry(QtCore.QRect(140, 90, 521, 421))
        self.txtCuerpo.setObjectName("txtCuerpo")
        self.lblImagen = QtWidgets.QLabel(self.centralwidget)
        self.lblImagen.setGeometry(QtCore.QRect(0, 0, 841, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImagen.sizePolicy().hasHeightForWidth())
        self.lblImagen.setSizePolicy(sizePolicy)
        self.lblImagen.setMinimumSize(QtCore.QSize(841, 591))
        self.lblImagen.setStyleSheet("background-image:url(\'diary.png\');\n"
"background-repeat:no-repeat;")
        self.lblImagen.setText("")
        self.lblImagen.setObjectName("lblImagen")
        self.lblDate = QtWidgets.QLabel(self.centralwidget)
        self.lblDate.setGeometry(QtCore.QRect(340, 25, 171, 95))
        self.lblDate.setStyleSheet("font: 75 11pt \"Segoe UI Semibold\";\n"
"color:black;")
        x = datetime.datetime.now()
        switcher = {
            "Monday": 'Lunes',
            "Tuesday": "Martes",
            "Wednesday": "Miercoles",
            "Thursday": "Jueves",
            "Friday": "Viernes",
            "Sathurday": "Sabado",
            "Sunday": "Domingo"
        }
        self.lblDate.setText(switcher.get(time.strftime("%A"), "Dia invalido") + time.strftime(" %d/%m/%y") +" "+ str(x.hour) +"and"+ str(x.minute) + "minutes")
        self.lblDate.setObjectName("lblDate")
        self.btnGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(370, 540, 75, 23))
        self.btnGuardar.setStyleSheet("font: 75 11pt \"Segoe UI Semibold\";\n"
"background-color:white;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"color:black;")
        self.btnGuardar.setObjectName("btnGuardar")
        self.lblImagen.raise_()
        self.btnAtras.raise_()
        self.btnAdelante.raise_()
        self.txtCuerpo.raise_()
        self.lblDate.raise_()
        self.btnGuardar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #Aqui se hace el evento
        self.btnGuardar.clicked.connect(self.btnGuardarClicked)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAtras.setText(_translate("MainWindow", "<"))
        self.btnAdelante.setText(_translate("MainWindow", ">"))
        self.btnGuardar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Save your information</p></body></html>"))
        self.btnGuardar.setText(_translate("MainWindow", "Save"))    
    def btnGuardarClicked(self):
        text = str(self.txtCuerpo.toPlainText())
        self.infoDialogue(text)
    def infoDialogue(self, text): ## Method to open a message box
        infoBox = QMessageBox() ##Message Box that doesn't run
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText(str(text))
        infoBox.setWindowTitle("Information Saved")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.setEscapeButton(QMessageBox.Close)
        infoBox.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

