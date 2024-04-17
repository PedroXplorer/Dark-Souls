
from time import sleep
import os

print ()
os.system("cls")
sleep(1.75)
print ('''
                                         ╔════════════════╗
             LOADING...                  ┃ ▁▂      10%    |                 
                                         ╚════════════════╝
 ''',flush=True)
sleep(1.75)
os.system("cls")
print ('''
                                         ╔════════════════╗
             LOADING...                  ┃ ▁▂▃▅    50%    |                 
                                         ╚════════════════╝
 ''',flush=True)
sleep(1.75)
os.system("cls")
print ('''
                                         ╔════════════════╗
             LOADING...                  ┃ ▁▂▃▅▆   80%    |                 
                                         ╚════════════════╝
 ''',flush=True)
sleep(1.75)
os.system("cls")
print ('''
                                         ╔════════════════╗
             LOADING...                  ┃ ▁▂▃▅▆▇ 100%    |                 
                                         ╚════════════════╝
 ''',flush=True)

sleep(1.75)
os.system("cls")


# Menu -----

menu = (''' -------------------------------------------------------------------------------------------------------------------------

             █▄██▄█                  █▄██▄█                  █▄██▄█                  █▄██▄█                  █▄██
    █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄█▐█ ╔═════════════════════╗ ██▌█▄█▄█▄█▄██▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄█▐█┼█
    ███┼█████▐████▌█████┼██████┼█████▐█ <    Retro Quest      > ██▌█████┼██████┼█████▐████▌█████┼██████┼█████▐███
    █████████▐████▌██████████████████▐█ ╚═════════════════════╝ ██▌██████████████████▐████▌██████████████████▐███
    █████████▐████▌██████████████████▐████▌██████████████████▐████▌██████████████████▐████▌██████████████████▐███
       
                                Por:   Pedro Henrique Alves Martins 
--------------------------------------------------------------------------------------------------------------------------
    >> (c) Pedro Henrique Alves Martins .Todos os direitos reservados.
            
    \033[0;0mMeu instagram: \033[94mhttps://www.instagram.com/pdrhnrqalvesmartins/\033[0;0m
    Meu GitHub: \033[94mhttps://github.com/PedroXplorer/PedroXplorer\033[0;0m  
    Meu site: \033[94mhttps://8049170068179271.carrd.co/\033[0;0m
>> Recomendável ver as informações sobre o jogo antes de começar a jogar.

\033[93m \033[1m        -- [S] -- \033[0;0m   Começar o jogo
              
\033[93m \033[1m        -- [R] -- \033[0;0m   Mostrar Saves

\033[93m \033[1m        -- [M] -- \033[0;0m   Mostrar Créditos

\033[93m \033[1m        -- [L] -- \033[0;0m   Linguagem

\033[93m \033[1m        -- [I] -- \033[0;0m   Informações sobre o jogo

\033[93m \033[1m        -- [Q] -- \033[0;0m   Fechar o jogo
''')

os.system('cls')

print (menu)

e = str(input(">> Sua opção: ")) 

e = e.strip()
while True:
##  Sair
    if e in "Qq":
        sleep(1.75)
        print ("")
        print ("")
        quit ()
    
## Começar o jogo  
    elif e in "Ss":
        sleep(1.75)
        os.system('cls') 
        print ("")
        break
        break
        
## Mostrar Créditos
    elif e in "Mm":
        sleep(1.75)
        os.system('cls')
        print ("")
        print ("       Criador: Pedro Henrique ")
        print ("")
        str(input("     [ Pressione ENTER ]"))
        print ("")
        sleep(1.75)
        os.system('cls')
        print (menu)
        e = str(input(">> Sua opção: ")) 


