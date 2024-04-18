
class Caracter:
    def __init__(self,hp,atk,dr,vel):
        self.hp = hp
        self.atk = atk
        self.defe = dr
        self.vel = vel

    def dobro_vel(self):
        self.vel *= 2 

guerreiro = Caracter(160,75, 60,50)
ninja = Caracter(150,75, 50,60)

print (f'Velocidade do Guerreiro: {guerreiro.vel}')
print (f'Velocidade do Mago: {ninja.vel}')

guerreiro.dobro_vel()
print (f'\nVelocidade do Guerreiro: {guerreiro.vel}')
print (f'Velocidade do Mago: {ninja.vel}')

