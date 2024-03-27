

class Caracter():
    def __init__(self, name,hpi, hp, atk, mgk, df, ouro, php = 0, pmk = 0,lv =0, xp =0, m= 0,item_Atk =0,item_Df = 0):
        """
                    Criador: PedroXplorer

            Criar um novo personagem.

        Args / Parametros:
            name (str): O nome do personagem.
            hpi (int): Pontos de vida inicial.
            hp (int): Pontos de vida.
            atk (int): Valor do ataque.
            mgk (int): Valor da magia.
            df (int): Valor da defesa.
            ouro (int): Quantidade de ouro do personagem.
            php (int): Pocoes de vida.
            pmk (int): Pocoes de magia.
            lv (int): Nivel do personagem.
            xp (int): Pontos de experiencia do personagem.
            m (int): Pontos de melhoria para distribuir ao subir de nivel.

        """
    
        self.name = name
        self.hp = hp
        self.php = php
        self.pmk = pmk
        self.lv  = lv
        self.xp = xp
        self.hpi = hpi 
        self.m = m
        self.item_Atk = Item("Nome Atk ","Arma")
        self.item_Df = Item("Nome Df ","Armadura")

        self.ouro = ouro
        
        self.cont_mgk = 5
        self.cont_p = php + pmk
        self.df = df
        self.mgk = mgk
        self.atk = atk
        
class Item():
    def __init__(self,name, tipo, hp =0, atk =0, mgk =0 , df = 0 ):
        self.name = name
        self.tipo = tipo
        self.hp = hp
        self.atk = atk
        self.mgk = mgk
        self.df = df

    def EquiparItem(self, usuario):
        escolha = 0
        if self.tipo == "Arma":
                print(f'''  Atributo      Atual    Equipando    Diferença
    1. Ataque   |  {usuario.atk + usuario.item_Atk.atk}   |    {(usuario.atk - usuario.item_Atk.atk)+ self.atk}      |    {self.atk - usuario.item_Atk.atk}
    2. Mágica   |  {usuario.mgk + usuario.item_Atk.mgk}   |    {(usuario.mgk -  usuario.item_Atk.mgk) + self.mgk}      |    {self.mgk - usuario.item_Atk.mgk}
            ''')
        elif self.tipo == "Armadura":
                print(f'''  Atributo      Atual    Equipando    Diferença
    1. Defesa   |  {usuario.df + usuario.item_Df.df}   |    {(usuario.df - usuario.item_Df.df) + self.df}      |    {self.df - usuario.item_Df.df}
    2. Vida     |  {usuario.hp + usuario.item_Df.hp}  |    {(usuario.hp - usuario.item_Df.hp) + self.hp}     |    {self.hp - usuario.item_Df.hp}
    ''')
                
        while escolha != "S" or escolha != 'N':
            escolha = input(str(f"Você encontrou um item, deseja equipa-lo [S/N]: "))
            if escolha == 'S' and self.tipo == "Arma":
                print(f"{usuario.name} trocou o equipamento {usuario.item_Atk.name} pelo equipamento {self.name}\n")
                usuario.item_Atk = self
                break

            elif escolha == 'S' and self.tipo == "Armadura":
                print(f"{usuario.name} trocou o equipamento {usuario.item_Df.name} pelo equipamento {self.name}\n")
                usuario.item_Df = self
                break

            elif escolha == 'N':
                print(f'{usuario.name} descartou o equipamento {self.name}... \n')
                break

            else :
                print ('Escolha somente [S/N], tente novamente.\n\n')


nome_jogador = input("\nDigite o nome do seu personagem: ")
jogador_principal = Caracter(nome_jogador,100, 100, 20, 20, 10, 0, 2,2)
print (f'\nEquipamento Ataque do Usuário: {jogador_principal.item_Atk.name}')
print (f'Equipameto Defesa Usuário: {jogador_principal.item_Df.name} \n')
al = Item('Adaga',"Arma",5,6)
ol = Item('Capacete',"Armadura",mgk =3, df =10)
al.EquiparItem(jogador_principal)
ol.EquiparItem(jogador_principal)

print (f'\nEquipamento Ataque do Usuário: {jogador_principal.item_Atk.name}')
print (f'Equipameto Defesa Usuário: {jogador_principal.item_Df.name} \n')
## Valores invertidos -- Arrumar depois é isso ai