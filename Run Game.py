from PyUI.Window import Window
from GameScreen import GameScreen

window = Window("Example App", (0,255,0))

gameScreen = GameScreen(window)

screen = gameScreen

while True:

    window.checkForInput(screen)
    window.update(screen)
