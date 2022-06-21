from turtle import title


dados_carta = ["nome", "logradouro", "numero","complemento","bairro","cep","cidade","estado"]
dados_usuario ={}

for dado in dados_carta:
    pergunta = "Por favor informe seu {}: ".format(dado)
    dados_usuario[dado] = input(pergunta)
    #print(dados_usuario)

traco_cep = dados_usuario['cep']
cep = '{}-{}'.format(traco_cep[:5], traco_cep[5:])
dados_usuario['cep'] = cep

carta = """
{nome}
{l}, {n} {c}
{b}
{cep} {cidade}/{uf}"""

print(carta.format(
    nome=dados_usuario['nome'].title(),
    l=dados_usuario['logradouro'].title(),
    n=dados_usuario['numero'],
    c=dados_usuario['complemento'].title(),
    b=dados_usuario['bairro'].title(),
    cep=dados_usuario['cep'],
    cidade=dados_usuario['cidade'].title(),
    uf=dados_usuario['estado'].upper()
))