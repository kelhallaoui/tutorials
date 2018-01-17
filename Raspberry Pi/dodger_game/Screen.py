from sense_hat import SenseHat
import time

class Screen(object):

  def __init__(self, sense):
    self.colors = {'W': [255, 255, 255],
                   'O': [0, 0, 0],
                   'R': [255, 0, 0],
                   'B': [0, 0, 255],
                   'G': [0, 255, 0],
                   'P': [255, 20, 147],
                   'A': [255, 140, 0]}
    # Set up the screen
    self.sense = sense
    self.sense.set_rotation(90)
    self.sense.clear()
    self.sense.low_light = True
    
  def setWhiteScreen(self):
    # Initialized with a white screen.
    W = self.colors['W']
    self.screen = [
                    W, W, W, W, W, W, W, W,
                    W, W, W, W, W, W, W, W,
                    W, W, W, W, W, W, W, W,
                    W, W, W, W, W, W, W, W,
                    W, W, W, W, W, W, W, W,
                    W, W, W, W, W, W, W, W,
                    W, W, W, W, W, W, W, W,
                    W, W, W, W, W, W, W, W
                  ]
    self.sense.set_pixels(self.screen)

  def update_screen(self, new_col):
    new_screen = []
    for i in range(0, 8):
      list.extend(new_screen, self.screen[i*8 + 1:i*8+8])
      if new_col[i] == 0:
        list.extend(new_screen, [self.colors['O']])
      else:
        list.extend(new_screen, [self.colors['B']])
    self.screen = new_screen
    self.sense.set_pixels(self.screen)

  def drawPlayer(self, x, y, color):
    color = self.colors[color]
    self.sense.set_pixel(x, y, color[0], color[1], color[2])

  def getScreen(self):
    return self.screen

  def chooseColorScreen(self, c1, c2, c3, c4):
    R = self.colors[c1]
    G = self.colors[c2]
    P = self.colors[c3]
    A = self.colors[c4]
    W = self.colors['W']
    self.screen = [
                    W, W, W, W, W, W, W, W,
                    W, W, W, R, R, W, W, W,
                    W, W, W, R, R, W, W, W,
                    W, G, G, W, W, A, A, W,
                    W, G, G, W, W, A, A, W,
                    W, W, W, P, P, W, W, W,
                    W, W, W, P, P, W, W, W,
                    W, W, W, W, W, W, W, W
                  ]
    self.sense.set_pixels(self.screen)
    time.sleep(0.05)
  
  def gameoverScreen(self, points):
    R = [255, 0, 0]
    O = [255, 255, 255]
    screen_display = [
      R, R, R, R, R, R, R, R,
      R, O, R, R, R, R, O, R,
      R, R, O, R, R, O, R, R,
      R, O, R, R, R, R, O, R,
      R, R, R, R, R, R, R, R,
      R, R, R, O, O, R, R, R,
      R, R, O, O, O, O, R, R,
      R, R, R, R, R, R, R, R
      ]

    self.sense.set_pixels(screen_display)
    time.sleep(0.5)
    self.sense.show_message("Points: " + str(points), scroll_speed = 0.06, text_colour = [255, 255, 255], back_colour = [255, 0, 0])
    self.sense.clear()
