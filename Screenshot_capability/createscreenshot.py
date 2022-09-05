from os import remove
from time import sleep
from datetime import datetime
import pyautogui


image_names = []
for i in range(10): #temoprary 
    screenshot = pyautogui.screenshot()
    file_name = datetime.now().strftime("%H-%M-%S")

    image_names.append(file_name + '.png')
    screenshot.save(fr"C:\Users\Niki\Documents\python\wow_player\Mogrin\Screenshot_capability\{image_names[-1]}")
    
    if len(image_names) > 5:
        remove(image_names.pop(0))
    sleep(2)