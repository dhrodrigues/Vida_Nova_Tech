from Funcionario import *

lista_menu = ["\n 1 - CADASTRAR FUNCIONÁRIO", "2 - DADOS DO FUNCIONÁRIO", "0 - SAIR\n"]

while True:
    resposta = menu(lista_menu)
    if resposta == 1:
        print("Cadastrar funcionario\n")
        dados = funcionario()  
        lista_menu.insert(2, "3 - TRIBUTAÇÃO")
        
        
    elif resposta == 2:
        try:
            exbir_dados(dados)
            print()
        except NameError:
            exbir_dados()
    
    elif resposta == 3:
        
        desconto_salario(dados[3])
     
    elif resposta == 0:
        print("O sistema de cadastrado foi finalizado! \n Obrigado por utilizar nosso sistema")
        break
    else:
        print("Erro. Númerio invalido.")

        