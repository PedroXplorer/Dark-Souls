# Ordem de organizar Personagem 
# --  self, name,hpi, hp, atk, mgk, df, ouro, php = 0, pmk = 0,lv =0, xp =0, m= 0

# Ordem de organizar inimigos
# --   name, hp, atk, df,lv,ouro, xp = 0

#Ordem de organizar itens
# -- name, tipo, atk =0, mgk =0 ,hp =0, df = 0 

# Código principal do programa, utiliza funções da pasta 'Objetos' e 'Equipamento'


# -----------------------------------------------------------------------------------------

from random import randint
from Objetos import *
from Equipamento import *

nome_jogador = input("\nDigite o nome do seu personagem: ")
jogador_principal = Caracter(nome_jogador,35, 35, 8, 10, 8, 0, 2,2)

#print("\nBem-vindo ao Jogo de Aventura!")
#print(f"{jogador_principal.name}, prepare-se para a batalha!\n")

#batalha(jogador_principal, RatoGigante)
#batalha(jogador_principal, Slime)
#batalha(jogador_principal, Morcego)
#batalha(jogador_principal, Aguia)
#print('')
#print('XP total obtido: ',jogador_principal.xp)

# ----------------------------------------------------------------------------------------



# Capítulo 1: O Despertar das Profecias
# Introdução
print("Introdução:")
print("Nos Reinos Esquecidos, um continente repleto de magia, criaturas misteriosas e perigos inimagináveis, uma antiga profecia ressurge...")
print("\nCapítulo 1: O Despertar das Profecias")
print("Os jogadores começam em uma pequena vila, onde coisas estranhas começam a acontecer. Uma série de eventos misteriosos, como desaparecimentos inexplicáveis e o surgimento de criaturas sombrias, levam os heróis a descobrir que algo está ameaçando a paz nos Reinos Esquecidos.")

# Recrutamento
print("\nRecrutamento:")
print("Os jogadores são recrutados por um sábio ancião que revela a profecia dos Relicários Perdidos e os encarrega de encontrar e proteger esses artefatos antigos.")

# Início da jornada
print("\nInício da Jornada:")
print("Os heróis partem da vila em direção ao desconhecido, determinados a descobrir a verdade por trás dos eventos perturbadores que estão ocorrendo nos Reinos Esquecidos.")

# Fim do Capítulo 1
print("\nFim do Capítulo 1: O Despertar das Profecias")



# Capítulo 2: A Busca pelos Relicários
# Introdução
print("\nCapítulo 2: A Busca pelos Relicários")
print("Os jogadores embarcam em uma jornada épica através de florestas assombradas, montanhas perigosas e cidades corrompidas, enfrentando inúmeros desafios pelo caminho.")

# Encontro com aliados improváveis
print("\nEncontro com Aliados Improváveis:")
print("Os heróis encontram aliados improváveis que se juntam à sua causa, oferecendo ajuda e informações valiosas.")

# Confronto com inimigos poderosos
print("\nConfronto com Inimigos Poderosos:")
print("Os jogadores enfrentam inimigos poderosos que desejam os relicários para seus próprios fins nefastos, testando sua coragem e habilidades de combate.")

# Descoberta de pistas
print("\nDescoberta de Pistas:")
print("Os heróis encontram pistas sobre a localização dos relicários, levando-os cada vez mais perto de seu objetivo.")

# Fim do Capítulo 2
print("\nFim do Capítulo 2: A Busca pelos Relicários")

# Função para batalha com inimigo poderoso
batalha(jogador_principal,Slime)

# Exemplo de uso:
# batalha_com_inimigo_poderoso(jogador, DragãoAncião)



# Capítulo 3: Revelações e Traições
# Introdução
print("\nCapítulo 3: Revelações e Traições")
print("Enquanto os heróis se aproximam de encontrar o primeiro Relicário, eles descobrem segredos sombrios sobre a história dos Reinos Esquecidos e aqueles que governam sobre eles.")

# Traição dentro do grupo
print("\nTraição Dentro do Grupo:")
print("Uma traição inesperada dentro do grupo de heróis os leva a uma busca por um antigo aliado que se voltou para o lado das trevas.")

# Alianças inesperadas
print("\nAlianças Inesperadas:")
print("Enquanto viajam por terras distantes, os heróis encontram aliados improváveis e lutam para decidir se devem buscar justiça ou perdão.")

# Fim do Capítulo 3
print("\nFim do Capítulo 3: Revelações e Traições")

# Função para confronto com traidor
batalha(jogador_principal,RatoGigante)

# Exemplo de uso:
# confronto_com_traidor(jogador, TraidorAntigo)



# Capítulo 4: O Confronto Final
# Introdução
print("\nCapítulo 4: O Confronto Final")
print("Após superar todos os obstáculos, os jogadores finalmente localizam os quatro Relicários. No entanto, eles descobrem que um antigo inimigo está tramando para usar os artefatos para mergulhar os Reinos Esquecidos na escuridão eterna.")

# Batalha épica
print("\nBatalha Épica:")
print("Uma batalha épica se desenrola, com o destino dos Reinos pendendo na balança.")

# Triunfo sobre o mal
print("\nTriunfo Sobre o Mal:")
print("Com a ajuda dos Relicários e sua coragem, os jogadores triunfam sobre o mal e restauram a paz nos Reinos Esquecidos.")

# Fim do Capítulo 4
print("\nFim do Capítulo 4: O Confronto Final")

# Função para a batalha épica final
batalha(jogador_principal,Aguia)
        # Lógica da batalha épica final

# Exemplo de uso:
# batalha_epica_final(jogador, AntigoInimigo)



