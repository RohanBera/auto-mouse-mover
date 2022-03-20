import pyautogui as pgui
import time

flag = 1
while True :
    pos1 = pgui.position()
    time.sleep(5)
    pos2 = pgui.position()

    if pos1 == pos2: 
        if flag == 1:
            pgui.moveRel(0, -5)
            flag = 0
        else:
            pgui.moveRel(0, 5)
            flag = 1