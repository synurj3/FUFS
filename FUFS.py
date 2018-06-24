from PyQt5 import QtWidgets
from guiFUFS import *
from Persons import *
from Resources import *
from goodNews import magicalSesh

from PyQt5.QtCore import *
from PyQt5.QtGui import *

class fufsWindow(QtWidgets.QMainWindow,Ui_Dialog):


    total = None
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connect Buttons to display
        # self.pushButton.clicked.connect(self.runSim)
        # self.runSim()

    def startGame(self):
        self.player1 = Person("Diseasy McGhee", 45, 1, 1, 1)

        self.setPic(resSuperHappy)

        self.lblName.setText(str(self.player1.getName()))
        self.lblHappy.setText(str(self.player1.getHappyStatus()))
        if self.player1.getParentStatus() == 1:
            self.lblParent.setText("Yes")
        else:
            self.lblParent.setText("No")

        if self.player1.getMarriedStatus() == 1:
            self.lblMarried.setText("Yes")
        else:
            self.lblMarried.setText("No")
        if self.player1.getAliveStatus() == 1:
            self.lblAlive.setText("Yes")
        else:
            self.lblAlive.setText("No")

        self.tbStatusMsg.clear()
        self.listGood.clear()
        self.listBad.clear()


    # This is what happens when the "GO Fish" button is pressed
    def runSim(self):
        self.magicalSesh()

    #
    def setPic(self, file):
        self.lblStatusPic.setStyleSheet(file)


    # def magicalSesh(self):
    #     print("You have a Magical Moon Rock Blunt...\nYou decide to smoke it...")
    #     self.player1.setHappyStatus("420")
    #     self.lblHappy.setText("420")
    #     self.tbStatusMsg.append("You have a Magical Moon Rock Blunt...")
    #     self.tbStatusMsg.append("You decide to smoke it...")
    #     self.listGood.append("Immune to everything!")
    #     self.listBad.clear()
    #     self.tbStatusMsg.append("You have acquired immunity to everything")
    #     self.tbStatusMsg.append("All negative status effects are cleared")
    #     self.setPic(resStonedAlien)

    def refreshStats(self):
        self.lblName.setText(str(self.player1.getName()))
        self.lblHappy.setText(str(self.player1.getHappyStatus()))
        if self.player1.getParentStatus() == 1:
            self.lblParent.setText("Yes")
        else:
            self.lblParent.setText("No")

        if self.player1.getMarriedStatus() == 1:
            self.lblMarried.setText("Yes")
        else:
            self.lblMarried.setText("No")
        if self.player1.getAliveStatus() == 1:
            self.lblAlive.setText("Yes")
        else:
            self.lblAlive.setText("No")