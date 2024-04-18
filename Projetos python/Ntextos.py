
#  Organizando os espaços
x3 = 11
y3 = 54321
z3 = 3
print("QNT | Código | Nome")
print(f"1   |{x3:^7} | Marcelo")
print(f"2   |{y3:^7} | Grilo")
print(f"3   |{z3:^7} | Pedro")
print ()

#  Usando as cores / modificações das letras
"\033[0;0m"
AZUL ='\033[94m azul'
VERDE ='\033[92m verde'
AMARELO ='\033[93m amarelo'
VERMELHO ='\033[91m vermelho'
NEGRITO ='\033[1m negrito'
SUBLINHADO ='\033[4m sublinhado'
NORMAL ='\033[0;0m normal'
print (NEGRITO, AZUL,VERDE,VERMELHO,AMARELO,NORMAL,SUBLINHADO, "\033[0;0m")

#  Salário:
salario = 0
print("Digite a sua idade : ")
idade2 = input()
print("Qual o  seu salario?")
salario = input()

#  Também podemos fazer:
idade3 = input("Digite sua idade: ")
salario2 = input("Qual o salario? ")

#  Dobro de números: 
numero1 = int(input("Digite um número para ser calculado o seu dobro: "))
dobro = numero1 * 2
print (f"O dobro de {numero1} é {dobro} \U0001f600")