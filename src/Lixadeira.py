from Ferramenta import Ferramenta


class Lixadeira(Ferramenta):
    def __init__(self, nome, tensao, preco, potencia):
        Ferramenta.__init__(self, nome, tensao, preco)
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia

    def getInformacoes(self):
        super().getInformacoes()
        print("Potencia: " + str(self.__potencia))

    def cadastrar(self):
        pass
