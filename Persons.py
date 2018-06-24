#######################################################
# Title:            Persons Class File
# Filename:         Persons.py
# Prepared For:     Personal Amusement
# Programmer:       Joseph Knight
# Development Date: 4/20/2018
#
# Purpose:  Class file for Person
#
# Version History:  v0.0.5 -- Alpha test sent
# v0.0.5 -- No user input yet.  Actions controlled
#   by a random integer generator and conditional
#   statements.  Class moved to individual file.
#
#############################################


class Person:
    # Start the game as Bob, Happy Level 100, Parent, Married, and Alive
    def __init__(self, name='Bob', happy=100, parent=1, married=1, alive=1,
                 goodStats=[], badStats=[]):
        self.__name = name
        self.__happy = happy
        self.__parent = parent
        self.__married = married
        self.__alive = alive
        self.__goodStats = goodStats
        self.__badStats = badStats

    # Setters
    def setName(self, name):
        self.__name = name

    def setHappyStatus(self, happy):
        self.__happy = happy

    def setParentStatus(self, parent):
        self.__parent = parent

    def setMarriedStatus(self, married):
        self.__married = married

    def setAliveStatus(self, alive):
        self.__alive = alive

    def addGood(self, goodStat):
        self.__goodStats.append(goodStat)

    def addBad(self, badStat):
        self.__badStats.append(badStat)

    # Getters
    def getName(self):
        return self.__name

    def getHappyStatus(self):
        return self.__happy

    def getParentStatus(self):
        return self.__parent

    def getMarriedStatus(self):
        return self.__married

    def getAliveStatus(self):
        return self.__alive

    def getGood(self):
        return self.__goodStats

    def getBad(self):
        return self.__badStats

    # Showers
    def showName(self):
        text = str("Your name is " + self.__name + ".")
        print(text)
        return text

    def showHappyStatus(self):
        num = str(self.__happy)
        text = str("Your happiness level is " + num + ".")
        print(text)
        return text

    def showParentStatus(self):
        if self.__parent == 1:
            text = str("You are a parent.")
            print(text)
            return text
        else:
            text = str("You are not a parent")
            print(text)
            return text

    def showMarriedStatus(self):
        if self.__married == 1:
            text = str("You are married.")
            print(text)
            return text
        else:
            text = str("You are not married")
            return text

    def showAliveStatus(self):
        if self.__alive == 1:
            text = "You are alive!"
            print(text)
            return text
        else:
            text = "You are dead!"
            print(text)
            return text


    def showAliveGui(self):
        if self.__alive == 1:
            text = "You are alive!"
            return text

    def showGood(self):  # Functional..  Make this look pretty later
        print("Your perks are:")
        i = 0
        while i <= self.__goodStats.__len__() - 1:
            print(self.__goodStats[i])
            i += 1

    def showBad(self):  # Functional..  Make this look pretty later
        print("Your downfalls are:")
        i = 0
        while i <= self.__badStats.__len__() - 1:
            print(self.__badStats[i])
            i += 1