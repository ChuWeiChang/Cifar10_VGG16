# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HW1_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 541, 411))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.B5 = QtWidgets.QPushButton(self.groupBox)
        self.B5.setGeometry(QtCore.QRect(160, 340, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B5.setFont(font)
        self.B5.setObjectName("B5")
        self.B3 = QtWidgets.QPushButton(self.groupBox)
        self.B3.setGeometry(QtCore.QRect(160, 170, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B3.setFont(font)
        self.B3.setObjectName("B3")
        self.B2 = QtWidgets.QPushButton(self.groupBox)
        self.B2.setGeometry(QtCore.QRect(160, 120, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B2.setFont(font)
        self.B2.setObjectName("B2")
        self.B1 = QtWidgets.QPushButton(self.groupBox)
        self.B1.setGeometry(QtCore.QRect(160, 60, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B1.setFont(font)
        self.B1.setObjectName("B1")
        self.B4 = QtWidgets.QPushButton(self.groupBox)
        self.B4.setGeometry(QtCore.QRect(160, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B4.setFont(font)
        self.B4.setObjectName("B4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(160, 290, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "VGG16 TEST"))
        self.B5.setText(_translate("MainWindow", "5.Test"))
        self.B3.setText(_translate("MainWindow", "3.Show Model Shortcut"))
        self.B2.setText(_translate("MainWindow", "2.Show HyperParameter"))
        self.B1.setText(_translate("MainWindow", "1.Show Train Images"))
        self.B4.setText(_translate("MainWindow", "4.Show Accuracy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

