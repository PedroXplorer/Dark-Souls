
def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except(ValueError,TypeError):
            print("\033[91mERRO! Digite um número real válido.\033[0;0m")
            continue
        except (KeyboardInterrupt):
            print ('\033[91mEntrada de dados interrompida por usuário.\033[0;0m')
            return 0
        else:
            return f
        

        

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print("\033[91mERRO! Digite um número inteiro válido.\033[0;0m")
            continue
        except (KeyboardInterrupt):
            print ('\033[91mEntrada de dados interrompida por usuário.\033[0;0m')
            return 0
        else:
            return n
        
n = leiaInt("Digite um inteiro: ")
f = leiaFloat("Digite um número real: ")

print (f'Número inteiro: {n}\nNúmero Real: {f}')