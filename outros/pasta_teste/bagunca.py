import pyautogui
import pygetwindow
import time
from screeninfo import get_monitors

def encontrar_janela_com_primeiro_nome(nome_substring):
    for janela in pygetwindow.getAllWindows():
        palavras_nome_janela = janela.title.split()
        if palavras_nome_janela and palavras_nome_janela[0] == nome_substring:
            return janela
    return None

def mover_para_monitor_principal(janela):
    # Obter o monitor principal
    monitor_principal = get_monitors()[0]

    # Obter as dimensões do monitor principal
    x, y, largura, altura = monitor_principal.x, monitor_principal.y, monitor_principal.width, monitor_principal.height

    # Mover a janela para o monitor principal
    janela.moveTo(x, y)

    # Maximizar a janela em tela cheia

def encontrar_e_mover_janela_do_tibia(nome_janela):
    janela_tibia = encontrar_janela_com_primeiro_nome(nome_janela)
    if janela_tibia:
        mover_para_monitor_principal(janela_tibia)
        return True
    return False

def encontrar_imagem_sem_regiao(nome_imagem, confianca=0.9):
    position = pyautogui.locateCenterOnScreen(nome_imagem, confidence=confianca)
    return position

# Nome da janela do Tibia
nome_janela_tibia = "Tibia"

# Encontrar e mover a janela do Tibia para o monitor principal
if encontrar_e_mover_janela_do_tibia(nome_janela_tibia): 
    print(f"Janela do Tibia encontrada e movida para o monitor principal.")
else:
    print(f"Janela do Tibia não encontrada.")

# Aguardar um pouco para a janela se mover e maximizar
time.sleep(3)

# Nome da imagem a ser procurada
nome_imagem = 'imgs/hp_mp.png'
