from tech import lin

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
        print ("Houve um erro na criação do arquivo")
    
def  lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print ('Erro ao tentar ler o arquivo')
    else:
        p =0
        lin('PESSOAS CADASTRADAS')
        for linha in a:
            p = p + 1
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print (f'{p} - {dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq,nome='<desconhecido>',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print ('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print ('Houve um ERRO no tempo de formular os dados!')
        else:
            print (f'Novo registro de {nome} adicionado.')
            a.close()

