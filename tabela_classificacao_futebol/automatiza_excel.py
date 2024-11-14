import pyautogui
import time

time.sleep(5)
#pos = pyautogui.position()
#print(pos)
pyautogui.click(46, 183, duration=0.5)
pyautogui.write("E5")
pyautogui.press('enter')
pyautogui.write("Preenchendo a celula")
pyautogui.press('enter')
