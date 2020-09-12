import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    numero_secreto = int(round(numero_secreto))
    pontos = 1000
    # print(f"O número secreto é {numero_secreto}")
    total_de_tentativas = 0
    rodada = 1

    print("Qual a dificuldade desejada?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Informe sua escolha: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print(f"\nTentativa {rodada} de {total_de_tentativas}")
        print(f"Pontuação atual: {pontos} pontos.")
        chute_str = input("Digite o seu número entre 1 e 100: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Seu número deve estar entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("****************************************")
            print(f"Você acertou! Sua pontuação foi de {pontos} pontos!")
            print("****************************************")
            break
        else:
            if (maior):
                print("****************************************")
                print("Você errou! O seu chute foi maior que o número secreto.")
                print("****************************************")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            elif (menor):
                print("****************************************")
                print("Você errou! O seu chute foi menor que o número secreto.")
                print("****************************************")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
