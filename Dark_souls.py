# Ordem de organizar Personagem 
# --  self, name,hpi, hp, atk, mgk, df, ouro, php = 0, pmk = 0,lv =0, xp =0, m= 0

# Ordem de organizar inimigos
# --   name, hp, atk, df,lv,ouro, xp = 0

#Ordem de organizar itens
# -- name, tipo, atk =0, mgk =0 ,hp =0, df = 0 

# Código principal do programa, utiliza funções da pasta 'Objetos' e 'Equipamento'

# -----------------------------------------------------------------------------------------

import os
from time import sleep
from random import randint
from Objetos import *
from Equipamento import *
from Sistema_de_Save import *

arq = 'save.txt'
parte = -1

os.system("cls")
time.sleep(1.75)
print ('''
                                         ╔════════════════╗
             LOADING.                    ┃ ▁▂      10%    |                 
                                         ╚════════════════╝
 ''',flush=True)
time.sleep(1.75)
os.system("cls")
print ('''
                                         ╔════════════════╗
             LOADING..                   ┃ ▁▂▃▅    50%    |                 
                                         ╚════════════════╝
 ''',flush=True)
time.sleep(1.75)
os.system("cls")
print ('''
                                         ╔════════════════╗
             LOADING...                  ┃ ▁▂▃▅▆   80%    |                 
                                         ╚════════════════╝
 ''',flush=True)
time.sleep(1.75)
os.system("cls")
print ('''
                                         ╔════════════════╗
             LOADING.                    ┃ ▁▂▃▅▆▇  100%   |                 
                                         ╚════════════════╝
 ''',flush=True)

time.sleep(1.75)
os.system("cls")


# Menu -----

menu = (''' -------------------------------------------------------------------------------------------------------------------------

             █▄██▄█                  █▄██▄█                  █▄██▄█                  █▄██▄█                  █▄██
    █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄█▐█ ╔═════════════════════╗ ██▌█▄█▄█▄█▄██▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄█▐█┼█
    ███┼█████▐████▌█████┼██████┼█████▐█ <      Retro Quest    > ██▌█████┼██████┼█████▐████▌█████┼██████┼█████▐███
    █████████▐████▌██████████████████▐█ ╚═════════════════════╝ ██▌██████████████████▐████▌██████████████████▐███
    █████████▐████▌██████████████████▐████▌██████████████████▐████▌██████████████████▐████▌██████████████████▐███
       
                                Por:   Pedro Henrique Alves Martins 
--------------------------------------------------------------------------------------------------------------------------
    >> (c) Pedro Henrique Alves Martins .Todos os direitos reservados.
            
    \033[0;0mMinhas redes sociais:
        Instagem: \033[94mhttps://www.instagram.com/pdrhnrqalvesmartins/\033[0;0m
        Steam (Jogos): \033[94mhttps://steamcommunity.com/profiles/76561199114894915\033[0;0m
    Meus GitHubs:
        PedroXplorer: \033[94mhttps://github.com/PedroXplorer/PedroXplorer\033[0;0m  
        Germinare: \033[94mhttps://github.com/Pedro-GerminareT3ch\033[0;0m
    Meu site: \033[94mhttps://8049170068179271.carrd.co/\033[0;0m

>> Recomendável ver as informações sobre o jogo antes de começar a jogar.

\033[93m \033[1m        -- [S] -- \033[0;0m   Começar o jogo
              
\033[93m \033[1m        -- [R] -- \033[0;0m   Gerenciamento de Saves

\033[93m \033[1m        -- [M] -- \033[0;0m   Mostrar Créditos

\033[93m \033[1m        -- [L] -- \033[0;0m   Linguagem

\033[93m \033[1m        -- [I] -- \033[0;0m   Informações sobre o jogo

\033[93m \033[1m        -- [Q] -- \033[0;0m   Fechar o jogo
''')

os.system('cls')
print (menu)

e = str(input(">> Sua opção: \033[93m\033[1m")) 
print("\033[0;0m")

e = e.strip()
while True:
##  Sair
    if e in ("Q","q"):
        print("Fechando o programa...")
        time.sleep(1.75)
        print ("")
        print ("")
        quit ()

