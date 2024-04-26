import os
import random

largura = 20
altura = 10

def criar_mapa(largura, altura, porta_pos):
    mapa = []
    for i in range(altura):
        linha = []
        for j in range(largura):
            if (i, j) == porta_pos:
                linha.append("|")
            elif random.random() < 0.2:
                linha.append("#")
            else:
                linha.append(" ")
        mapa.append(linha)
    return mapa

def exibir_mapa(mapa):
    for linha in mapa:
        print("".join(linha))

def limpar_terminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def verificar_movimento_possivel(mapa, posicao_jogador):
    movimentos_possiveis = []
    altura = len(mapa)
    largura = len(mapa[0])
    
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        novo_x = posicao_jogador[0] + dx
        novo_y = posicao_jogador[1] + dy
        if 0 <= novo_x < altura and 0 <= novo_y < largura and mapa[novo_x][novo_y] != "#":
            movimentos_possiveis.append((novo_x, novo_y))
    
    return movimentos_possiveis

def criar_chefao(mapa, altura, largura):
        x = random.randint(0, altura - 1)
        y = random.randint(0, largura - 1)
        if mapa[x][y] == " ":
            mapa[x][y] = "C"  # Representação do chefão
            return (x, y)

def main():
    porta_pos = (5, 5)
    mapa = criar_mapa(largura, altura, porta_pos)
    posicao_jogador = [altura - 1, largura // 2]
    posicao_chefao = None

    while True:
        limpar_terminal()
        mapa[posicao_jogador[0]][posicao_jogador[1]] = "J"

        # Verifica se é hora de criar um chefão
        if posicao_chefao is None:
            posicao_chefao = criar_chefao(mapa, altura, largura)
            print("Um chefão apareceu! Derrote-o para continuar.")

        exibir_mapa(mapa)

        direcao = input("Digite w (cima), s (baixo), a (esquerda) ou d (direita), ou q para sair: ").lower()
        if direcao == "q":
            print("Você saiu do jogo.")
            break

        movimentos_possiveis = verificar_movimento_possivel(mapa, posicao_jogador)

        if not movimentos_possiveis:
            print("Você está bloqueado! Escolha outra direção.")
            continue

        if direcao == "w":
            novo_x, novo_y = posicao_jogador[0] - 1, posicao_jogador[1]
        elif direcao == "s":
            novo_x, novo_y = posicao_jogador[0] + 1, posicao_jogador[1]
        elif direcao == "a":
            novo_x, novo_y = posicao_jogador[0], posicao_jogador[1] - 1
        elif direcao == "d":
            novo_x, novo_y = posicao_jogador[0], posicao_jogador[1] + 1
        elif direcao == "":
            novo_x, novo_y = posicao_jogador[0], posicao_jogador[0] 
        else:
            continue

        
        for i in range(altura):
            for j in range(largura):
                if mapa[i][j] == "J":
                    mapa[i][j] = " "

        if (novo_x, novo_y) in movimentos_possiveis:
            posicao_jogador = [novo_x, novo_y]

        if tuple(posicao_jogador) == porta_pos:
            print("Você passou pela porta!")
            input("Pressione Enter para continuar para o próximo mapa...")
            porta_pos = (2, 8)
            mapa = criar_mapa(largura, altura, porta_pos)
            posicao_jogador = [altura - 1, largura // 2]
            posicao_chefao = None  # Reseta a posição do chefão para o próximo mapa

        # Movimento do chefão se ele estiver presente no mapa
        if posicao_chefao:
            movimentos_possiveis_chefao = verificar_movimento_possivel(mapa, posicao_chefao)
            if movimentos_possiveis_chefao:
                novo_pos_chefao = random.choice(movimentos_possiveis_chefao)
                mapa[posicao_chefao[0]][posicao_chefao[1]] = " "  # Limpa a posição anterior do chefão
                posicao_chefao = novo_pos_chefao
                mapa[posicao_chefao[0]][posicao_chefao[1]] = "C"  # Define a nova posição do chefão

main()