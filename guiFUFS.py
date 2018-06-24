# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiFUFS.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(602, 613)
        Dialog.setMinimumSize(QtCore.QSize(602, 432))
        self.lblStatusPic = QtWidgets.QLabel(Dialog)
        self.lblStatusPic.setGeometry(QtCore.QRect(310, 20, 281, 201))
        self.lblStatusPic.setStyleSheet("image: url(:/newPrefix/blowBrains.jpeg);")
        self.lblStatusPic.setText("")
        self.lblStatusPic.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatusPic.setObjectName("lblStatusPic")
        self.tbStatusMsg = QtWidgets.QTextBrowser(Dialog)
        self.tbStatusMsg.setGeometry(QtCore.QRect(10, 500, 581, 101))
        self.tbStatusMsg.setObjectName("tbStatusMsg")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 17))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 71, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 71, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 71, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 71, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 71, 17))
        self.label_6.setObjectName("label_6")
        self.lblName = QtWidgets.QLabel(Dialog)
        self.lblName.setGeometry(QtCore.QRect(110, 50, 191, 17))
        self.lblName.setObjectName("lblName")
        self.lblHappy = QtWidgets.QLabel(Dialog)
        self.lblHappy.setGeometry(QtCore.QRect(110, 80, 191, 17))
        self.lblHappy.setObjectName("lblHappy")
        self.lblParent = QtWidgets.QLabel(Dialog)
        self.lblParent.setGeometry(QtCore.QRect(110, 110, 191, 17))
        self.lblParent.setObjectName("lblParent")
        self.lblMarried = QtWidgets.QLabel(Dialog)
        self.lblMarried.setGeometry(QtCore.QRect(110, 140, 191, 17))
        self.lblMarried.setObjectName("lblMarried")
        self.lblAlive = QtWidgets.QLabel(Dialog)
        self.lblAlive.setGeometry(QtCore.QRect(110, 170, 191, 17))
        self.lblAlive.setObjectName("lblAlive")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 260, 85, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 220, 85, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 320, 261, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(310, 320, 261, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(13, 480, 581, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.listGood = QtWidgets.QTextBrowser(Dialog)
        self.listGood.setGeometry(QtCore.QRect(30, 340, 261, 121))
        self.listGood.setObjectName("listGood")
        self.listBad = QtWidgets.QTextBrowser(Dialog)
        self.listBad.setGeometry(QtCore.QRect(310, 340, 261, 121))
        self.listBad.setObjectName("listBad")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.runSim)
        self.pushButton_2.clicked.connect(Dialog.startGame)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Stats:"))
        self.label_2.setText(_translate("Dialog", "Name:"))
        self.label_3.setText(_translate("Dialog", "Happiness:"))
        self.label_4.setText(_translate("Dialog", "Parent:"))
        self.label_5.setText(_translate("Dialog", "Married:"))
        self.label_6.setText(_translate("Dialog", "Alive:"))
        self.lblName.setText(_translate("Dialog", "No User Loaded"))
        self.lblHappy.setText(_translate("Dialog", "xxx"))
        self.lblParent.setText(_translate("Dialog", "xxx"))
        self.lblMarried.setText(_translate("Dialog", "xxx"))
        self.lblAlive.setText(_translate("Dialog", "xxx"))
        self.pushButton.setText(_translate("Dialog", "GO FISH"))
        self.pushButton_2.setText(_translate("Dialog", "Start/Restart"))
        self.label_7.setText(_translate("Dialog", "Good Effects"))
        self.label_8.setText(_translate("Dialog", "Bad Effects"))
        self.label_9.setText(_translate("Dialog", "Status Messages"))
        self.listGood.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

import test_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

