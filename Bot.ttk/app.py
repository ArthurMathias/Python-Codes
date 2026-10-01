import webbrowser
import pyautogui
from time import sleep

pyautogui.FAILSAFE = True  
pyautogui.PAUSE = 0.5

REGIAO_CURTIDA = (1124, 355, 100, 100)  
BOTAO_CURTIR = (1174, 405)
QTD_VIDEOS = 10

def ja_esta_curtido():
    try:
        return pyautogui.locateOnScreen(
            'curtido.png', confidence=0.8, region=REGIAO_CURTIDA
        ) is not None
    except pyautogui.ImageNotFoundException:
        return False

webbrowser.open("https://www.tiktok.com/@neymarjr")
sleep(10)
pyautogui.click(581, 726, duration=1)
sleep(4)

for i in range(QTD_VIDEOS):
    if ja_esta_curtido():
        print(f"[{i+1}] já curtido, pulando...")
    else:
        print(f"[{i+1}] curtindo...")
        pyautogui.click(*BOTAO_CURTIR, duration=1)
        sleep(2)
    pyautogui.press('down')
    sleep(3)