from Game import Game
from sense_hat import SenseHat
import numpy as np
import time
import sys

sense = SenseHat()
game = Game(sense)

game.initPlayerColor()
while game.getState() == 0:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            game.getPlayerColor(event)

# Start game screen
game.initStartScreen()
while game.getState() == 1:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            game.setState(2)


print('Playing game...')

# Play game
while True:
    for event in sense.stick.get_events():
        game.bttnPressed(event)

    if not game.update():
        break


    
game.gameoverScreen()
