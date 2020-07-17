import random


def jogo():
    print("Jogo de adivinhação!\n")

    numero = random.randrange(1, 101)
    pontos = 500

    print("Qual nível de dificuldade?")

    nivel = int(input("[1]Fácil [2]Médio [3]Difícil: "))
    if nivel == 1:
        total_de_tentativas = 15
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero
        maior   = chute > numero
        menor   = chute < numero

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero - chute)
            pontos = pontos - pontos_perdidos

    print("\nFim do jogo!")


if __name__ == "__main__":
    jogo()
