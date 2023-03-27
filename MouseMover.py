import pyautogui
import time
import math
from geopy import distance
#print(pyautogui.position()) can be used to find where to type in the coords in Bermuda
x = 109
y = 685 # Basically the bottom left corner of my pc

def pathMaker(x1, y1, x2, y2, speed, travelInt):
    #Using 2 GPS coordinates this splits it into "travelInt" times equal segments and then returns the coordinates.
    dist = distance.distance([x1,y1],[x2,y2]).km
    steps = round((dist*1000 / speed)/travelInt)
    coordinates = []
    for i in range(0, steps):
        coordinates.append([x1+(((x2-x1)/steps)*i), y1+(((y2-y1)/steps)*i)])
    coordinates.append([x2, y2])
    print(len(coordinates))
    return coordinates

def changeLocation(path):
  #This actually moves the mouse and then types in the stuff
    for i in range(len(path)):
        pyautogui.moveTo(x, y, duration = 0)
        pyautogui.click(x, y)
        pyautogui.hotkey("ctrlleft", "a")
        pyautogui.press("backspace")
        pyautogui.typewrite(str(path[i][0])+","+str(path[i][1]))
        pyautogui.press("enter")
        time.sleep(0.5)

coordinates = []##Copy paste from Geocircle.py, ik its very scuffed 
num = 1#How many times to repeat traveling to the coordinates

for j in range(0, num):
  #Main Loop
    for i in range(0, len(coordinates)-1):
        changeLocation(pathMaker(coordinates[i][0], coordinates[i][1], coordinates[i+1][0], coordinates[i+1][1], 2.9, 0.5))
    print(str(j)+"/"+str(num))