## Informações do jogo
    elif e in "Ii":
        sleep(1.75)
        os.system('cls')
        print ('''
 
        Funcionamento do jogo:       
         
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
        sleep(1.75)
        os.system('cls')
        print (menu)
        e = str(input(">> Sua opção: ")) 



## Linguagem
    elif e in "Ll":
        sleep(1.75)
        os.system('cls')
        print ('''
        
        [1] Português
        [2] Inglês (em breve)

''')
        str(input("   [ Pressione ENTER ]"))
        os.system('cls')
        print (menu)
        e = str(input(">> Sua opção: ")) 


    else:
        print ()
        print (" Insira uma opção válida... ")
        sleep(1)
        os.system('cls')
        print (menu)
        e = str(input(">> Sua opção: ")) 



# ------------------------------------------------------------------------------------------------

## Começo 
import time


def introducao():
    print("Nos Reinos Esquecidos, um continente repleto de magia, criaturas misteriosas e perigos inimagináveis, uma antiga profecia ressurge.")
    time.sleep(2)
    print("Diz-se que há séculos atrás, quatro relicários sagrados foram criados para proteger o mundo da escuridão.")
    time.sleep(2)
    print("Porém, eles foram perdidos ao longo do tempo e agora ameaçam cair nas mãos erradas.")
    time.sleep(2)
    print("Aventureiros de todo o continente são convocados para encontrar os relicários e salvar os Reinos Esquecidos da destruição iminente.")
    time.sleep(2)

def capitulo1():
    print("\nCapítulo 1: O Despertar das Profecias")
    time.sleep(2)
    print("Os jogadores começam em uma pequena vila, onde coisas estranhas começam a acontecer.")
    time.sleep(2)
    print("Uma série de eventos misteriosos, como desaparecimentos inexplicáveis e o surgimento de criaturas sombrias, levam os heróis a descobrir que algo está ameaçando a paz nos Reinos Esquecidos.")
    time.sleep(2)
    print("Eles são recrutados por um sábio ancião que revela a profecia dos Relicários Perdidos e os encarrega de encontrar e proteger esses artefatos antigos.")
    time.sleep(2)

def capitulo2():
    print("\nCapítulo 2: A Busca pelos Relicários")
    time.sleep(2)
    print("Os jogadores embarcam em uma jornada épica através de florestas assombradas, montanhas perigosas e cidades corrompidas, enfrentando inúmeros desafios pelo caminho.")
    time.sleep(2)
    print("Eles encontram pistas e aliados improváveis, mas também enfrentam adversários poderosos que desejam os relicários para seus próprios fins nefastos.")
    time.sleep(2)

def capitulo3():
    print("\nCapítulo 3: Revelações e Traições")
    time.sleep(2)
    print("Enquanto os heróis se aproximam de encontrar o primeiro Relicário, eles descobrem segredos sombrios sobre a história dos Reinos Esquecidos e aqueles que governam sobre eles.")
    time.sleep(2)
    print("Traições dentro do próprio grupo e alianças inesperadas desafiam sua lealdade e determinação.")
    time.sleep(2)

def capitulo4():
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
    print("\nCapítulo 5: O Renascimento dos Reinos Esquecidos")
    time.sleep(2)
    print("Com a ajuda dos Relicários e sua coragem, os jogadores triunfam sobre o mal e restauram a paz nos Reinos Esquecidos.")
    time.sleep(2)
    print("Os artefatos são selados novamente, desta vez em um lugar seguro, para evitar que caiam nas mãos erradas novamente.")
    time.sleep(2)
    print("Os heróis são celebrados como lendas e o continente se prepara para uma nova era de prosperidade e harmonia.")

def capitulo6():
    print("\nCapítulo 6: As Provações Elementais")
    time.sleep(2)
    print("Antes que os heróis possam alcançar o próximo Relicário, eles são desafiados por uma série de provações elementais, cada uma representando um dos quatro elementos primordiais: terra, água, fogo e ar.")
    time.sleep(2)
    print("Cada desafio testa não apenas suas habilidades de combate, mas também sua sabedoria e habilidades mágicas.")

def capitulo7():
    print("\nCapítulo 7: A Trilha da Traição")
    time.sleep(2)
    print("Uma traição inesperada dentro do grupo de heróis os leva a uma busca por um antigo aliado que se voltou para o lado das trevas.")
    time.sleep(2)
    print("Enquanto viajam por terras distantes, eles encontram pistas sobre os motivos por trás da traição e lutam para decidir se devem buscar justiça ou perdão.")

def capitulo8():
    print("\nCapítulo 8: A Cidadela das Sombras")
    time.sleep(2)
    print("Os jogadores descobrem uma antiga cidadela nas profundezas de uma floresta proibida, onde uma raça ancestral de criaturas das sombras guarda o próximo Relicário.")
    time.sleep(2)
    print("Para alcançá-lo, eles devem atravessar os corredores escuros da fortaleza e enfrentar o poderoso guardião que o protege.")

def capitulo9():
    print("\nCapítulo 9: A Ascensão do Lich")
    time.sleep(2)
    print("Enquanto os heróis se aproximam do terceiro Relicário, eles descobrem que um lich poderoso está tentando subir ao poder.")
    time.sleep(2)
    print("Ele busca usar os artefatos para fortalecer seu domínio sobre os mortos-vivos.")
    time.sleep(2)
    print("Eles devem impedir seus planos malignos antes que seja tarde demais, enfrentando seus exércitos de esqueletos e fantasmas.")

def capitulo10():
    print("\nCapítulo 10: O Despertar da Besta")
    time.sleep(2)
    print("O último Relicário está escondido em uma ilha remota, habitada por uma antiga besta lendária que dorme há séculos.")
    time.sleep(2)
    print("Os jogadores devem encontrar uma maneira de despertar a besta e derrotá-la para recuperar o Relicário.")
    time.sleep(2)
    print("No entanto, eles logo descobrem que despertar a fera pode ter consequências catastróficas para o mundo.")

def capitulo11():
    print("\nCapítulo 11: O Julgamento Final")
    time.sleep(2)
    print("Com os quatro Relicários finalmente reunidos, os heróis enfrentam o antagonista final em uma batalha épica que determinará o destino dos Reinos Esquecidos.")
    time.sleep(2)
    print("Eles devem usar todas as suas habilidades, aliados e sabedoria para derrotar o mal de uma vez por todas e restaurar a paz no mundo.")

def capitulo12():
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
    if escolha_sim_ou_nao("Você está disposto(a) a enfrentar as Provações Elementais para alcançar o próximo Relicário?"):
        capitulo7()
        if escolha_sim_ou_nao("Você busca justiça ou perdão para o traidor dentro do grupo?"):
            capitulo8()
            if escolha_sim_ou_nao("Você está pronto(a) para enfrentar o guardião da Cidadela das Sombras?"):
                capitulo9()
                if escolha_sim_ou_nao("Você está preparado(a) para enfrentar o Lich e seus exércitos?"):
                    capitulo10()
                    if escolha_sim_ou_nao("Você está pronto(a) para despertar a Besta e recuperar o último Relicário?"):
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

if __name__ == "__main__":
    historia()



