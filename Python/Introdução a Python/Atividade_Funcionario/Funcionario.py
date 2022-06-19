def verifica_menu(texto):

    """Realiza a verirficação da opção selecionada no menu """

    while True:
        try:
            txt = int(input(texto))
        except (ValueError, TypeError):
            print("Por favor digite apenas números válidos.")
        except (KeyboardInterrupt):
            print("Nenhum número foi digitado")
            return 0
        else:
            return txt

def exbir_dados(func = ["Sem dados", "Sem dados", "Sem dados", "Sem dados"]):
    
    """Retorna os dados do funcionario cadastrado"""

    print()
    print("\tNome: ", func[0])
    print("\tSobrenome: ", func[1])
    print("\tCargo: ", func[2])
    print("\tSalário: R$", func[3])
    print()

def salario(salarioFuncionario = 0.0):
    
    while True:
        try:
            salarioFuncionario = float(input("Digite o salário do funcionario cadastrado: "))
                      
        except ValueError:
            print("Por favor utilize apenas números!")
        else:
            return salarioFuncionario

def funcionario(nome= "Nome",sobrenome = "Sobrenome",cargo = "Cargo",salarioFuncionario = "salario"):

    "Cadastro do funcionario"   

    nome = input("Qual o nome do funcionário?\n").title().strip(),
    sobrenome = input("Qual o sobrenome do funcionário?\n").title().strip(),
    cargo =input("Qual o cargo que o funcionário ocupará?\n").title().strip()
    salarioFuncionario =salario()

    lista_dados = []
    lista_dados.extend(nome)
    lista_dados.extend(sobrenome)
    lista_dados.append(cargo)
    lista_dados.append(salarioFuncionario)
    return lista_dados

def desconto_salario(salario_bruto = 0.0):
    """Calcula o valor a ser descontado para o imposto de renda de acordo com a faixa salarial do funcionario cadastrado"""
    
    porcentagens = [0, 0.075, 0.15, 0.225, 0.275]
    if salario_bruto <= 1903.98:
        desconto = porcentagens[0]
    elif salario_bruto > 1903.98 and salario_bruto <= 2826.65:
        desconto = porcentagens[1]
    elif salario_bruto > 2826.65 and salario_bruto <= 3751.05:
        desconto = porcentagens[2]
    elif salario_bruto > 3751.05 and salario_bruto <= 4664.68:
        desconto = porcentagens[3]
    else:
        desconto = porcentagens[4]

    "Calculo d"

    desconto_porcentagem = desconto * 100
    liquido = salario_bruto - (salario_bruto * desconto)
    print(f"\nFoi deduzido {desconto_porcentagem:.2f}% de R${salario_bruto} ")
    print(f"\nO salário liquido será de {liquido}")
    print()


def menu(lista):
    x = 1
    for item in lista:
        print(f" {item}")
        x += 1
    opcao = verifica_menu("Escolha uma opção: ")
    return opcao

#def informacoesFuncionario(self):
#   print('Olá, %s %s!\nSeu cargo é: %s \n Seu salario é: %s' %(nome, sobrenome, cargo, salario))



#Teste = Funcionario(input("Digite Nome:"),input("Digite Sobrenome:"),input("Digite Cargo:"),input("Digite Salario:"))

#print(Teste.funcionario_list())

