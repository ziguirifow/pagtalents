import random


def jogo():
    print("Jogo de Adivinhação\n")

    numero = random.randrange(1, 101)
    pontos = 500

    print("Escolha o nível de dificuldade")

    nivel = int(input("[1]Fácil [2]Médio [3]Difícil: )")
    if nivel == 1:
        total_de_tentativas = 15
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5