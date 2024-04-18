from tech import *
from arquivo import *
from time import sleep
import tech



arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print("Arquivo encontrado com sucesso!")
else:
    print ('Arquivo não encontrado')


pessoas = {
        'Pedro Henrique': 14,
        'Dulcinéia Alves': 52,
        'Eduardo Henrique': 20,
        "Finéias Anselmo": 51
    }

while True:
    lst = ['Ver pessoas cadastradas','Cadastrar nova Pessoa',"Sair do sistema"]
    print ()
    lin('MENU PRINCIPAL')
    menu(lst)
    print ('-'*50)
    try:
        scl = (input("\033[93mSua Opção: \033[0;0m"))

    except:
        print ()
        lin('Saindo do sistema... Até logo!')
        print ()
        quit()


    else:
        if scl == "1":
            lin('PESSOAS CADASTRADAS')
            for k,v in pessoas.items():
                print ("{:<30}".format(f'{k}'),'{:<20}'.format(f'{v} anos'))

        elif scl == "2":
            lin('NOVO CADASTRO')
            n = input("Nome: ")
            i = input("Idade: ")
            while not i.isnumeric():
                print("\033[91mERRO! Digite uma idade válida.\033[0;0m")
                i = input("Idade: ")
            i = int(i)
            pessoas[n] = i

            print (f'Novo registro de {n} adicionado.')
        elif scl == "3":
            print ()
            lin('Saindo do sistema... Até logo!')
            print ()
            quit()

        while scl != '1' and scl != '2' and scl != '3':
            print("\033[91mERRO! Digite uma opção válida.\033[0;0m")
            try:
                scl = (input("\033[93mSua Opção: \033[0;0m"))

            except:
                print ()
                lin('Saindo do sistema... Até logo!')
                print ()
                quit()