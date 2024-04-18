

from RPG_MUD import *
from time import sleep
import os

print ()
os.system("cls")
# sleep(1.75)
# print ('''
#                                         ╔════════════════╗
#             LOADING...                  ┃ ▁▂      10%    |                 
#                                         ╚════════════════╝
# ''',flush=True)
# sleep(1.75)
# os.system("cls")
# print ('''
#                                         ╔════════════════╗
#             LOADING...                  ┃ ▁▂▃▅    50%    |                 
#                                         ╚════════════════╝
# ''',flush=True)
# sleep(1.75)
# os.system("cls")
# print ('''
#                                         ╔════════════════╗
#             LOADING...                  ┃ ▁▂▃▅▆   80%    |                 
#                                         ╚════════════════╝
# ''',flush=True)
# sleep(1.75)
# os.system("cls")
# print ('''
#                                         ╔════════════════╗
#             LOADING...                  ┃ ▁▂▃▅▆▇ 100%    |                 
#                                         ╚════════════════╝
# ''',flush=True)

# sleep(1.75)
# os.system("cls")


# Menu -----

menu = (''' -------------------------------------------------------------------------------------------------------------------------

             █▄██▄█                  █▄██▄█                  █▄██▄█                  █▄██▄█                  █▄██
    █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄█▐█ ╔═════════════════════╗ ██▌█▄█▄█▄█▄██▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄██▄█▄█▄█▄█▐█┼█
    ███┼█████▐████▌█████┼██████┼█████▐█ <   80's Retro Quest  > ██▌█████┼██████┼█████▐████▌█████┼██████┼█████▐███
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



começo()