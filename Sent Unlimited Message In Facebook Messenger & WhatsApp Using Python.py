# -*- coding: utf-8 -*-
# pip install pyautogui
import pyautogui
import time
n = 5
while n > 0:
    time.sleep(4)
    message = "How are you!"
    pyautogui.typewrite(message)
    time.sleep(2)
    pyautogui.press("enter")
    n -= 1