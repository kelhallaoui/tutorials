from Screen import Screen
from Player import Player
import numpy as np
import time

class Game(object):
  
  def __init__(self, sense):
    x, y = 1, 3
    self.player = Player(x, y)
    self.screen = Screen(sense)
    self.screen.setWhiteScreen()
    
    self.state = 0
    self.counter = 0
    self.points = 0

  def initPlayerColor(self):
    self.screen.chooseColorScreen('R', 'G', 'P', 'A')

  def getPlayerColor(self, event):
    if event.action == 'pressed' and event.direction == 'up':
      self.player.setColor('A')
    if event.action == 'pressed' and event.direction == 'down':
      self.player.setColor('G')
    if event.action == 'pressed' and event.direction == 'right':
      self.player.setColor('R')
    if event.action == 'pressed' and event.direction == 'left':
      self.player.setColor('P')
    if not self.player.getColor == ' ':
      self.state = 1
      
  def initStartScreen(self):
    self.screen.setWhiteScreen()
    x, y = self.player.getXY()
    self.screen.drawPlayer(x, y, self.player.getColor())
    
  def getState(self):
    return self.state

  def setState(self, state):
    """ Game states
    0. Get player color
    1. Wait for start
    2. Playing
    """
    self.state = state

  def bttnPressed(self, event):
    if event.action == 'pressed' and event.direction == 'right':
      self.player.moveUp()
    if event.action == 'pressed' and event.direction == 'left':
      self.player.moveDown()
      
  def update(self):
    if self.counter % 4 == 0:
      newCol = np.random.choice(2,8)
    else:
      newCol = np.zeros((8,))
    self.screen.update_screen(newCol)
    x, y = self.player.getXY()
    self.screen.drawPlayer(x, y, self.player.getColor())
    
    if self.gameover():
      return False
    else:
      self.points += 1
      self.counter += 1
      time.sleep(0.2)
      return True

  def getCounter(self):
    return self.counter

  def setCounter(self):
    self.counter += 1
      
  def gameover(self):
    x, y = self.player.getXY()
    B = [0, 0, 255]
    if self.screen.getScreen()[8*y + x] == B:
      return True
    else: return False

  def gameoverScreen(self):
    self.screen.gameoverScreen(self.points)
