from PyUI.Screen import Screen 
from PyUI.PageElements import * 
from random import randint
from datetime import datetime

class GameScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (20,200,120))
        self.fix = True
        self.upX = 1
        self.upY = 1
        self.speed = 7
        self.startTime = datetime.now()
        self.endTime = datetime.now()
        self.state = {
            "molePos" : (100, 100),
            "moleClicks"  : 0,
            "totalClicks" : 0,
            "lastClick" : -1,
            "time" : self.endTime - self.startTime
        }

    def moveMole(self, currPos):
        newX = 0
        newY = 0

        #Update X position
    
        if self.state["molePos"][0] >= 750:
            self.upX = False
        if self.state["molePos"][0] <= 50:
            self.upX = True

        if self.upX == False:
            newX = -self.speed
        if self.upX == True:
            newX = self.speed

        #Update Y position
    
        if self.state["molePos"][1] >= 550:
            self.upY = False
        if self.state["molePos"][1] <= 50:
            self.upY = True

        if self.upY == False:
            newY = -self.speed
        if self.upY == True:
            newY = self.speed
    
        return ((currPos[0] + newX), (currPos[1] + newY))

    def elementsToDisplay(self):
        self.elements = [
            BGButton(),
            Mole((100, 100), self),
            Button((400, 25), 125, 25, str(self.state["time"]), (20,200,160), (0,0,0)),
        ]

        #Update Time

        if self.state["moleClicks"] != 10:
            self.endTime = datetime.now()
            self.state["time"] = self.endTime - self.startTime

        #Check if mole was moved

        if self.state["lastClick"] + 1 != self.state["moleClicks"]:
            self.fix = True
            self.state["lastClick"] += 1
        else:
            self.fix = False

        #Slide Mole

        self.state["molePos"] = self.moveMole(self.state["molePos"])

        #Win check

        if self.state["moleClicks"] == 10:
            
            self.elements.remove(self.elements[1])
            self.elements.append(Button((400, 275), 300, 200, "", (20,200,120), (20,200,160)))
            self.elements.append(Label((400, 250), 300, 50, "You Won!", 50))
            self.elements.append(Label((385, 300), 300, 50, "Total Clicks:", 30))
            self.elements.append(Label((500, 300), 300, 50, str(self.state["totalClicks"]), 30))

class Mole(Image):
   def __init__(self, molePos, screen):
       super().__init__(screen.state["molePos"], 100, 100, './imgs/moleImg.jpg')

   def onClick(self, screen):
       screen.state["molePos"] = moveMoleToRight(screen.state["molePos"])
       screen.state["moleClicks"] += 1
       screen.state["totalClicks"] += 1

class BGButton(Image):
    def __init__(self):
        super().__init__((400, 300), 800, 600, './imgs/bg.jpg')

    def onClick(self, screen):
        screen.state["totalClicks"] += 1

def moveMoleToRight(currPos):
    newX = randint(50, 750)
    newY = randint(50, 550)
    return (newX, newY)

