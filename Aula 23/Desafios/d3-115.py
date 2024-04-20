from tech import *
from arquivo import *

arq = 'CADASTROS_PESSOAS2.txt'

if arquivoExiste(arq):
    print(">> Arquivo encontrado com sucesso!")
else:
    print (f'>> Arquivo {arq} não encontrado')
    criarArquivo(arq)
    print (f'\n>> Arquivo {arq} criado com sucesso!')

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
        while scl != '1' and scl != '2' and scl != '3':
            print("\033[91mERRO! Digite uma opção válida.\033[0;0m")

            try:
                scl = (input("\033[93mSua Opção: \033[0;0m"))
            except:
                print ()
                lin('Saindo do sistema... Até logo!')
                print ()
                quit()

        if scl == "1":
            lerArquivo(arq)

        elif scl == "2":
            lin('NOVO CADASTRO')
            nome = input("Nome: ")
            idade = input("Idade: ")
            while not idade.isnumeric():
                print("\033[91mERRO! Digite uma idade válida.\033[0;0m")
                idade = input("Idade: ")
            idade = int(idade)
            cadastrar(arq,nome,idade)

        elif scl == "3":
            print ()
            lin('Saindo do sistema... Até logo!')
            print ()
            quit()
