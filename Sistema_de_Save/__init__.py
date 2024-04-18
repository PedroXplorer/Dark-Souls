
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao tentar ler o arquivo')
    else:
        print("""------------------------------------------------------------
            INFORMAÇÕES SALVAS DENTRO DA MEMÓRIA
------------------------------------------------------------""")
        print(a.read())
    finally:
        a.close()

