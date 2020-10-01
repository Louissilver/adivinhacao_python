import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    palavras = []
    arquivo = open("palavras.txt", "r")
    for palavra in arquivo:
        palavras.append(palavra.strip())
    arquivo.close()


    aleatorio = random.randrange(0, (len(palavras)+1))
    palavra_secreta = palavras[aleatorio].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    tentativas = 5
    enforcou = False
    acertou = False

    print("Palavra secreta:")
    print(letras_acertadas)
    print(f"\nVocê pode errar {tentativas} vezes\n")

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        posicao = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(letra == chute):
                    letras_acertadas[posicao] = chute
                posicao += 1
            print("Boa! Encontrei sua letra na palavra!")
            print(letras_acertadas)
        else:
            print("Não foi dessa vez, tente novamente!")
            tentativas -= 1
            print(f"Você ainda pode errar {tentativas} tentativas!")
            if(tentativas == 0):
                enforcou = True;
                print("Você foi enforcado!")
        acertou = "_" not in letras_acertadas
        if(acertou):
            print("Parabéns! Você ganhou!")
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()