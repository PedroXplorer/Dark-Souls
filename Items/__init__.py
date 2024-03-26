
class Caracter():
    def __init__(self, name,hpi, hp, atk, mgk, df, ouro, php = 0, pmk = 0,lv =0, xp =0, m= 0,item =0):
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
        self.item = item
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
        print(f'''  Atributo      Atual    Equipando    Diferença
  1. Ataque   |  {usuario.atk + usuario.item}   |    {usuario.atk + self.atk}      |    {usuario.atk - self.atk}
  2. Mágica   |  {usuario.mgk + usuario.item}   |    {usuario.mgk + self.mgk}      |    {usuario.mgk - self.mgk}
  3. Defesa   |  {usuario.df + usuario.item}   |    {usuario.df + usuario.df}      |    {usuario.df - self.df}
  4. Vida     |  {usuario.hp + usuario.item}  |    {usuario.hp  + usuario.hp}     |    {usuario.hp - self.hp}

        ''')
        escolha = input(f"Você encontrou um item, deseja equipa-lo [S/N]: ")

nome_jogador = input("\nDigite o nome do seu personagem: ")
jogador_principal = Caracter(nome_jogador,100, 100, 20, 20, 10, 0, 2,2)
al = Item('Adaga','Ataque',5,6,3,10)
al.EquiparItem(jogador_principal)

## TEM MUITA COISA ERRADA AKI -- Arrumar depois