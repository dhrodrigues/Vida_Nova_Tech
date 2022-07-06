def mostrar_pista(pinos):
    for x in pista:
        print(x, end = '')
    print()

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

game = ["3","5","8"]

for pino in game:
    posicao = map_pinos[pino]
    pista[posicao]=" "
mostrar_pista(pista)