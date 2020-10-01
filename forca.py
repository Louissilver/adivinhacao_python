import random

def jogar():
    imprimirBoasVindas()
    palavra_secreta = carregarPalavraSecreta()
    letras_acertadas = carregarLetrasCorretas(palavra_secreta)
    print("Palavra secreta:")
    print(letras_acertadas)

    tentativas = 7
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = solicitaChute()
        if (chute in palavra_secreta):
            marcaChuteCorreto(chute, palavra_secreta, letras_acertadas)
        else:
            tentativas -= 1
            desenhaForca(tentativas)

        enforcou = tentativas == 1;
        acertou = "_" not in letras_acertadas

    if (acertou):
        imprimeMensagemVencedor()
    else:
        imprimeMensagemPerdedor(palavra_secreta)


def imprimirBoasVindas():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


def carregarPalavraSecreta():
    palavras = []
    arquivo = open("palavras.txt", "r")
    for palavra in arquivo:
        palavras.append(palavra.strip())
    arquivo.close()
    aleatorio = random.randrange(0, (len(palavras) + 1))
    palavra_secreta = palavras[aleatorio].upper()
    return palavra_secreta


def carregarLetrasCorretas(palavra):
    return ["_" for letra in palavra]

def solicitaChute():
    return input("Qual letra? ").strip().upper()

def marcaChuteCorreto(chute, palavra, letras_corretas):
    posicao = 0
    for letra in palavra:
        if (letra == chute):
            letras_corretas[posicao] = chute
        posicao += 1
    print("Boa! Encontrei sua letra na palavra!")
    print(letras_corretas)

def imprimeMensagemPerdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprimeMensagemVencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenhaForca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()



