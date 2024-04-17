from time import sleep
from random import randint

def t(n):
    sleep(n)

import random

def mostrar_status(jogador, inimigo):
    print("\nStatus:")
    print(f"Jogador: HP {jogador['hp']}")
    print(f"Inimigo: HP {inimigo['hp']}")

def ataque(jogador, inimigo):
    dano_jogador = random.randint(1, 10)
    dano_inimigo = random.randint(1, 8)

    inimigo['hp'] -= dano_jogador
    jogador['hp'] -= dano_inimigo

    print(f"\nVocê causou {dano_jogador} de dano ao inimigo.")
    print(f"Você recebeu {dano_inimigo} de dano do inimigo.")

def batalha():
    jogador = {'hp': 30}
    inimigo = {'hp': 20}

    print("Bem-vindo à batalha!")

    while jogador['hp'] > 0 and inimigo['hp'] > 0:
        mostrar_status(jogador, inimigo)

        escolha = input("\nO que você deseja fazer? (atacar/defender): ").lower()

        if escolha == 'atacar':
            ataque(jogador, inimigo)
        elif escolha == 'defender':
            print("Você se defendeu.")
        else:
            print("Comando inválido. Tente novamente.")

    if jogador['hp'] <= 0:
        print("\nVocê foi derrotado. Game Over!")
    else:
        print("\nVocê derrotou o inimigo! Parabéns!")

batalha()

def começo():
    print ("")
    print ('Seja bem-Vindo(a) ao mundo de Sagak aventureiro(a)!')
    t(1)
    nome = input('>> Primeiramente insira o seu nome: ')
    t(1)
    print("Muito bem vamos começar...")
    print("\nVocê está na sua cama, porém começar aos poucos escutar gritos que parecem de dor, parece estar vindo do andar debaixo.")
    t(1)
    e1 = input(f">> Você quer ir verificar o que é ou deseja voltar a dormir {nome}? [Verificar / Continuar no quarto]: ").lower()
    

    if e1 == "v":
        ver = 1
        print("\nVocê decide sair e descer as escadas e verificar o que está acontecendo, ao que parece não mais ninguém em casa.")
        t(1.75)
        print ('Você sente algo molhado em seus pés, é um liquído vermelho e ele está formando um trilha até fora de sua casa.')
        t(1)
        e2 = input(f">> {nome} vai ir para fora ou vai voltar para cama e acorda desse pesadelo? [ Olhar / Temer ]: ").lower()

        if e2 == 'o':
            t(1)
            print ("\nVocê decide olhar para ver o que está acontecendo lá fora, você tropeça em dois corpos, são os dos seus pais. \nVocê olha ao redor e vê que a aldeia em você morou sua vida toda está em chamas, você decide voltar para o seu quarto e se esconder de baixo da sua cama.")
            t(1)
        else:
            t(1)
            print ('Você decide retornar para seu quarto e esperar a noite acabar.')

    else:
        ver = 2
    print(f"""
{nome} deseja que tudo isso seja um sonho ruim, tenta dormir porém os gritos continuam. \nDecide então pegar o seu travesseiro e tampar os seus ouvidos, mesmo cansado e com medo consegue dormir, de mal jeito, porém consegue. """) 
    t(1)
    print("Você encontra um final trágico. Fim da aventura.")

começo()


def lutar():
    import random

    class Personagem:
        def __init__(self, nome, hp, mp, atk, defe):
            self.nome = nome
            self.hp = hp
            self.mp = mp
            self.atk = atk
            self.defe = defe

        def atacar(self, alvo):
            dano = self.atk - alvo.defe
            alvo.hp -= dano
            return dano

        def usar_magia(self, alvo):
            if self.mp >= 5:
                dano_magia = random.randint(5, 10)
                alvo.hp -= dano_magia
                self.mp -= 5
                return dano_magia
            else:
                return 0

    def batalha(personagem, inimigo):
        while personagem.hp > 0 and inimigo.hp > 0:
            print(f"\n{personagem.nome} - HP: {personagem.hp} | MP: {personagem.mp}")
            print(f"{inimigo.nome} - HP: {inimigo.hp}")

            acao = input("\nEscolha sua ação: [1] Atacar | [2] Usar Magia\n")

            if acao == '1':
                dano = personagem.atacar(inimigo)
                print(f"\nVocê atacou {inimigo.nome} e causou {dano} de dano!")
            elif acao == '2':
                dano_magia = personagem.usar_magia(inimigo)
                if dano_magia > 0:
                    print(f"\nVocê usou magia em {inimigo.nome} e causou {dano_magia} de dano!")
                else:
                    print("\nVocê não tem MP suficiente para usar magia.")
            else:
                print("\nAção inválida. Tente novamente.")

            if inimigo.hp > 0:
                dano_inimigo = inimigo.atacar(personagem)
                print(f"\n{inimigo.nome} atacou você e causou {dano_inimigo} de dano!")

        if personagem.hp <= 0:
            print("\nVocê foi derrotado. Game Over!")
        else:
            print(f"\nParabéns! Você derrotou {inimigo.nome}!")

    if __name__ == "__main__":
        seu_personagem = Personagem("Herói", 50, 20, 10, 5)
        inimigo = Personagem("Monstro", 30, 0, 8, 2)

        print("Batalha contra um Monstro!")
        batalha(seu_personagem, inimigo)

lutar()