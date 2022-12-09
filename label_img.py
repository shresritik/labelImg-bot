import pyautogui as py
import time

while(1):

    print("start")
    time.sleep(3)
    #copy boundary
    py.keyDown("ctrl")
    py.keyDown("v")
    print("ctrl+v down")
    time.sleep(1)
    py.keyUp("ctrl")
    py.keyUp("v")
    print("ctrl+v up")
    print("save down")
    time.sleep(1)
    # save
    py.keyDown("ctrl")
    py.keyDown("s")
    print("save down")

    time.sleep(1)
    py.keyUp("ctrl")
    py.keyUp("s")
    print("save up")

    time.sleep(1)
    print("Do you want to continue")
    time.sleep(3)
    
    # next image
    py.press('d')
    
    time.sleep(1)
