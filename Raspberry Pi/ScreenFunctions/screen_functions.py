from sense_hat import SenseHat
import numpy as np
import time
import sys

class Screen(SenseHat):

    def __init__(self):
        self.sense = SenseHat()
        self.sense.set_rotation(90)
        self.sense.clear()
        self.sense.low_light = True

        self.setAll([255, 255, 255])
        
    def set_rotation(self, rot):
        self.sense.set_rotation(rot)

    def off(self):
        self.setAll([0, 0, 0])

    def setAll(self, color):
        O = color
        screen_display = [
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O
            ]

        self.sense.set_pixels(screen_display)

    def setHalf(self, half, char, text_color, back_color):
        pixels = self.charToPixel(char)
        if half == 0:
            self.setHalfPixels(pixels, 0, 0, text_color, back_color)
        elif half == 1:
            self.setHalfPixels(pixels, 4, 0, text_color, back_color)
            
    def setHalfPixels(self, pixels, xi, yi, text_color, back_color):
        counter = 0
        y = yi
        for i in range(0, 8):
            x = xi
            for j in range(0, 4):
                if pixels[counter] == 1: self.sense.set_pixel(x, y, text_color)
                else: self.sense.set_pixel(x, y, back_color)
                counter += 1
                x += 1
            y += 1
            
    def charToPixel(self, char):
        if char == '0':
            return [0,0,1,0,
                    0,1,1,1,
                    0,1,0,1,
                    0,1,0,1,
                    0,1,0,1,
                    0,1,0,1,
                    0,1,1,1,
                    0,0,1,0]
        elif char == '1':
            return [0,1,1,0,
                    0,0,1,0,
                    0,0,1,0,
                    0,0,1,0,
                    0,0,1,0,
                    0,0,1,0,
                    0,1,1,1,
                    0,1,1,1]
        elif char == '2':
            return [0,1,1,1,
                    0,1,0,1,
                    0,0,0,1,
                    0,0,1,1,
                    0,1,1,0,
                    0,1,0,0,
                    0,1,0,0,
                    0,1,1,1]
        elif char == '3':
            return [0,1,1,1,
                    0,1,0,1,
                    0,0,0,1,
                    0,0,1,0,
                    0,0,1,0,
                    0,0,0,1,
                    0,1,0,1,
                    0,1,1,1]
        elif char == '4':
            return [0,1,0,1,
                    0,1,0,1,
                    0,1,0,1,
                    0,1,1,1,
                    0,0,0,1,
                    0,0,0,1,
                    0,0,0,1,
                    0,0,0,1]
        elif char == '5':
            return [0,1,1,1,
                    0,1,0,0,
                    0,1,0,0,
                    0,1,1,1,
                    0,0,0,1,
                    0,0,0,1,
                    0,1,0,1,
                    0,1,1,1]
        elif char == '6':
            return [0,1,1,1,
                    0,1,0,0,
                    0,1,0,0,
                    0,1,1,1,
                    0,1,0,1,
                    0,1,0,1,
                    0,1,0,1,
                    0,1,1,1]
        elif char == '7':
            return [0,1,1,1,
                    0,0,0,1,
                    0,0,0,1,
                    0,0,0,1,
                    0,0,0,1,
                    0,0,0,1,
                    0,0,0,1,
                    0,0,0,1]
        elif char == '8':
            return [0,1,1,1,
                    0,1,0,1,
                    0,1,0,1,
                    0,1,1,1,
                    0,1,1,1,
                    0,1,0,1,
                    0,1,0,1,
                    0,1,1,1]
        elif char == '9':
            return [0,1,1,1,
                    0,1,0,1,
                    0,1,0,1,
                    0,1,1,1,
                    0,0,0,1,
                    0,0,0,1,
                    0,0,0,1,
                    0,1,1,1]
        else: return [1]*32
