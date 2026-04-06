import random
import os
import sys
import time
import webbrowser

def abrirNavegador():
    urls = [
        "https://youtu.be/xvFZjo5PgG0?si=KOAwbTTKpEMDpuT7"
        "https://youtu.be/EFALkpovkIE?si=tsn6kYrPAyNk0Ii9"
    ]
    for site in urls:
        webbrowser.open(site)

def desligar():
    time.sleep(7)
    if sys.platform == "win32":
        os.system("shutdown /s /t 1")
    elif sys.platform == "linux" or sys.platform == "linux2":
        os.system("shutdown -h now")    
    elif sys.platform == "darwin":
        os.system("sudo shutdown -h now")

def evento_aleatorio():
    numOpcoes = 6
    escolhaIndesejada = random.randint(1, numOpcoes)

    escolha = int(input(f"Escolha um número entre 1 e {numOpcoes}: "))

    if escolha == escolhaIndesejada:
        print("Ops! o PC será desligado")
        abrirNavegador()
        desligar()
    else:
        print("Você está seguro, por enquanto...")

evento_aleatorio()