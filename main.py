#coding:utf-8 
import sys 

if sys.platform.startswith("linux"):
    raise BadOsExecution("Please you need to have windows operating system !")
    exit()
else:
    import msvcrt
    import os
    import time 

class Rectangle:

    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y 
        self._w = w 
        self._h = h 
        print("Rectangle create in this adresse", self)

    def draw(self):
        countX = 0
        countY = 0
        x = 0 
        y = 0 

        while y < self.y:
            print("")
            y+=1 
  
        while countY < self.h:
            
            x = 0
            while x < self.x:
                print(" ", end="")
                x+=1

            while countX < self.w:
                print("*", end="")
                countX += 1 
            print("")
            countY += 1
            countX = 0

    def info(self):
        print("x = {} ; y = {}\nw = {} ; h = {}".format(self.x, self.y, self.w, self.h))

    # Accesseur 
    def _getX(self):
        return self._x 
    def _getY(self):
        return self._y 
    def _getW(self):
        return self._w
    def _getH(self):
        return self._h 

    # Muttateur 
    def _setX(self, x):
        try:
            assert type(x) == type(self._x)
        except AssertionError:
            print("Warning please x must be a number !")
        else:
            self._x = x 
    def _setY(self, y):
        try:
            assert type(y) == type(self._y)
        except AssertionError:
            print("Warning please y must be a number !")
        else:
            self._y = y 
    def _setW(self, w):
        try:
            assert type(w) == type(self._w)
        except AssertionError:
            print("Warning w must be a number !")
        else:
            self._w = w 
    def _setH(self, h):
        try:
            assert type(h) == type(self._h)
        except AssertionError:
            print("Warning h must be number !")
        else:
            self._h = h 

    x = property(_getX, _setX)
    y = property(_getY, _setY)
    w = property(_getW, _setW)
    h = property(_getH, _setH) 


quit = False 
rectangle = Rectangle(0, 0, 10, 10)
 
while not quit:
    if msvcrt.kbhit():
        catchKeyboardPressed = msvcrt.getch()  
        
        if catchKeyboardPressed == b"z":
            if rectangle.y > 0:
                rectangle.y -= 1
        elif catchKeyboardPressed == b"s":
            rectangle.y += 1 
        elif catchKeyboardPressed == b"d":
            rectangle.x += 1
        elif catchKeyboardPressed == b"+":
            rectangle.w += 1
            rectangle.h += 1
        elif catchKeyboardPressed == b"-":
            if rectangle.w > 0 and rectangle.h > 0:
                rectangle.w -= 1
                rectangle.h -= 1
        elif catchKeyboardPressed == b"q":
            if rectangle.x > 0:
                rectangle.x -= 1
        

    try:
        os.system("cls")
        rectangle.info()
        rectangle.draw()
        time.sleep(float(16 / 1000))
    except KeyboardInterrupt:
        print("You stop main.py application.")
        quit = True 