from Objetos import *

nome_jogador = input("\nDigite o nome do seu personagem: ")
jogador_principal = Caracter(nome_jogador,100, 100, 20, 20, 10, 0, 2,2)

inimigo_1 = Inimigo("Inimigo 1", 50, 15, 5, 1,5, 10)
inimigo_2 = Inimigo("Inimigo 2", 60, 18, 8, 1,5, 10)
inimigo_3 = Inimigo("Inimigo 3", 70, 22, 10,1,5, 10)

print("\nBem-vindo ao Jogo de Aventura!")
print(f"{jogador_principal.name}, prepare-se para a batalha!\n")

batalha(jogador_principal, inimigo_1)
batalha(jogador_principal, inimigo_2)
batalha(jogador_principal, inimigo_3)
print('')
print('XP total obtido: ',jogador_principal.xp)

Rato_Gigante = Inimigo('Rato Gigante', 12, 11,3, 1,5, xp = randint(3,4))
Slime = Inimigo('Slime',15,12,4,1,5, xp = randint(3,6))
Morcego = Inimigo('Morcego',13,11,3,1,5, xp=randint(2,4))
Águia = Inimigo('Águia')
