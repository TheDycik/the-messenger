# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 655)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 281, 101))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(90, 110, 113, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(270, 110, 113, 20))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 150, 421, 411))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 590, 291, 41))
        self.textEdit.setObjectName("textEdit")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(340, 590, 91, 41))
        self.sendButton.setObjectName("sendButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dyc Messenger"))
        self.lineEditName.setPlaceholderText(_translate("MainWindow", "name"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "pass"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
