# Ordem de organizar Personagem 
# --  self, name,hpi, hp, atk, mgk, df, ouro, php = 0, pmk = 0,lv =0, xp =0, m= 0

# Ordem de organizar inimigos
# --  name, hp, atk, df,lv,ouro, xp

# Código principal do programa, utiliza funções da pasta 'Objetos'

from Objetos import *
from Equipamento import *

nome_jogador = input("\nDigite o nome do seu personagem: ")
jogador_principal = Caracter(nome_jogador,100, 100, 20, 20, 10, 0, 2,2)

inimigo_1 = Inimigo("Inimigo 1", 50, 15, 5, 1,5, 60)
inimigo_2 = Inimigo("Inimigo 2", 60, 18, 8, 1,5, 30)
inimigo_3 = Inimigo("Inimigo 3", 70, 22, 10,1,5, 30)

print("\nBem-vindo ao Jogo de Aventura!")
print(f"{jogador_principal.name}, prepare-se para a batalha!\n")

print (jogador_principal.item_Atk.name,jogador_principal.item_Atk.tipo,jogador_principal.item_Atk.atk,jogador_principal.item_Atk.df,jogador_principal.item_Atk.mgk,jogador_principal.item_Atk.hp)
print (jogador_principal.item_Df.name,jogador_principal.item_Df.tipo,jogador_principal.item_Df.atk,jogador_principal.item_Df.df,jogador_principal.item_Df.mgk,jogador_principal.item_Df.hp)

al = Item('Adaga Envenenada',"Arma",5,3)
ol = Item('Capacete',"Armadura",hp = 12, df= 5)
al.EquiparItem(jogador_principal)
ol.EquiparItem(jogador_principal)

print (jogador_principal.item_Atk.name,jogador_principal.item_Atk.tipo,jogador_principal.item_Atk.atk,jogador_principal.item_Atk.df,jogador_principal.item_Atk.mgk,jogador_principal.item_Atk.hp)
print (jogador_principal.item_Df.name,jogador_principal.item_Df.tipo,jogador_principal.item_Df.atk,jogador_principal.item_Df.df,jogador_principal.item_Df.mgk,jogador_principal.item_Df.hp)
print(jogador_principal.atk,jogador_principal.df,jogador_principal.hp,jogador_principal.mgk)

batalha(jogador_principal, inimigo_1)
batalha(jogador_principal, inimigo_2)
batalha(jogador_principal, inimigo_3)
print('')
print('XP total obtido: ',jogador_principal.xp)