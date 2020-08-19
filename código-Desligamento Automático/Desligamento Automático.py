
import pyautogui
import time

#Função para ler apenas letras:
def leiastr(msg):
    while True:
        print()
        verif=str(input(msg).strip().replace(" ", ""))
        if verif.isalpha() == False:
            print()
            print("ERRO:""\nDigite apenas letras.")
            continue
        else:
            verif=verif.lower()
            return verif


#Função verificadora de números decimais
def leiafloat(msg):
    while True:
        try:
            print()
            N=float(input(msg).strip().replace(" ", ""))
        except (ValueError, TypeError, IndexError):
            print()
            print("ERRO:""\nDigite apenas números.")
            continue
        else:
            return N


def initshow():
    print("-"*27)
    print("  Desligamento Automático")
    print("-"*27)


#Função para abrir terminal:
def terminal():
    global timesys
    pyautogui.hotkey("win")
    time.sleep(timesys)
    pyautogui.typewrite("cmd")
    time.sleep(timesys)
    pyautogui.press("Enter")
    time.sleep(timesys)


def options():
    perg=str("Deseja marcar um tempo de desligamento ou reinicialização automática ou cancelar alguma predefinição já existente? ")
    perg=leiastr(perg)
    if "can" in perg:
        terminal()
        pyautogui.typewrite("shutdown -a")
    else:
        if "re" in perg:
            tempoff=str("Digite em quantos minutos deseja que o computador reinicie: ")
        else:
            tempoff=str("Digite em quantos minutos deseja que o computador desligue: ")
        tempoff=leiafloat(tempoff)
        tempoff=float(tempoff)
        terminal()
        if  "re" in perg:
            pyautogui.typewrite(f"shutdown -r -t {int(tempoff*60)}")
        else:
            pyautogui.typewrite(f"shutdown -s -t {int(tempoff*60)}")   


def end():
    time.sleep(timesys/2)
    pyautogui.press("Enter")
    time.sleep(timesys/2)
    pyautogui.hotkey("Alt", "F4")
    print()
    print("Operação feita com sucesso!")
    input()


def run():
    global timesys

    timesys=1
    initshow()
    options()
    end()


run()






