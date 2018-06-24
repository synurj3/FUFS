# Good events for the game
# from FUFS import *
# from functions import *
# from lists import *
from Resources import *
from random import *

# def getJob(self):
#     print("Congrats!!! You have gotten a job.\nYour happiness has increased by 10!")
#     me.setHappyStatus(me.getHappyStatus() + 10)
#     return
#
#
# def blazeUp(me):
#     print("It's 420!!! TIME TO BLAZE!!!\nYour happiness has been restored!")
#     me.setHappyStatus(100)
#     return

def magicalSesh(self):
    print("You have a Magical Moon Rock Blunt...\nYou decide to smoke it...")
    self.player1.setHappyStatus("420")
    self.lblHappy.setText("420")
    self.tbStatusMsg.append("You have a Magical Moon Rock Blunt...")
    self.tbStatusMsg.append("You decide to smoke it...")
    self.listGood.append("Immune to everything!")
    self.listBad.clear()
    self.tbStatusMsg.append("You have acquired immunity to everything")
    self.tbStatusMsg.append("All negative status effects are cleared")
    self.setPic(resStonedAlien)


# def magicalSesh(self):
#     print("You have a Magical Moon Rock Blunt...\nYou decide to smoke it...")
#     self.player1.setHappyStatus(420)
#     self.lblHappy.setText("420")
#     self.tbStatusMsg.append("You have a Magical Moon Rock Blunt...")
#     self.tbStatusMsg.append("You decide to smoke it...")
    # Will cure all negative status except death
    # Unless... you have a magical blunt in possession at time of death (FUTURE)


# def celebrate(self):
#     print("Congrats!!  It's a celebration!\nYou are celebrating something")  # , goodList[randint(0, 1)])
#     self.player1.setHappyStatus(me.getHappyStatus() + 5)