## Mostrar Saves
    if e in ("R","r"):
        time.sleep(1.75)
        os.system('cls')
        print("""
        >> O Sistema de saves funciona criando um arquivo.txt (saves.txt) e colocando as informações de que parte do jogo você parou, ainda está em andamento. 
        >> As informações do save serve para guardar o seu progresso, para resetar os seus saves, apague o arquivo ou as suas informações.
        >> Se você for alterar alguma informação dentro dele seu save pode corromper, então tome cuidado.
""")

        if arquivoExiste(arq):
            print(">> Arquivo encontrado com sucesso!")
        else:
            print (f'>> Arquivo {arq} não encontrado')
            criarArquivo(arq)
            print (f'\n>> Arquivo {arq} criado com sucesso!')

        while True:
            lst = ['Ver todos os saves','Cadastrar novo save','Deletar um save','Selecionar save','Sair do sistema']
            print ()
            lin('SISTEMA DE SAVE')
            l = 0
            k = len(lst)
            for c in lst:
                l = l + 1 
                if l == k:
                    print (f'[{l}] -  {c}')
                else:
                    print (f'[{l}] -  {c}')
            try:
                scl = (input("Sua Opção: "))

            except:
                print ()
                lin('Saindo do sistema... Até logo!')
                print ()
                quit()

## Opções de save
            else:
                while scl != '1' and scl != '2' and scl != '3' and scl != '4' and scl != '5':
                    print("\033[91mERRO! Digite uma opção válida.\033[0;0m")

                    try:
                        scl = (input("Sua Opção: "))
                    except:
                        print ()
                        lin('Saindo do sistema... Até logo!')
                        print ()
                        quit()

                if scl == "1":
                    lerArquivo(arq)

                elif scl == "2":
                    with open('save.txt', 'r') as file:
                        lines = file.read().splitlines()
                        limit = len(lines)
                        if limit == 3:
                            print("\033[91mERRO! Limite de saves alcançado, delete um save e substitua por um novo.\033[0;0m")
                            continue
                    
                    lin('NOVO SAVE')
                    nome = input("Nome: ")
                    while nome == "" or nome == '':
                        print("\033[91mERRO! Digite algum nome.\033[0;0m")
                        nome = input("Nome: ")

                    cap = input("Capítulo: ")
                    while True:
                        while not cap.isnumeric():
                            print("\033[91mERRO! Digite um capítulo válido, existem 12 capítulos. \033[0;0m")
                            cap = input("Capítulo: ")
                        while int(cap) <= -1 or int(cap) >= 13:
                            print("\033[91mERRO! Digite um capítulo válido, existem 12 capítulos. \033[0;0m")
                            cap = input("Capítulo: ")
                        cap = int(cap)
                        nome = nome.upper()
                        cadastrar(arq,nome,cap)
                        break
                elif scl == "3":
                    print ()
                    lin('DELETAR SAVE')
                    print ()
                    linha_a_deletar = int(input("Digite o número do save que deseja deletar: "))
                    deletar(arq, linha_a_deletar)
                    print (f"Save {linha_a_deletar} foi deletado com sucesso")
                
                elif scl == "4":
                    print ()
                    lin('Escolher save')
                    print ()
                    lerArquivo(arq)
                    linha_desejada = int(input("Digite o número do save desejado: ")) 
                    nome_save, cap_save = ler_arquivo_e_obter_dados(arq, linha_desejada)
                    if nome_save is not None and cap_save is not None:
                        print(f"Nome: {nome_save}")
                        print(f"Capítulo: {cap_save}")

                        
                elif scl == "5":
                    print ()
                    lin('Saindo do sistema... Até logo!')
                    print ()
                    break
                
        str(input("     [ Pressione ENTER ]"))
        time.sleep(1.75)
        os.system('cls')
        print (menu)
        e = str(input(">> Sua opção: \033[93m\033[1m")) 
        print("\033[0;0m")



## Começar o jogo  
    elif e in  ("S","s"):
        if arquivoExiste(arq):
            print(">> Arquivo encontrado com sucesso!")
        else:
            print (f'>> Arquivo {arq} não encontrado')
            criarArquivo(arq)
            print (f'\n>> Arquivo {arq} criado com sucesso!')

        with open('save.txt', 'r') as file:
            lines = file.read().splitlines()
            limit = len(lines)
            if limit == 3:
                print("\033[91mERRO! Limite de saves alcançado, delete um save e substitua por um novo.\033[0;0m\n")
                str(input("     [ Pressione ENTER ]"))
                time.sleep(1.75)
                os.system('cls')
                print (menu)
                e = str(input(">> Sua opção: \033[93m\033[1m")) 
                print("\033[0;0m")
            else:
                time.sleep(1.75)
                os.system('cls') 
                print ("")
                break
        