# Capítulo 5: O Renascimento dos Reinos Esquecidos
# Introdução
print("\nCapítulo 5: O Renascimento dos Reinos Esquecidos")
print("Com o mal derrotado e os Reinos Esquecidos seguros mais uma vez, os heróis se separam para seguir seus próprios caminhos.")

# Celebração como lendas
print("\nCelebração como Lendas:")
print("Os heróis são celebrados como lendas e o continente se prepara para uma nova era de prosperidade e harmonia.")
# Fim do Capítulo 5
print("\nFim do Capítulo 5: O Renascimento dos Reinos Esquecidos")



# Capítulo 6: As Provações Elementais
# Introdução
print("\nCapítulo 6: As Provações Elementais")
print("Antes que os heróis possam alcançar o próximo Relicário, eles são desafiados por uma série de provações elementais, cada uma representando um dos quatro elementos primordiais: terra, água, fogo e ar.")

# Desafios elementais
print("\nDesafios Elementais:")
print("Cada desafio testa não apenas suas habilidades de combate, mas também sua sabedoria e habilidades mágicas.")

# Fim do Capítulo 6
print("\nFim do Capítulo 6: As Provações Elementais")

# Capítulo 7: A Trilha da Traição
# Introdução
print("\nCapítulo 7: A Trilha da Traição")
print("Uma traição inesperada dentro do grupo de heróis os leva a uma busca por um antigo aliado que se voltou para o lado das trevas.")

# Busca pelo traidor
print("\nBusca pelo Traidor:")
print("Os heróis viajam por terras distantes, seguindo as pistas sobre os motivos por trás da traição e lutando para decidir se devem buscar justiça ou perdão.")

# Fim do Capítulo 7
print("\nFim do Capítulo 7: A Trilha da Traição")

# Função para busca e confronto com o traidor
batalha(jogador_principal,Morcego)
        # Lógica da busca e confronto com o traidor

# Exemplo de uso:
# busca_e_confronto_traidor(jogador, TraidorAntigo)



# Capítulo 8: A Cidadela das Sombras
# Introdução
print("\nCapítulo 8: A Cidadela das Sombras")
print("Os jogadores descobrem uma antiga cidadela nas profundezas de uma floresta proibida, onde uma raça ancestral de criaturas das sombras guarda o próximo Relicário.")

# Exploração da cidadela
print("\nExploração da Cidadela:")
print("Os heróis devem atravessar os corredores escuros da fortaleza e enfrentar o poderoso guardião que o protege.")

# Fim do Capítulo 8
print("\nFim do Capítulo 8: A Cidadela das Sombras")

# Função para exploração e batalha na cidadela
batalha(jogador_principal,Slime)
        # Lógica da exploração e batalha na cidadela

# Exemplo de uso:
# exploracao_e_batalha_cidadela(jogador, GuardiaoDasSombras)


# Capítulo 9: A Ascensão do Lich
# Introdução
print("\nCapítulo 9: A Ascensão do Lich")
print("Enquanto os heróis se aproximam do terceiro Relicário, eles descobrem que um lich poderoso está tentando subir ao poder, buscando usar os artefatos para fortalecer seu domínio sobre os mortos-vivos.")

# Confronto com o lich
print("\nConfronto com o Lich:")
print("Os heróis devem impedir os planos malignos do lich antes que seja tarde demais, enfrentando seus exércitos de esqueletos e fantasmas.")

# Fim do Capítulo 9
print("\nFim do Capítulo 9: A Ascensão do Lich")

# Função para confronto com o lich
batalha(jogador_principal,Aguia)
        # Lógica do confronto com o lich

# Exemplo de uso:
# confronto_com_lich(jogador, LichPoderoso)



# Capítulo 10: O Despertar da Besta
# Introdução
print("\nCapítulo 10: O Despertar da Besta")
print("O último Relicário está escondido em uma ilha remota, habitada por uma antiga besta lendária que dorme há séculos.")

# Despertar da besta
print("\nDespertar da Besta:")
print("Os jogadores devem encontrar uma maneira de despertar a besta e derrotá-la para recuperar o Relicário.")

# Fim do Capítulo 10
print("\nFim do Capítulo 10: O Despertar da Besta")

# Função para despertar da besta e batalha
batalha(jogador_principal,Slime)

# Exemplo de uso:
# despertar_da_besta_e_batalha(jogador, BestaLendaria)



# Capítulo 11: O Julgamento Final
# Introdução
print("\nCapítulo 11: O Julgamento Final")
print("Com os quatro Relicários finalmente reunidos, os heróis enfrentam o antagonista final em uma batalha épica que determinará o destino dos Reinos Esquecidos.")

# Batalha épica final
print("\nBatalha Épica Final:")
print("Os heróis devem usar todas as suas habilidades, aliados e sabedoria para derrotar o mal de uma vez por todas e restaurar a paz no mundo.")

# Fim do Capítulo 11
print("\nFim do Capítulo 11: O Julgamento Final")

# Função para a batalha épica final
batalha(jogador_principal,Morcego)
        # Lógica da batalha épica final

# Exemplo de uso:
# batalha_epica_final(jogador, AntagonistaFinal)



# Capítulo 12: O Epílogo
# Introdução
print("\nCapítulo 12: O Epílogo")
print("Com o mal derrotado e os Reinos Esquecidos seguros mais uma vez, os heróis se separam para seguir seus próprios caminhos.")

# Legado dos heróis
print("\nLegado dos Heróis:")
print("Alguns continuam suas aventuras, enquanto outros escolhem se estabelecer em paz. Mas eles sempre serão lembrados como aqueles que salvaram os Reinos da escuridão e trouxeram esperança para um mundo dilacerado pela guerra e pela intriga.")

# Fim do Capítulo 12
print("\nFim do Capítulo 12: O Epílogo")
