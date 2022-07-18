#abertura do arquivo.
filename = "palavras.txt"

#leitura do arquivo
lista_palavras=[]
with open(filename, "r", encoding ="utf-8") as arquivo_poo:
    for linha in arquivo_poo:
        lista_palavras.append(linha.upper())

#Contagem de palavras do arquivo.
def quantidade_palavras(lista_palvras):
    return len(lista_palavras)

#Contagem quantas vezes cada letra aparece na lista
def contagem_letras ():
    lista_acumula={}

    for palavra in lista_palavras:
        lista_letras = list(palavra)
        for letra in lista_letras:
            if letra not in lista_acumula:
                lista_acumula [letra] =1
            else:
                lista_acumula[letra]+=1
    return lista_acumula

#Contagem quantas vezes aparece cada letra no inicio
def contagem_primeira ():
    lista_acumula={}

    for palavra in lista_palavras:
        if palavra[0] not in lista_acumula:
            lista_acumula [palavra[0]] =1
        else:
            lista_acumula[palavra[0]]+=1
    return lista_acumula

#Criação de Arquivo com as Três primeiras letras do meu nome
def cont_tres_nome(lista_palavras, inicia_nome):

    with open("Die.txt", "a") as f:
        for palavra in lista_palavras:
            if palavra[:3] == inicia_nome:
                f.write(palavra)

#Encontrar palavras que tenham a letra do meu nome
def palavras_nome(lista_palavras, nome):

    with open("Diego.txt", "a") as f:
        for palavra in lista_palavras:
            if nome in palavra:
                f.write(palavra)

 # Encontrar os palindromos
def palindromos(lista_palavras =[]):
    with open("palindromos.txt", "a") as f:
        for palavra in lista_palavras:
            if palavra == palavra[::-1]:
                    f.write(palavra)
              


palavri =quantidade_palavras(lista_palavras)
print (quantidade_palavras)