## Mostrar Créditos
    elif e in  ("M","m"):
        time.sleep(1.75)
        os.system('cls')
        print ("")
        print ("""               Criador: Pedro Henrique 
               Desenvolvedor: Pedro Henrique
               Sistema de Batalha
               Sistema de Personagem: Pedro Henrique
               Sistema de Inimigo: Pedro Henrique
               Sistema de Level_up: Pedro Henrique
               Gerenciamento de Save: Pedro Henrique
               Sistema de Equipamento: Pedro Henrique
               Desing Gráfico: Pedro Henrique
               História do Jogo: ChatGPT
               """)
        print ("")
        str(input("     [ Pressione ENTER ]"))
        print ("")
        time.sleep(1.75)
        os.system('cls')
        print (menu)
        e = str(input(">> Sua opção:\033[93m\033[1m ")) 
        print("\033[0;0m")



## Informações do jogo
    elif e in  ("I","i"):
        time.sleep(1.75)
        os.system('cls')
        print ('''
 
        Funcionamento do jogo:       
               
               >> O jogo é baseado em MUDs (Multi-User-Dungeon) que  é um sugênero de RPG eletrônico multijogador, que normalmente é executado em um sistema online BBS ou em um servidor na Internet. Aviso, o jogo não é online.

               >> O jogo normalmente te dará informações sobre algum acontecimento e você indicara como o seu avatar vai reagir ao ocorrido, dependendo da forma que você agir com os personagens e suas ações é possível obter um final diferente, portanto, tome cuidado com suas escolhas feitas ao longo dessa aventura.

               >> Use apenas as primeiras letras das escolhas para se referir a elas, Exemplo.

               Você quer ir verificar o que é ou deseja voltar a dormir? [verificar / dormir]
                  para verificar o barulho: v
                  para voltar a dormir: d
            
        Instruções:
                     
    \033[1m           S\033[0;0m = Seguir para trás (Sul)
    \033[1m           L\033[0;0m = Seguir para direita (Leste)
    \033[1m           O\033[0;0m = Seguir para esquerda (Oeste)           

    \033[1m           b\033[0;0m = Voltar
    \033[1m          \F\033[0;0m = Olhar o iventário  
    \033[1m          \S\033[0;0m = Salvar o jogo
    \033[1m          \M\033[0;0m = Voltar para o menu       

               

''')
        str(input("     [ Pressione ENTER ]"))
        time.sleep(1.75)
        os.system('cls')
        print (menu)
        e = str(input(">> Sua opção: \033[93m\033[1m")) 
        print("\033[0;0m")



## Linguagem
    elif e in ("L","l"):
        time.sleep(1.75)
        os.system('cls')
        print ('''
        
        [1] Português
        [2] Inglês (em breve)

''')
        str(input("   [ Pressione ENTER ]"))
        os.system('cls')
        print (menu)
        e = str(input(">> Sua opção: \033[93m\033[1m")) 
        print("\033[0;0m")



    else:
        print ()
        print (" Insira uma opção válida... ")
        time.sleep(1)
        os.system('cls')
        print (menu)
        e = str(input(">> Sua opção: \033[93m\033[1m")) 
        print("\033[0;0m")


# ----------------------------------------------------------------------------------------

import time
        

nome_jogador = input("\nDigite o nome do seu personagem: ")
jogador_principal = Caracter(nome_jogador,35, 35, 8, 10, 8, 0, 2,2)


while True:
    nome_save, cap_save = ler_arquivo_e_obter_dados(arq, 1)
    if nome_save == None and cap_save ==  None:
        cadastrar(arq,nome_jogador.upper(),0,nome_jogador)
        break
    nome_save, cap_save = ler_arquivo_e_obter_dados(arq, 2)
    if nome_save == None and cap_save ==  None:
        cadastrar(arq,nome_jogador.upper(),0,nome_jogador)
        break
    nome_save, cap_save = ler_arquivo_e_obter_dados(arq, 3)
    if nome_save == None and cap_save ==  None:
        cadastrar(arq,nome_jogador.upper(),0,nome_jogador)
        break

def introducao():
    parte = 0
    print("Nos Reinos Esquecidos, um continente repleto de magia, criaturas misteriosas e perigos inimagináveis, uma antiga profecia ressurge.")
    time.sleep(2)
    print("Diz-se que há séculos atrás, quatro relicários sagrados foram criados para proteger o mundo da escuridão.")
    time.sleep(2)
    print("Porém, eles foram perdidos ao longo do tempo e agora ameaçam cair nas mãos erradas.")
    time.sleep(2)
    print("Aventureiros de todo o continente são convocados para encontrar os relicários e salvar os Reinos Esquecidos da destruição iminente.")
    time.sleep(2)

