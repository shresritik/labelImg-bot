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
    time.sleep(3)
    print("Saving ...")
    # save
    py.keyDown("ctrl")
    py.keyDown("s")
    print("ctrl+s down")

    time.sleep(1)
    py.keyUp("ctrl")
    py.keyUp("s")
    print("ctrl+s up")
    print("Saved")

    time.sleep(1)
    print("Do you want to continue")
    time.sleep(3)
    
    # next image
    py.press('d')
    
    time.sleep(1)
