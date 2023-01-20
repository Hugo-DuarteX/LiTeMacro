# LiTeMacro V2.0
# Done By Hugo Duarte

# Requirements: A HQ icon image of misson complete scroll, send on quest blue button and confirm green button.

import pyautogui
import time
import psutil
from screeninfo import get_monitors


def check_mission():
    # Esperar a conclusão da missão
    print('Iniciando a validação/envio do char')
    image_name = resolution+'QuestCompleted.png'
    icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)

    x = 0

    while icon is None:
        print("Não foi possivel encontrar o icone de missão concluida, refazendo análise.")
        time.sleep(1)
        icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)
        if x == 6:
            print('Desencontro das etapas. voltando ao menu inicial..')
            pyautogui.press('esc')
            main_menu = resolution+'Back.png'
            time.sleep(2)
            icon_menu = pyautogui.locateCenterOnScreen(main_menu, confidence=nr_confidence)
            time.sleep(2)
            if icon_menu is not None:
                pyautogui.click(icon_menu[0], icon_menu[1])
            x = 0

        x = x+1

    print('Icone encontrado, iniciando o procedimento de reenvio')
    time.sleep(2)
    pyautogui.click(icon[0], icon[1])


def start_quest():
    # Solicitar envio para missão
    print('Buscando botão para envio da missão')
    image_name = resolution+'SendOnQuest.png'
    icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)

    x = 0

    while icon is None:
        print("Não foi possivel encontrar o icone de envio, refazendo análise.")
        time.sleep(1)
        icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)
        if x == 6:
            break
        x = x+1

    if x == 6:
        check_mission()

    print('Icone encontrado, iniciando o procedimento de envio')
    time.sleep(2)
    pyautogui.click(icon[0], icon[1])


def confirm_quest():
    # Confirmando envio para missão
    print('Buscando botão de confirmação da missão')
    image_name = resolution+'Confirm.png'
    icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)

    x = 0

    while icon is None:
        print("Não foi possivel encontrar o icone de confirmação, refazendo análise.")
        time.sleep(1)
        icon = pyautogui.locateCenterOnScreen(image_name, confidence=nr_confidence)
        if x == 6:
            break
        x = x+1

    if x == 6:
        start_quest()

    print('Icone encontrado, confirmando o envio para missão')
    time.sleep(2)
    pyautogui.click(icon[0], icon[1])


print('Iniciando macro..')
time.sleep(2)
for m in get_monitors():
    resolution = str(m.width)+'x'+str(m.height)

if resolution == '1920x1080':
    nr_confidence = 0.8
else:
    nr_confidence = 0.5

while "LiteBringer.exe" in (i.name() for i in psutil.process_iter()):
    check_mission()
    start_quest()
    confirm_quest()
