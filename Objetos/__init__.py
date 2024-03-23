from random import randint
import time


class Caracter():
    def __init__(self, name,hpi, hp, atk, mgk, df, ouro, php = 0, pmk = 0,lv =0, xp =0, m= 0):
        """
                    Criador: PedroXplorer

            Criar um novo personagem.

        Args / Parâmetros:
            name (str): O nome do personagem.
            hpi (int): Pontos de vida inicial.
            hp (int): Pontos de vida.
            atk (int): Valor do ataque.
            mgk (int): Valor da magia.
            df (int): Valor da defesa.
            ouro (int): Quantidade de ouro do personagem.
            php (int): Poções de vida.
            pmk (int): Poções de magia.
            lv (int): Nível do personagem.
            xp (int): Pontos de experiência do personagem.
            m (int): Pontos de melhoria para distribuir ao subir de nível.

        """
    
        self.name = name
        self.hp = hp
        self.php = php
        self.pmk = pmk
        self.lv  = lv
        self.xp = xp
        self.hpi = hpi 
        self.m = m
        self.ouro = ouro
        
        self.cont_mgk = 5
        self.cont_p = php + pmk
        self.df = df
        self.mgk = mgk
        self.atk = atk

    def Level_up(self,alvo):
        """
                    Criador: PedroXplorer

            Aumenta o nível do personagem e permite distribuir pontos de atributo.

        Args / Parâmetros:
            alvo (Inimigo): Oponente derrotado.
            self (Caracter): Personagem vitorioso.
        Returns:
            int: 0 se a experiência não for suficiente para subir de nível.
            
        """
        self.m  = self.m + 1
        self.xp = self.xp + alvo.xp
        marca = self.lv * 20
        
        if marca == 0:
            marca = 20

        if self.xp >= marca:
            self.xp = self.xp - marca
            self.lv = self.lv + 1
            df = self.df
            hp = self.hpi
            mgk = self.mgk
            atk = self.atk

            print (f' Parabéns, {self.name} subiu para o level {self.lv}\nEscolha os atributos para aumentar.')
            escolha = 0 
            m = self.m
            while escolha not in ('S','Q'):
                while self.m != 0 or n == 'Q':
                    print ('-' * 30)
                    n = input(str(f'''  Atributo     Up     Atual
  1. Ataque   |  +3  |  {atk}
  2. Mágica   |  +4  |  {mgk}
  3. Defesa   |  +3  |  {df}
  4. Vida     |  +5  |  {hp}
  Pontos: {self.m}
 Escolha a opção (Se não quiser usa-los - Q): '''))
                    print ('-' * 30)
         
                    if n == '1':
                        atk = atk + 3
                        self.m = self.m - 1
                    elif n == '2':
                        mgk = mgk + 4
                        self.m = self.m - 1
                    elif n == '3':
                        df = df + 3
                        self.m = self.m - 1
                    elif n == '4':
                        hp = hp + 5
                        self.m = self.m - 1
                    elif n == 'Q':
                        escolha = 'Q'
                        break
                    else:
                        print ('Opção Inválida. Tente novamente.')
                        print ('-' * 30 + '\n')

                    if self.cont_mgk == 0:
                        self.cont_mgk = self.cont_mgk + 3 
                    if n != 'Q':
                        escolha = input('Deseja confirmar as alterações feitas [S/N]: ')
                        if escolha == 'N':
                            print ('Revertendo alterações..."')
                            df = self.df
                            atk = self.atk
                            mgk = self.mgk 
                            hp = self.hpi
                            self.m = m
                            continue

                        elif escolha == 'S':
                            print ('Confirmando alterações...')
                            self.hpi = hp
                            self.df = df
                            self.atk = atk
                            self.mgk = mgk 
                            self.hp = hp
                            self.m = 0
                            print ('-' * 30)
                            print (f'''    Atributo      Atual
        1. Ataque   |  {self.atk}
        2. Mágica   |  {self.mgk}
        3. Defesa   |  {self.df}
        4. Vida     |  {self.hp}''')
                            print ('-' * 30 + '\n')
                            break
                        else:
                            print ('Opção Inválida. Tente novamente.')
                            print ('-' * 30 + '\n')
                            continue
                    else:
                        break
        if self.xp < marca:
            return 0
        else:
            return 0

    def atacar(self, alvo):
        """
                    Criador: PedroXplorer

            Realiza um ataque ao alvo.

        Args / Parâmetros:
            alvo (Inimigo): Oponente que será atacado.
            self (Caracter): Personagem que está atacado.
        Returns:
            int: O dano causado.
        """
        dano = self.atk - alvo.df
        if dano <= 0 :
            dano = 0
        else: 
            alvo.hp = alvo.hp - dano
            
        if alvo.hp <= 0:
            alvo.hp = 0
        return dano

    def usar_magia(self, alvo):
        """
                    Criador: PedroXplorer
            Usa magia contra o alvo.

        Args / Parâmetros:
            alvo (Inimigo): Oponente que será atacado.
            self (Caracter): Personagem que está atacado.
        Returns:
            int: O dano causado.
        """
        if self.cont_mgk > 0:
            alvo.hp = alvo.hp - self.mgk
            if alvo.hp <= 0:
                alvo.hp = 0      
            return self.mgk 
        else:
            return
    
    def usar_pocao(self, tipo):
        """
                    Criador: PedroXplorer
            Usa uma poção. Para recuperar a vida ou pontos de magia do personagem.

        Args:
            tipo (str): Tipo de poção a ser usada ('vida' ou 'magia').

        Returns:
            None
        """
        if self.cont_p > 0:
            if tipo == 'vida' and self.php > 0:
                cura = randint(10,20)
                self.hp = self.hp + cura
                self.cont_p = self.cont_p - 1
                print (f'{self.name} usou uma poção de vida, recuperando {cura} de hp.')
            
            elif tipo == 'magia' and self.pmk > 0:
                recup_magia = randint(5,10)
                self.cont_mgk = self.cont_mgk + recup_magia
                self.cont_p = self.cont_p - 1
                print (f'{self.name} usou uma poção de magia, recuperando {recup_magia} de magia.')
    
            else:
                print ('Sem poções suficientes.')
                print ('-' * 30 + '\n')
        else:
            print ('Sem poções suficientes.')
            print ('-' * 30 + '\n')

