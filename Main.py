# LiTeMacro V1.0
# Done By Hugo Duarte

import pyautogui
import time
import psutil
from colormap import rgb2hex


def get_pixel_colour(i_x, i_y):
    import PIL.ImageGrab
    return PIL.ImageGrab.grab().load()[i_x, i_y]


def start_quest():
    time.sleep(1)
    print('Buscando botão para envio da missão')
    pixel_rgb = get_pixel_colour(1620, 915)
    while not rgb2hex(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]) == '#0CCECF':
        time.sleep(1)
        print('Não foi possível encontrar o botão, refazendo análise. Cor atual:')
        print(rgb2hex(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]))
        pixel_rgb = get_pixel_colour(1620, 915)
    pyautogui.click(1620, 915)

    print('Buscando botão de confirmação de operação')
    pixel_rgb = get_pixel_colour(1170, 700)
    while not rgb2hex(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]) == '#0BD40B':
        time.sleep(1)
        print('Não foi possível encontrar o botão, refazendo análize')
        pixel_rgb = get_pixel_colour(1170, 700)
    pyautogui.click(1170, 700)

    return True


while "LiteBringer.exe" in (i.name() for i in psutil.process_iter()):
    print('Iniciando macro..')
    time.sleep(3)
    # Clicando na janela do LiteBringer
    print('Clicando na janela do LiteBringer')
    pyautogui.click(1040, 80)
    time.sleep(1)
    # Esperar a conclusão da missão do primeiro char
    print('Iniciando a validação/envio do primeiro char')
    pixel_rgb = get_pixel_colour(1675, 260)
    while not rgb2hex(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]) == '#E4C560':
        print('Não foi possivel encontrar o icone de conclusão, refazendo análise. Cor atual:')
        print(rgb2hex(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]))
        time.sleep(1)
        pixel_rgb = get_pixel_colour(1675, 260)
    print('Icone encontrado, iniciando o procedimento de envio')
    pyautogui.click(1675, 260)
    start_quest()

    # Esperar a conclusão da missão do segundo char
    print('Iniciando a validação/envio do segundo char')
    pixel_rgb = get_pixel_colour(1675, 400)
    while not rgb2hex(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]) == '#E4C560':
        print('Não foi possivel encontrar o icone de conclusão, refazendo analise.  Cor atual:')
        print(rgb2hex(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]))
        time.sleep(1)
        pixel_rgb = get_pixel_colour(1675, 400)
    print('Icone encontrado, iniciando o procedimento de envio')
    pyautogui.click(1675, 400)
    start_quest()

    # Esperar a conclusão da missão do terceiro char
    print('Iniciando a validação/envio do terceiro char')
    pixel_rgb = get_pixel_colour(1675, 540)
    while not rgb2hex(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]) == '#E4C560':
        print('Não foi possivel encontrar o icone de conclusão, refazendo análise. Cor atual:')
        print(rgb2hex(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]))
        time.sleep(1)
        pixel_rgb = get_pixel_colour(1675, 540)
    print('Icone encontrado, iniciando o procedimento de envio')
    pyautogui.click(1675, 540)
    start_quest()

    # print(pyautogui.position())
    #print(rgb2hex(get_pixel_colour(315, 380)))
