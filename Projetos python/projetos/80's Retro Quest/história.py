import time

def historia():
    print("Bem-vindo à aventura!")
    time.sleep(1)
    print("Você está em uma encruzilhada na floresta.")
    time.sleep(1)

    escolha_1 = input("Você quer ir para a esquerda ou para a direita? (esquerda/direita): ").lower()

    if escolha_1 == "esquerda":
        print("Você encontra uma caverna escura.")
        time.sleep(1)
        escolha_2 = input("Você entra na caverna ou continua pela floresta? (caverna/floresta): ").lower()

        if escolha_2 == "caverna":
            print("Dentro da caverna, você encontra um dragão adormecido.")
            time.sleep(1)
            escolha_3 = input("Você tenta acordar o dragão ou sai silenciosamente? (acordar/sair): ").lower()

            if escolha_3 == "acordar":
                print("O dragão acorda e... você se torna amigo dele!")
                time.sleep(1)
                print("Parabéns, você encontrou um final feliz!")
            else:
                print("Você sai silenciosamente da caverna.")
                time.sleep(1)
                print("Você continua sua jornada e encontra um vilarejo.")
                time.sleep(1)
                print("Parabéns, você encontrou um final positivo!")

        else:
            print("Você continua pela floresta e encontra um rio.")
            time.sleep(1)
            print("Infelizmente, você não sabe nadar e...")
            time.sleep(1)
            print("Você encontra um final trágico. Fim da aventura.")

    else:
        print("Você segue para a direita e encontra uma ponte.")
        time.sleep(1)
        escolha_4 = input("Você atravessa a ponte ou volta para trás? (atravessar/voltar): ").lower()

        if escolha_4 == "atravessar":
            print("Você atravessa a ponte com sucesso e encontra um tesouro!")
            time.sleep(1)
            print("Parabéns, você encontrou um final feliz!")
        else:
            print("Você decide voltar para trás e se perde na floresta.")
            time.sleep(1)
            print("Infelizmente, você não encontra o caminho de volta.")
            time.sleep(1)
            print("Você encontra um final trágico. Fim da aventura.")

if __name__ == "__main__":
    historia()