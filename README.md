Linguagem: python

ATENÇÃO: No próprio código já estão escritas o que cada função, é só usar: 
from Objetos import *
from Inimigos import *
help(nomedafuncaodaclasses)

Funções Incrementadas até o momento:
1 - Classes Caracter e Inimigo:
- A classe Caracter representa o personagem controlado pelo jogador, enquanto a classe Inimigo representa os adversários que o jogador enfrentará.
- Ambas as classes têm atributos como nome, pontos de vida (hp), ataque (atk), defesa (df), nível (lv), pontos de experiência (xp) e ouro (ouro).
- O método Level_up é responsável por permitir que o personagem suba de nível, distribuindo pontos de atributo.
- Os métodos atacar, usar_magia e usar_pocao permitem que o personagem realize ações durante a batalha.
 
2 - Funções exibir_status e batalha:
- exibir_status é responsável por mostrar o estado atual do jogador e do inimigo durante a batalha.
- batalha é onde a mecânica de batalha ocorre. O jogador e o inimigo alternam entre atacar e defender, usando magia e itens de cura.

3 - Funcionalidade Principal:
- O jogador enfrenta uma série de batalhas com diferentes inimigos (inimigo_1, inimigo_2 e inimigo_3) em sequência.
- Após cada batalha bem-sucedida, o jogador recebe pontos de experiência, e quando atinge certos limiares de experiência, pode subir de nível e distribuir pontos de atributo.

4 -  Interface de Usuário:
- O código solicita ao jogador que insira seu nome no início do jogo.
- Durante a batalha, o jogador pode escolher entre atacar, usar magia ou usar itens de cura.
- Em resumo, o código implementa um jogo de aventura simples com combate por turnos, onde o jogador controla um personagem que enfrenta uma série de desafios, ganha experiência e melhora suas habilidades ao longo do tempo.

Ideia Principal do projeto:
A ideia principal é fazer um jogo inspirado nos MUDs de 1970, Zork: The Great Underground Empire e inclusive o final fantasy 1.
O projeto é feito em forma de texto e sem interface gráfica, ainda não tenho uma  história formada, porém,
ele foi imaginado como um jogo de escolhas, onde são informadas opções ao jogador e dependendo a escolha feita,
a história é direcionada para um outro lado...

ADMINISTRADORES ATUAIS DO PROJETO:
- PedroXplorer
- Skip0s
