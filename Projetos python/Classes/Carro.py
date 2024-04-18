class Automóvel:
    def __init__(self = 'Automóvel',marca = '<desconhecida>',velocidade =  '<desconhecida>', preço =  '0.00'):
        self.marca = marca
        self.v = velocidade
        self.p = float(preço)

# Métodos 
    def parcela(self):
        try: 
            print (f'Parcelando até 12x por mês o preço de R${self.p} será necessário R${(self.p / 12):.2f} por mês.\n\n')
        except:
            print (f'Ocorreu um ERRO ao tentar calcular a parcela do veículo.\n\n')

    def mostrarInf(self):
        if self.v == '<desconhecida>':
            return f'\n >> Marca: {self.marca}\n >> Velocidade: {self.v} \n >> Valor estimado: R$ {self.p}'
        else:
            return f'\n >> Marca: {self.marca}\n >> Velocidade: {self.v} km/h \n >> Valor estimado: R$ {self.p}'
    
print ()
car1 = Automóvel('Toyota',250,24000)
print (f'   Carro 1: {car1.mostrarInf()}')
car1.parcela()

car2 = Automóvel('Ford',266,27000)
print (f'   Carro 2: {car2.mostrarInf()}')
car2.parcela()

car3 = Automóvel('Chevrolet',312, 25000)
print (f'   Carro 3: {car3.mostrarInf()}')
car3.parcela()

car4 = Automóvel()
print (f'   Carro 4: {car4.mostrarInf()}')
car4.parcela()
