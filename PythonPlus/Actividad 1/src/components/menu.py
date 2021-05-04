import PySimpleGUI as sg
from src.windows import menu
from src.handlers import PES, PAISES

def start():
    window = loop()
    window.close

def loop():
    window = menu.build()
    while True:
        event, values = window.read()
        if event in ('-BOT_SALIR-'):
            break

        if event in ('-BOT_FM-'):
            PES.archivo_PES()

        if event in ('-BOT_PAISES-'):
            PAISES.archivo_Paises()

    return window