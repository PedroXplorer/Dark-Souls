
# As classes devem ser modeladas nas situações de uso, ou seja, de forma dinâmica
## Computador 
# Marca, Ram, Placa de vídeo


class Pc:
    def __init__(self = 'Personal Communications Services',marca = '<desconhecida>',RAM = '<desconhecida>',GPU =  '<desconhecida>'):
        self.marca = marca
        self.RAM = RAM
        self.GPU = GPU


# Métodos 
    def Ligar(self):
        print (f'Estou ligando.')

    def desligar(self):
        print (f'Estou desligando...\n')
        quit()   
    
    def mostrarInf(self):
        if '<desconhecida>' in  [self.marca, self.RAM, self.GPU]:
            return f'\n >> Marca: {self.marca}\n >> Memória Ram: {self.RAM}\n >> Placa de vídeo (GPU): {self.GPU}\nFavor preencher dados faltantes...'
        else:
            return f'\n >> Marca: {self.marca}\n >> Memória Ram: {self.RAM}\n >> Placa de vídeo (GPU): {self.GPU}\n'
    

pc1 = Pc('dell','16gb','NVIDIA')
pc2 = Pc('Apple','8gb','AMD')
pc3 = Pc('Sony','10gb','ASUS')
pc4 = Pc()


pc1.Ligar()

print (f'\n   Pc1: {pc1.mostrarInf()} ')
print (f'\n   Pc2: {pc2.mostrarInf()} ')
print (f'\n   Pc3: {pc3.mostrarInf()} ')
print (f'\n   Pc4: {pc4.mostrarInf()} ')

print ()
pc1.desligar()
