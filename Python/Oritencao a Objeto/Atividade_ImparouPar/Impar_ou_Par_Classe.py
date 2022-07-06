from random import randint

derota = "\U0001f62d"
victory = "\U0001f3c6"
victory2= "\U0001F601"
zueira= "\U0001F601"

def __init__(self,nome):
    self.nome = nome

def vitoria(escolha, resultado):
    """função que retorna 1 ou 0, dependendo do resultado da partida."""
    if escolha == resultado:
        print(f"{victory}{victory2} You is the Champions my friend {victory}{victory2}")
        return 0
    else:
        print(f"{derota}{derota}{derota}  DEROTA!!!!  {derota}{derota}{derota}{derota}{derota}")
        return 1

def game (self):

    print("""\tBora Jogar?\n Bem-Vindo ao decissão de impar ou par!!!\n""")


    jogada = input('Você quer par ou ímpar?: ').lower().strip()
    while 'impar' and 'par' not in jogada:
        escolha = input("\nPutsss você escolheu errado!!!!\nBora Digite Impar ou Par?  " ).lower().strip()
        jogada = escolha.upper

    while  True:
        print(f"Boa!!! você escolheu {jogada}")
        try:
            dedos =-1
            while dedos <0 or dedos >10:
                # print("Boa!!! você escolheu {}".format(jogada).upper())
                dedos = int(input(f"\nLemebre-se que sua mão tem apenas 10 dedos!!{zueira}\nDigite  um numero: "))
            break
        except ValueError:
            print("Ixiii sua mão não tem mais de 10 dedos.")

    maquina = randint (0,10)
    print(f"A máquina escolheu {maquina}, você escolheu {dedos}, Bora ver quem ganhou?\n")

    soma = maquina+dedos

    if soma % 2 == 0:
        print("\t PAR!!!!!\n")
        resultado = "par"
    else:
        print("\t IMPAR!!!!!\n")
        resultado = "impar"

vitoria(jogada, resultado)