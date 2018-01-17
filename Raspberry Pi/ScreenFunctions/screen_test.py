from screen_functions import Screen
import time

screen = Screen()
time.sleep(0.5)
screen.off()

screen.setHalf(0, '9', [0, 0, 255], [255, 255, 255])
screen.setHalf(1, '8', [0, 0, 255], [255, 255, 255])
time.sleep(0.3)
screen.set_rotation(180)
screen.setHalf(0, '2', [0, 0, 255], [255, 255, 255])
screen.setHalf(1, '3', [0, 0, 255], [255, 255, 255])
screen.off()
