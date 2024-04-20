def lin(str):
        print ('-'*50)
        print ('{:^50}'.format(f'{str}'))
        print ('-'*50)

def menu(lst):
     l = 0
     k = len(lst)
     for c in lst:
        l = l + 1 
        if l == k:
            print (f'\033[93m {l} - \033[94m {c}\033[0;0m')
        else:
          print (f'\033[93m {l} - \033[94m {c}')

def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print ("\033[91mHouve um erro na criação do arquivo.\033[0;0m")
    
def  lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print ('\033[91mErro ao tentar ler o arquivo.\033[0;0m')
    else:
        p =0
        lin('SAVES CADASTRADOS')
        for linha in a:
            p = p + 1
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print (f'{p} - {dado[0]:<30} Capítulo {dado[1]:>3}')
    finally:
        a.close()

def cadastrar(arq,nome='<desconhecido>',cap=0):
    try:
        a = open(arq, 'at')
    except:
        print ('\033[91mHouve um ERRO na abertura do arquivo.\033[0;0m')
    else:
        try:
            a.write(f"{nome};{cap}\n")
        except:
            print ('\033[91mHouve um ERRO ao escrever os dados!\033[0;0m')
        else:
            print (f"Novo registro do save '{nome}' adicionado.")
            a.close()

def deletar(arq, linha_d):
    with open(arq, 'r') as arquivo:
        linhas = arquivo.readlines()

    if linha_d <= 0 or linha_d > len(linhas):
        print("\033[91mErro! Save especificado está fora do intervalo válido.\033[0;0m")
        return

    linhas.pop(linha_d - 1)
    print (f"Save {linha_d} foi deletado com sucesso")


    with open(arq, 'w') as arquivo:
        arquivo.writelines(linhas)

def ler_arquivo_e_obter_dados(arquivo, numero_linha):
    nome = None
    numero = None
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()

            if numero_linha > 0 and numero_linha <= len(linhas):
                linha_desejada = linhas[numero_linha - 1]  
                partes = linha_desejada.strip().split(';')
                nome = partes[0]
                numero = int(partes[1]) 
            else:
                print("\033[91mErro! Número de save fora do intervalo válido.\033[0;0m")
    except FileNotFoundError:
        print(f"\033[91mErro! O arquivo '{arquivo}' não foi encontrado.\033[0;0m")
    except Exception as e:
        print(f"\033[91mErro! {e}\033[0;0m")
    print (f"Save {linha_a_deletar} foi deletado com sucesso")
    return nome, numero