class Inimigo:
    def __init__(self, name, hp, atk, df,lv,ouro, xp = 0):
        """
                    Criador: PedroXplorer
        Cria um novo inimigo.

        Args / Parâmetros:
            name (str): O nome do inimigo.
            hp (int): Pontos de vida do inimigo.
            atk (int): Valor do ataque do inimigo.
            df (int): Valor da defesa do inimigo.
            lv (int): Nível do inimigo.
            ouro (int): Quantidade de ouro que o inimigo pode largar.
            xp (int): Pontos de experiência que o inimigo concede ao ser derrotado (padrão: 0; ou seja é opcional).
        """
        self.name = name
        self.ouro = ouro
        self.hp = hp
        self.atk = atk
        self.df = df
        self.lv = lv
        self.xp = xp
    
    def atacar(self, jogador):
        """
                    Criador: PedroXplorer
        Realiza um ataque ao jogador.

        Args / Parâmetros:
            jogador (Caracter): O jogador que será atacado.
            self (Inimigo): O inimigo que está atacando.

        Returns:
            int: O dano causado ao jogador.
        """
        dano = self.atk - jogador.df
        if dano <= 0 :
            dano = 0
        else: 
            jogador.hp = jogador.hp - dano
            return dano
        
def exibir_status(personagem, inimigo):
    """
                    Criador: PedroXplorer
      Exibe o status atual do jogador e do inimigo durante a batalha.

        Args / Parâmetros:
            personagem (Caracter): O jogador.
            inimigo (Inimigo): O inimigo.

        Returns:
            None
    """
    print ('\n' +'='*30)
    print(f'{personagem.name.upper():^30}')
    print('='*30)
    print(f'Vida: {personagem.hp} | Magia: {personagem.cont_mgk} | Poções: {personagem.cont_p}')
    print("\n" + "=" * 30)
    print(f"{inimigo.name.upper():^30}")
    print("=" * 30)
    print(f"Vida: {inimigo.hp} | Ataque: {inimigo.atk} | Defesa: {inimigo.df}")
    print("=" * 30)

def batalha(jogador, inimigo):
    """
                    Criador: PedroXplorer

            Simula uma batalha entre o jogador e um inimigo. 
            Usa a maioria das outras funções nesse código.

        Args / Parâmetros:
            jogador (Caracter): O jogador.
            inimigo (Inimigo): O inimigo.
        Funções usadas:
            atacar: Esta função é chamada quando o jogador decide atacar o inimigo.
            usar_magia: Esta função é chamada quando o jogador decide usar magia contra o inimigo.
            exibir_status: Esta função é chamada para exibir o status atual do jogador e do inimigo durante a batalha.
            time.sleep também é usada para adicionar um atraso de 1 segundo entre cada ação durante a batalha.

        Returns:
            None
    """
    print (f'{jogador.name} vs {inimigo.name}')

    while jogador.hp > 0 and inimigo.hp > 0:
        print ('\nOpções:')
        print("1. Atacar")
        print("2. Usar Magia")
        print("3. Usar Item")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            dano_jogador = jogador.atacar(inimigo)
            print(f"{jogador.name} atacou {inimigo.name} causando {dano_jogador} de dano.")
        elif escolha == "2":
            dano_magia = jogador.usar_magia(inimigo)
            if jogador.cont_mgk <= 0:
                print("Sem pontos de magia suficientes. Tente novamente")
                print ('-' * 30)
                continue
            if dano_magia > 0:
                print(f"{jogador.name} usou magia em {inimigo.name} causando {dano_magia} de dano.")

            jogador.cont_mgk = jogador.cont_mgk - 1
        elif escolha == "3":
            print("\nOpções de Item:")
            print(f"a. Poção de Vida  -- {jogador.php}")
            print(f"b. Poção de Magia -- {jogador.pmk}")
            tipo_item = input("Escolha um item: ")
            if tipo_item == "a":
                jogador.usar_pocao("vida")
                if jogador.php == 0:
                    continue
                else:
                    jogador.php -= 1

            elif tipo_item == "b":
                jogador.usar_pocao("magia")
                if jogador.pmk == 0:
                    continue
                else:
                    jogador.pmk -= 1

            else:
                print("Opção inválida. Tente novamente.")
                print ('-' * 30 + '\n')
                continue
        else:
            print("Opção inválida. Tente novamente.")
            print ('-' * 30 + '\n')
            continue


        dano_inimigo = inimigo.atacar(jogador)
        print(f"{inimigo.name} atacou {jogador.name} causando {dano_inimigo} de dano.")

        exibir_status(jogador, inimigo)

        time.sleep(1)

    if jogador.hp <= 0:
        print(f"{jogador.name} foi derrotado. Game Over.")
    else:
        print(f"{inimigo.name} foi derrotado. Você venceu!")
        jogador.Level_up(inimigo)

