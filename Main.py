# LiTeMacro V4.0
# Done By Hugo Duarte

# Requirements: A HQ icon image of misson complete scroll, send on quest blue button and confirm green button.

import pyautogui
import time
import psutil
from screeninfo import get_monitors

def main_menu():
    print('Desencontro das etapas. voltando ao menu inicial..')
    time.sleep(1)
    pyautogui.press('esc')
    image_cancel = resolution+'Cancel.png'
    time.sleep(1)
    icon_cancel = pyautogui.locateCenterOnScreen(image_cancel, confidence=nr_confidence)
    time.sleep(1)
    if icon_cancel is not None:
        pyautogui.click(icon_cancel[0], icon_cancel[1])
    image_back = resolution+'Back.png'
    time.sleep(1)
    icon_menu = pyautogui.locateCenterOnScreen(image_back, confidence=nr_confidence)
    time.sleep(1)
    if icon_menu is not None:
        pyautogui.click(icon_menu[0], icon_menu[1])
    check_mission()
    

def check_mission():
    # Esperar a conclusão da missão
    print('Iniciando a validação/envio do char')
    image_name = resolution+'QuestCompleted.png'
    image_char = resolution+'Characters.png'
    time.sleep(2)
    icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)

    while icon is None:
        print("Não foi possivel encontrar o icone de missão concluida, refazendo análise.")
        time.sleep(2)
        icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)
        icon_c = pyautogui.locateCenterOnScreen(image_char, confidence=nr_confidence)
        if icon_c is None:
            main_menu()

    print('Icone encontrado, iniciando o procedimento de reenvio')
    time.sleep(1)
    pyautogui.click(icon[0], icon[1])

    start_quest()


def start_quest():
    # Solicitar envio para missão
    print('Buscando botão para envio da missão')
    image_name = resolution+'SendOnQuest.png'
    image_map1 = resolution+'Map1.png'
    time.sleep(2)
    icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)

    while icon is None:
        print("Não foi possivel encontrar o icone de envio, refazendo análise.")
        time.sleep(2)
        icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)
        icon_m1 = pyautogui.locateCenterOnScreen(image_map1, confidence=nr_confidence)
        if icon_m1 is None:
            main_menu()

    print('Icone encontrado, iniciando o procedimento de envio')
    time.sleep(1)
    pyautogui.click(icon[0], icon[1])

    confirm_quest()


def confirm_quest():
    # Confirmando envio para missão
    print('Buscando botão de confirmação da missão')
    image_name = resolution+'Confirm.png'
    image_map2 = resolution+'Map2.png'
    time.sleep(2)
    icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)

    while icon is None:
        print("Não foi possivel encontrar o icone de confirmação, refazendo análise.")
        time.sleep(2)
        icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)
        icon_m2 = pyautogui.locateCenterOnScreen(image_map2, confidence=nr_confidence)
        if icon_m2 is None:
            main_menu()

    print('Icone encontrado, confirmando o envio para missão')
    time.sleep(1)
    pyautogui.click(icon[0], icon[1])


print('Iniciando macro..')
time.sleep(1)
for m in get_monitors():
    resolution = str(m.width)+'x'+str(m.height)

if resolution == '1920x1080':
    nr_confidence = 0.8
else:
    nr_confidence = 0.5

while "LiteBringer.exe" in (i.name() for i in psutil.process_iter()):
    check_mission()
