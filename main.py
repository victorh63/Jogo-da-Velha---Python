"""
Jogo da Velha em Python
"""

def mostrar_tabuleiro(tab):
    for linha in tab:
        print(" | ".join(linha))

tabuleiro = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

mostrar_tabuleiro(tabuleiro)