# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simpleexample.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scan = QtWidgets.QToolButton(self.centralwidget)
        self.scan.setGeometry(QtCore.QRect(110, 180, 111, 41))
        self.scan.setObjectName("scan")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 60, 381, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 70, 91, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setObjectName("open")
        self.menu.addAction(self.open)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.open.triggered.connect(MainWindow.close)
        self.scan.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scan.setText(_translate("MainWindow", "浏览"))
        self.label.setText(_translate("MainWindow", "文件地址"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.open.setText(_translate("MainWindow", "打开"))

