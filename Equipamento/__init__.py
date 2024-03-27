

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
        self.item_Atk = Item("Vazio","Arma")
        self.item_Df = Item("Vazio","Armadura")

        self.ouro = ouro
        
        self.cont_mgk = 5
        self.cont_p = php + pmk
        self.df = df
        self.mgk = mgk
        self.atk = atk
        
class Item():
    def __init__(self,name, tipo, atk =0, mgk =0 ,hp =0, df = 0 ):
        """
                    Criador: PedroXplorer

            Criar itens e gerencia eles

        Args / Parametros:
        name (str): Nome do equipamento
        tipo (str): Tipo do equipamento ("Armadura","Arma")
        atk (int): Dano de Ataque 
        mgk (int): Dano de Mágica 
        df (int): Pontos de Defesa
        hp (int): Pontos de Vida  
        """
        self.name = name
        self.tipo = tipo
        self.hp = hp
        self.atk = atk
        self.mgk = mgk
        self.df = df

    def EquiparItem(self, usuario):
        escolha = 0
        print (f'''\nInformações do equipamento: 
NOME: {self.name}      TIPO:   {self.tipo}
ATK: {self.atk}      MGK: {self.mgk}      DEF: {self.df}       HP: {self.hp} 
------------------------------------------------''')
        if self.tipo == "Arma":
            print(f'''  Atributo      Atual    Equipando    Diferença
        1. Ataque   |  {usuario.atk + usuario.item_Atk.atk}   |    {(usuario.atk - usuario.item_Atk.atk)+ self.atk}      |    {self.atk - usuario.item_Atk.atk}
        2. Mágica   |  {usuario.mgk + usuario.item_Atk.mgk}   |    {(usuario.mgk -  usuario.item_Atk.mgk) + self.mgk}      |    {self.mgk - usuario.item_Atk.mgk}
        3. Defesa   |  {usuario.df + usuario.item_Atk.df}   |    {(usuario.df - usuario.item_Atk.df) + self.df}      |    {self.df - usuario.item_Atk.df}
        4. Vida     |  {usuario.hp + usuario.item_Atk.hp}  |    {(usuario.hp - usuario.item_Atk.hp) + self.hp}     |    {self.hp - usuario.item_Atk.hp}
        ''')
        elif self.tipo == "Armadura":
            print(f'''  Atributo      Atual    Equipando    Diferença
        1. Ataque   |  {usuario.atk + usuario.item_Df.atk}   |    {(usuario.atk - usuario.item_Df.atk)+ self.atk}      |    {self.atk - usuario.item_Df.atk}
        2. Mágica   |  {usuario.mgk + usuario.item_Df.mgk}   |    {(usuario.mgk -  usuario.item_Df.mgk) + self.mgk}      |    {self.mgk - usuario.item_Df.mgk}
        3. Defesa   |  {usuario.df + usuario.item_Df.df}   |    {(usuario.df - usuario.item_Df.df) + self.df}      |    {self.df - usuario.item_Df.df}
        4. Vida     |  {usuario.hp + usuario.item_Df.hp}  |    {(usuario.hp - usuario.item_Df.hp) + self.hp}     |    {self.hp - usuario.item_Df.hp}
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

al = Item('Adaga Envenenada',"Arma",5,3)
ol = Item('Capacete',"Armadura",hp = 12, df= 5)
al.EquiparItem(jogador_principal)
ol.EquiparItem(jogador_principal)

## Valores invertidos -- Arrumar depois é isso ai