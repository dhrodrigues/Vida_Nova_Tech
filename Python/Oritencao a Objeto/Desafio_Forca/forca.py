from getpass import getpass
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_perdedor(palavra_inicial):
    print("\nPuxa, você foi enforcado!\n")
    print("\nA palavra é {}\n".format(palavra_inicial))
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

def imprime_mensagem_vencedor():
    print("\nParabéns, você ganhou!")
    print("\nA palavra era {}\n".format(palavra_inicial))
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


palavra_inicial=getpass ("Informe a plavra da forca: ")

max_palpites = 7
erros = 0
acerto = False
letras_usadas = []

is_valid=palavra_inicial.isalpha()
if not is_valid:
    print("Essa palavra não contém apenas letras. É Invalida")
    exit()

palavra_inicial = palavra_inicial.strip().upper()

while erros < max_palpites and not acerto:
    # total_caracteres = len(palavra_inicial)
    for letra in palavra_inicial:
        if letra in letras_usadas:
            print(letra, end=" ")
        else:
            print("_", end= " ")
    print()

    palpilte = input("Digite uma letra: ")
    palavra_valido=palpilte.isalpha() and len(palpilte) == 1

    while not palavra_valido:
        palpilte = input("Digite outra letra, pense bem hein: ")
        palavra_valido=palpilte.isalpha() and len(palpilte) == 1

    palpilte=palpilte.upper()

    if palpilte in letras_usadas:
        print("Não pode repitir a letra fera!!")
    else:
        letras_usadas.append(palpilte)


    if palpilte in palavra_inicial:
        # print("Boa!")
        pontos = 0
        for letra in palavra_inicial:
            if letra in letras_usadas:
                pontos = pontos+1
        if pontos == len(palavra_inicial):
            acerto = True
            imprime_mensagem_vencedor()
    else:
        #print("patssss!!!")
        erros = erros+1
        desenha_forca(erros)
        if erros == 7:
            enforcou = erros == 7
            imprime_mensagem_perdedor(palavra_inicial)

print("\n\tFINAL DE JOGO!!!!!!!!!!")

        
