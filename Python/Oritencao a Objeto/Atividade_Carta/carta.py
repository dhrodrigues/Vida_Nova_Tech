dados_carta = ["nome", "logradouro", "numero","complemento","bairro","cep","cidade","estado"]
dados_usuario ={}

for dado in dados_carta:
    pergunta = "Por favor informe seu {}: ".format(dado).title()
    dados_usuario[dado] = input(pergunta)
    #print(dados_usuario)

traco_cep = dados_usuario['cep']
cep = '{}-{}'.format(traco_cep[:5], traco_cep[5:])
dados_usuario['cep'] = cep

carta = """
{}
{}, {} {}
{}
{} {}/{}"""

print(carta.format(
    dados_usuario['nome'],
    dados_usuario['logradouro'],
    dados_usuario['numero'],
    dados_usuario['complemento'],
    dados_usuario['bairro'],
    dados_usuario['cep'],
    dados_usuario['cidade'],
    dados_usuario['estado']
))