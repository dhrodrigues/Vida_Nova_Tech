# def player():
#     global pista
#     jogadas = int(input("\nInforme os pinos que deseja derrubar informe um numero de (1 á 10): "))
#     pista.pop(jogadas)

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


 

game =[]

for pino in game:
    posicao = map_pinos[pino]
    pista[posicao]=" "
mostrar_pista(pista)
# while True:
#     mostrar_pista(pista)

#     for i in range(0,10):
#         x =int(input("Informe numeros de 1 á 10 para vermos os pinos cairem!!:"))
#         posicao = map_pinos[i]
#         pista[posicao]= " "
#     for i in game:
#         if x == i:
#             print("Não tem esse pino broww!")
#         else:
#             game.append(x)
        
#     print(v)
    

# for pino, posicao in map_pinos.items():
#     posicao = map_pinos[pino]
#     pista[posicao]=pino
#     #   print(pino,posicao)
# mostrar_pista(pista)

# while True:
#     if "I" in pista:
#         mostrar_pista(pista)
#         player()
#     else:
#         print("Jogo encerrado")

