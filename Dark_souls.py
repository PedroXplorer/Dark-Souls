from Objetos import *

nome_jogador = input("Digite o nome do seu personagem: ")
jogador_principal = Caracter(nome_jogador,100, 100, 20, 20, 10, 2,2)

inimigo_1 = Inimigo("Inimigo 1", 50, 15, 5, 10)
inimigo_2 = Inimigo("Inimigo 2", 60, 18, 8, 10)
inimigo_3 = Inimigo("Inimigo 3", 70, 22, 10, 10)

print("\nBem-vindo ao Jogo de Aventura!")
print(f"{jogador_principal.name}, prepare-se para a batalha!\n")

batalha(jogador_principal, inimigo_1)
batalha(jogador_principal, inimigo_2)
batalha(jogador_principal, inimigo_3)