# LiTeMacro V2.0
# Done By Hugo Duarte

#Requirements: A HQ icon image of misson complete scroll, send on quest blue button and confirm green button.

import pyautogui
import time
import psutil
from screeninfo import get_monitors


def start_quest():
    time.sleep(1)
    
    # Solicitar envio para missão
    print('Buscando botão para envio da missão')
    image_name = 'SendOnQuest.png'
    icon = pyautogui.locateCenterOnScreen(image_name, confidence=0.8)

    while icon is None:
        print("Não foi possivel encontrar o icone de envio, refazendo análise.") 
        time.sleep(1)
        icon = pyautogui.locateCenterOnScreen(image_name, confidence=0.8)

    print('Icone encontrado, iniciando o procedimento de envio')
    time.sleep(1)
    pyautogui.click(icon[0], icon[1])

    # Confirmando envio para missão
    print('Buscando botão de confirmação da missão')
    image_name = 'Confirm.png'
    icon = pyautogui.locateCenterOnScreen(image_name, confidence=0.8)

    while icon is None:
        print("Não foi possivel encontrar o icone de confirmação, refazendo análise.") 
        time.sleep(1)
        icon = pyautogui.locateCenterOnScreen(image_name, confidence=0.8)

    print('Icone encontrado, confirmando o envio para missão')
    time.sleep(1)
    pyautogui.click(icon[0], icon[1])

    return True


print('Iniciando macro..')

while "LiteBringer.exe" in (i.name() for i in psutil.process_iter()):
    # Esperar a conclusão da missão
    print('Iniciando a validação/envio do char')
    image_name = 'QuestCompleted.png'
    icon = pyautogui.locateCenterOnScreen(image_name, confidence=0.8)

    while icon is None:
        print("Não foi possivel encontrar o icone de missão concluida, refazendo análise.") 
        time.sleep(1)
        icon = pyautogui.locateCenterOnScreen(image_name, confidence=0.8)

    print('Icone encontrado, iniciando o procedimento de reenvio')
    time.sleep(1)
    pyautogui.click(icon[0], icon[1])
    start_quest()