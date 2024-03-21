from Objetos import *
from random import randint

# Ordem de organizar Personagem 
# --  name, hpi (Cópia hp), hp, atk, mgk, df, ouro, php = 0 (), pmk = 0,lv =0, xp =0, m= 0

# Ordem de organizar inimigos
# --  name, hp, atk, df,lv,ouro, xp
Rato_Gigante = Inimigo('Rato Gigante', 12, 11,3, 1,5, xp = randint(3,4))
Slime = Inimigo('Slime',15,12,4,1,5, xp = randint(3,6))
Morcego = Inimigo('Morcego',13,11,3,1,5, xp=randint(2,4))
Águia = Inimigo('Águia')
