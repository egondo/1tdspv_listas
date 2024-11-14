#pip install pyautogui
import pyautogui
import time

def preenche_formulario(timeA, placarA, timeB, placarB):
    pyautogui.moveTo(100, 220, duration=0.5)
    pyautogui.click()
    pyautogui.typewrite(timeA)
    pyautogui.moveTo(300, 220, duration=0.5)
    pyautogui.click()
    pyautogui.typewrite(placarA)

    pyautogui.moveTo(430, 220, duration=0.5)
    pyautogui.click()
    pyautogui.typewrite(placarB)

    pyautogui.moveTo(500, 220, duration=0.5)
    pyautogui.click()
    pyautogui.typewrite(timeB)

    time.sleep(5)
    pos = pyautogui.position()
    print(pos)
    pyautogui.click(58, 264, duration=0.5) #cadastra
    pyautogui.click(91, 58, duration=0.5)  #recarrega

time.sleep(5)
lista = [
    ["Brasil", "1", "Venezuela", "1"],
    ["Paraguai", "2", "Colômbia", "0"],
    ["Argentina", "1", "Uruguai", "2"],
    ["Peru", "3", "Equador", "1"]
]

for dado in lista:
    preenche_formulario(dado[0], dado[1], dado[2], dado[3])