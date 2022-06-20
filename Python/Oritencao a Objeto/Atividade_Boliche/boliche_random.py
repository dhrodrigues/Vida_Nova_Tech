import random

def mostrar_pista(pinos):
    for x in pista:
        print(x, end = '')
    print()

def 

pista = ['I', ' ', 'I', ' ', 'I', ' ', 'I', '\n', 
' ', 'I', ' ', 'I', ' ', 'I', ' ', '\n', 
' ', ' ', 'I', ' ', 'I', ' ', ' ', '\n', 
' ', ' ', ' ', 'I']

map_pinos = {
    "1": 27,
    "2": 18,
    "3": 20,
    "4": 9,
    "5": 11,
    "6": 13,
    "7": 0,
    "8": 2,
    "9": 4,
    "10": 6
}

game = [27, 18, 20, 9, 11, 13, 0, 2, 4, 6]

mostrar_pista(pista)

jogada_1 = input('\nDeseja jogar a bola? (s/n)? ')
print()
