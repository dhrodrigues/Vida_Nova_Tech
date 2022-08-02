class Quitanda:

    def __init__(self):
        self.frutas = {
            "1": "Laranja",
            "2": "Melão",
            "3": "Kiwi"
        }
        self.precos = {
            "1": 3,
            "2": 8,
            "3": 15
        }
    
    def pergunta_fruta(self):
        print("Olá Cliente!!!\n Essas são as nossas frutas fresquinhas:")
        for cod in self.frutas:
            fruta = self.frutas[cod]
            print (f"{cod} - {fruta}")

        user_cod = input("Informe o numero da fruta que deseja:")
        user_fruta = self.frutas[user_cod]
        print(f"Você escolheu {user_fruta}")
    
    def quantidade (self):
        user_qtd = input(f"Quantas você deseja ?\n")
        return int(user_qtd)
    
    def calculadora (self,cod, qtd):
        preco_unit = self.precos[cod]
        preco_total = preco_unit * qtd
        return preco_total
    
    def pedido (self):
        cod = self.pergunta_fruta()
        qtd = self.quantidade()
        preco_total = self.calculadora (cod, qtd)
        print(f"Deu R$ {preco_total,},00")

teste = Quitanda()
teste.pedido()