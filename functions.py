from Persons import *
from random import *
# from endings import *
from FUFS import *


def getStatus(self):
    self.player1.showName()
    self.player1.showHappyStatus()
    self.player1.showParentStatus()
    self.player1.showMarriedStatus()
    self.player1.showAliveStatus()
    self.player1.showGood()
    self.player1.showBad()
    return


def getDivorced(self):
    self.player1.setHappyStatus(randint(1, 10))
    self.player1.setParentStatus(1)
    self.player1.setMarriedStatus(0)
    self.player1.setAliveStatus(1)
    print("You have gotten a divorce...")
    if randint(0, 9800) > 9500:
        print("It's not that bad...\nYou keep your child...")
        self.player1.setHappyStatus(randint(50, 80))
        self.player1.setParentStatus(1)
        self.player1.setMarriedStatus(0)
        self.player1.setAliveStatus(1)
        self.refreshStats()
        return
    else:
        self.rockBottom()
        self.refreshStats()
        return


def rockBottom(self):
    self.player1.setHappyStatus(0)
    self.player1.setParentStatus(0)
    self.player1.setMarriedStatus(0)
    self.player1.setAliveStatus(1)
    print("You have hit rock bottom...")
    if randint(0, 25) < 10:
        self.blowBrains()
        self.refreshStats()
        return
    else:
        print("You will start over...")
        self.player1.setHappyStatus(randint(5, 65))
        self.player1.setParentStatus(0)
        self.player1.setMarriedStatus(0)
        self.player1.setAliveStatus(1)
        self.refreshStats()
        return


def getSeparated(self):
    self.player1.setHappyStatus(25)
    self.player1.setParentStatus(0)
    self.player1.setMarriedStatus(1)
    self.player1.setAliveStatus(1)
    print("You have separated...\n")
    self.decideFate()
    self.refreshStats()
    return


def getHelp(self):
    self.player1.setHappyStatus(75)
    self.player1.setParentStatus(1)
    self.player1.setMarriedStatus(1)
    self.player1.setAliveStatus(1)
    print("You have sought help...\n")
    if randint(0, 25) < 15:
        print("Marriage therapy failed...\n")
        self.getSeparated()
        self.refreshStats()
        return
    else:
        print("Marriage therapy was successful!\n")
        self.refreshStats()
        return


def decideFate(self):
    print("The courts will decide...\n")
    if randint(0, 100) < 60:
        print("Shit did not go in your favor...")
        self.getDivorced()
        self.refreshStats()
        return
    else:
        print("The courts order you to marriage therapy...\n")
        self.getHelp()
        self.refreshStats()
        return


# Might be buggy


def happyEnding(self):
    if self.player1.getAliveStatus() == 1 and self.player1.getParentStatus() == 1 and \
            self.player1.getHappyStatus() >= 30:
        print("Rejoice, everything will be A OK!!!!\n")
        self.refreshStats()
        return
    else:
        if self.player1.getAliveStatus() == 1 and self.player1.getParentStatus() == 0 and \
                self.player1.getHappyStatus() < 30 and randint(0, 25) > 1:
            print("Why even try anymore...")
            self.blowBrains()
            print("You Died... The End\n")
            self.refreshStats()
            return
        else:
            print("It will be ok.\n")  # Bug ID: Does even if dead. Create con stmt in main()
            self.refreshStats()
            return
