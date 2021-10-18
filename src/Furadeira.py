from Ferramenta import Ferramenta


class Furadeira(Ferramenta):
    def __init__(self, nome, tensao, preco, rotacoes):
        Ferramenta.__init__(self, nome, tensao, preco)
        self._rotacoes = rotacoes

    def getRotacoes(self):
        return self._rotacoes

    def getInformacoes(self):
        super().getInformacoes()
        print("Rotacoes: " + str(self._rotacoes))

    def cadastrar(self):
        pass
