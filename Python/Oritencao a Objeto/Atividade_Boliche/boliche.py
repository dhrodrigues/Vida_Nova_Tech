def player():
    global pista
    jogadas = int(input("\nInforme os pinos que deseja derrubar informe um numero de (1 á 10): "))
    pista.pop(jogadas)

def mostrar_pista(pinos):
    for x in pista:
        print(x, end = '')
print()

pista = ["I"," ","I"," ","I"," ","I","\n",
" ","I"," ","I"," ","I"," ","\n",
" "," ","I"," ","I"," "," ","\n",
" "," "," ","I"," "," "," ","\n"
]

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


 

# game =["2","1"]

# for pino in game:
#     posicao = map_pinos[pino]
#     pista[posicao]=" "
# mostrar_pista(pista)


# for pino in map_pinos:
#     posicao = map_pinos[pino]
#     pista[posicao]=pino
# mostrar_pista(pista)
game=[]

while True:
    if game in pista:
        mostrar_pista(pista)
        player()
    else:
        print("Jogo encerrado")

