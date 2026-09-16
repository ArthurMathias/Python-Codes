import webbrowser
import pyautogui
from time import sleep

webbrowser.open("https://www.tiktok.com/@neymarjr")
sleep(10)
pyautogui.click(581, 726, duration=2)  # entrar no video
sleep(4)

try:
    ja_curtido = pyautogui.locateOnScreen(
        'curtido.png',
        confidence=0.9,
        region=(1200, 650, 200, 150)
    )
except pyautogui.ImageNotFoundException:
    ja_curtido = None

print(ja_curtido)

if ja_curtido:
    print("Video ja curtido, pulando...")
    pyautogui.press('down')
else:
    print("Video nao curtido, curtindo agora...")
    pyautogui.click(1174, 405, duration=2)  # Curtida
    sleep(2)
    pyautogui.press('down')