def capitulo1():
    parte =1
    print("\nCapítulo 1: O Despertar das Profecias")
    time.sleep(2)
    print(f"{jogador_principal.name} começa em uma pequena vila, onde coisas estranhas começam a acontecer.")
    time.sleep(2)
    print(f"Uma série de eventos misteriosos, como desaparecimentos inexplicáveis e o surgimento de criaturas sombrias, leva {jogador_principal.name} a pensar que algo está ameaçando a paz nos Reinos Esquecidos.")
    time.sleep(2)
    print("Você foi recrutado(a) por um sábio ancião que revela a profecia dos Relicários Perdidos e os encarrega de encontrar e proteger esses artefatos antigos.")
    time.sleep(2)

def capitulo2():
    parte =2
    print("\nCapítulo 2: A Busca pelos Relicários")
    time.sleep(2)
    print("Você embarca em uma jornada épica através de florestas assombradas, montanhas perigosas e cidades corrompidas, enfrentando inúmeros desafios pelo caminho.")
    time.sleep(2)
    print("Ao andar por uma esquina você é atacado(a)")
    batalha(jogador_principal,Slime) # Ladrão 1
    batalha(jogador_principal,Slime) #Ladrão 2
    time.sleep(2)

def capitulo3():
    parte =3
    print("\nCapítulo 3: Revelações e Traições")
    time.sleep(2)
    print(f"Enquanto {jogador_principal.name} se aproximam de encontrar o primeiro Relicário, eles descobrem segredos sombrios sobre a história dos Reinos Esquecidos e aqueles que governam sobre eles.")
    time.sleep(2)
    print("Traições dentro do próprio grupo e alianças inesperadas desafiam sua lealdade e determinação.")
    time.sleep(2)

def capitulo4():
    parte = 4
    print("\nCapítulo 4: O Confronto Final")
    time.sleep(2)
    print("Após superar todos os obstáculos, os jogadores finalmente localizam os quatro Relicários.")
    time.sleep(2)
    print("No entanto, eles descobrem que um antigo inimigo está tramando para usar os artefatos para mergulhar os Reinos Esquecidos na escuridão eterna.")
    time.sleep(2)
    print("Uma batalha épica se desenrola, com o destino dos Reinos pendendo na balança.")

def escolha_sim_ou_nao(pergunta):
    while True:
        resposta = input(pergunta + " (sim/não): ").lower()
        if resposta == "sim":
            return True
        elif resposta == "não":
            return False
        else:
            print("Por favor, responda com 'sim' ou 'não'.")

def final_feliz():
    print("\nParabéns! Os heróis triunfaram sobre o mal e restauraram a paz nos Reinos Esquecidos.")
    time.sleep(2)
    print("Os artefatos são selados novamente, desta vez em um lugar seguro, para evitar que caiam nas mãos erradas novamente.")
    time.sleep(2)
    print("Os heróis são celebrados como lendas e o continente se prepara para uma nova era de prosperidade e harmonia.")

def final_tragico():
    print("\nInfelizmente, os heróis foram derrotados pelo mal e os Reinos Esquecidos caíram na escuridão.")
    time.sleep(2)
    print("A esperança foi perdida e os artefatos foram usados para propósitos nefastos.")
    time.sleep(2)
    print("O mundo agora enfrenta uma era de trevas e desespero.")

def capitulo5():
    parte = 5
    print("\nCapítulo 5: O Renascimento dos Reinos Esquecidos")
    time.sleep(2)
    print("Com a ajuda dos Relicários e sua coragem, os jogadores triunfam sobre o mal e restauram a paz nos Reinos Esquecidos.")
    time.sleep(2)
    print("Os artefatos são selados novamente, desta vez em um lugar seguro, para evitar que caiam nas mãos erradas novamente.")
    time.sleep(2)
    print("Os heróis são celebrados como lendas e o continente se prepara para uma nova era de prosperidade e harmonia.")

def capitulo6():
    parte = 6
    print("\nCapítulo 6: As Provações Elementais")
    time.sleep(2)
    print("Antes que os heróis possam alcançar o próximo Relicário, eles são desafiados por uma série de provações elementais, cada uma representando um dos quatro elementos primordiais: terra, água, fogo e ar.")
    time.sleep(2)
    print("Cada desafio testa não apenas suas habilidades de combate, mas também sua sabedoria e habilidades mágicas.")

