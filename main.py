"""
Jogo da Velha em Python
"""

def mostrar_tabuleiro(tab):
    for linha in tab:
        print(" | ".join(linha))

tabuleiro = [["1", "2", "3"], 
             ["4", "5", "6"], 
             ["7", "8", "9"]]
jogador_atual = "X"

for rodada in range(9):
    mostrar_tabuleiro(tabuleiro)
    escolha = input(f"Jogador {jogador_atual}, escolha uma posição de (1-9): ")
    pos = int(escolha) - 1
    linha, coluna = pos // 3, pos % 3

    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("Posição já ocupada. Tente outra.")
        continue

    tabuleiro[linha][coluna] = jogador_atual

    if jogador_atual == "O":
        jogador_atual = "X"
    else:
        jogador_atual = "O"