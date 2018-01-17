class Player(object):
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.color = ' '

  def moveUp(self):
    if self.y>0: self.y -= 1

  def moveDown(self):
    if self.y<7: self.y += 1

  def getXY(self):
    return self.x, self.y

  def getColor(self):
    return self.color

  def setColor(self, color):
    self.color = color