def capitulo7():
    parte =7
    print("\nCapítulo 7: A Trilha da Traição")
    time.sleep(2)
    print("Uma traição inesperada dentro do grupo de heróis os leva a uma busca por um antigo aliado que se voltou para o lado das trevas.")
    time.sleep(2)
    print("Enquanto viajam por terras distantes, eles encontram pistas sobre os motivos por trás da traição e lutam para decidir se devem buscar justiça ou perdão.")

def capitulo8():
    parte = 8
    print("\nCapítulo 8: A Cidadela das Sombras")
    time.sleep(2)
    print("Os jogadores descobrem uma antiga cidadela nas profundezas de uma floresta proibida, onde uma raça ancestral de criaturas das sombras guarda o próximo Relicário.")
    time.sleep(2)
    print("Para alcançá-lo, eles devem atravessar os corredores escuros da fortaleza e enfrentar o poderoso guardião que o protege.")

def capitulo9():
    parte =9
    print("\nCapítulo 9: A Ascensão do Lich")
    time.sleep(2)
    print("Enquanto os heróis se aproximam do terceiro Relicário, eles descobrem que um lich poderoso está tentando subir ao poder.")
    time.sleep(2)
    print("Ele busca usar os artefatos para fortalecer seu domínio sobre os mortos-vivos.")
    time.sleep(2)
    print("Eles devem impedir seus planos malignos antes que seja tarde demais, enfrentando seus exércitos de esqueletos e fantasmas.")

def capitulo10():
    parte = 10
    print("\nCapítulo 10: O Despertar da Besta")
    time.sleep(2)
    print("O último Relicário está escondido em uma ilha remota, habitada por uma antiga besta lendária que dorme há séculos.")
    time.sleep(2)
    print("Os jogadores devem encontrar uma maneira de despertar a besta e derrotá-la para recuperar o Relicário.")
    time.sleep(2)
    print("No entanto, eles logo descobrem que despertar a fera pode ter consequências catastróficas para o mundo.")

def capitulo11():
    parte = 11
    print("\nCapítulo 11: O Julgamento Final")
    time.sleep(2)
    print("Com os quatro Relicários finalmente reunidos, os heróis enfrentam o antagonista final em uma batalha épica que determinará o destino dos Reinos Esquecidos.")
    time.sleep(2)
    print("Eles devem usar todas as suas habilidades, aliados e sabedoria para derrotar o mal de uma vez por todas e restaurar a paz no mundo.")

def capitulo12():
    parte = 12
    print("\nCapítulo 12: O Epílogo")
    time.sleep(2)
    print("Com o mal derrotado e os Reinos Esquecidos seguros mais uma vez, os heróis se separam para seguir seus próprios caminhos.")
    time.sleep(2)
    print("Alguns continuam suas aventuras, enquanto outros escolhem se estabelecer em paz.")
    time.sleep(2)
    print("Mas eles sempre serão lembrados como aqueles que salvaram os Reinos da escuridão e trouxeram esperança para um mundo dilacerado pela guerra e pela intriga.")

def historia():
    introducao()
    capitulo1()
    if escolha_sim_ou_nao("Você aceita a missão para encontrar os Relicários Perdidos?"):
        capitulo2()
        if escolha_sim_ou_nao("Você escolhe viajar pelas florestas assombradas ou pelas montanhas perigosas?"):
            capitulo3()
            if escolha_sim_ou_nao("Você confia em um aliado improvável que oferece ajuda?"):
                capitulo4()
                if escolha_sim_ou_nao("Você está pronto para enfrentar o inimigo final e salvar os Reinos Esquecidos?"):
                    capitulo5()
                else:
                    final_tragico()
            else:
                final_tragico()
        else:
            final_tragico()
    else:
        final_tragico()

    capitulo6()
    if escolha_sim_ou_nao("Você está disposto a enfrentar as Provações Elementais para alcançar o próximo Relicário?"):
        capitulo7()
        if escolha_sim_ou_nao("Você busca justiça ou perdão para o traidor dentro do grupo?"):
            capitulo8()
            if escolha_sim_ou_nao("Você está pronto para enfrentar o guardião da Cidadela das Sombras?"):
                capitulo9()
                if escolha_sim_ou_nao("Você está preparado para enfrentar o Lich e seus exércitos?"):
                    capitulo10()
                    if escolha_sim_ou_nao("Você está pronto para despertar a Besta e recuperar o último Relicário?"):
                        capitulo11()
                        final_feliz()
                    else:
                        final_tragico()
                else:
                    final_tragico()
            else:
                final_tragico()
        else:
            final_tragico()
    else:
        final_tragico()

    capitulo12()

historia()