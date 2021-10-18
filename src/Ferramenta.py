class Ferramenta:
    def __init__(self, nome, tensao, preco):
        self.__nome = nome
        self.__tensao = tensao
        self.__preco = preco

    def getNome(self):
        return self.__nome

    def getTensao(self):
        return self.__tensao

    def getPreco(self):
        return self.__preco

    def getInformacoes(self):
        print("\nNome: " + str(self.__nome) + \
              "\nTensao: " + self.__tensao + \
              "\nPreço: " + self.__preco)

    def cadastrar(self):
        pass
