#Desafio de Teste de Software Profº Wallece 

class Marvel_Viloes:
    def violoes (self, nome, poderes, perigo):
        self.nome = nome
        self. poderes = poderes
        self.perigo = perigo

    
    def get_nome (self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_poder(self):
        return self.__poderes

    def set_poder(self, poderes):
        self.__poderes = poderes

    def get_perigo(self):
        return self.__perigo

    def set_perigo(self, perigo):
        self.__perigo = perigo

    def fraquesa(self):
        for p in range(0, 5):
            self.__perigo = p


    def dominar_mundo():
        