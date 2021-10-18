from Lixadeira import Lixadeira
from src.Furadeira import Furadeira

estoque = []


def mostramenu():
    print('''
 ________________________________
|     LOJA DE FERRAMENTAS        |
|     Menu                       |
|     0 - Sair                   |
|     1 - Cadastrar              |
 --------------------------------''')
    try:
        opcao = int(input("Escolha: "))
        return opcao
    except ValueError:
        print("Somente dígitos!")
        return mostramenu()


def cadastrar():

    result = tipoFerramenta()

    if result == 1:
        cadastrarLixadeira()
    elif result == 2:
        cadastrarFuradeira()
    else:
        print("Opcao invalida")
        cadastrar()


def tipoFerramenta():
    try:
        opcao = int(input("Que tipo de ferramenta deseja cadastrar? [1 Lixadeira/ 2 Furadeira]"))
        return opcao
    except ValueError:
        print("Somente dígitos!")
        return tipoFerramenta()


def cadastrarLixadeira():
    nome = input("Nome: ")
    tensao = input("Tensao:")
    preco = input("Preço:")
    potencia = input("Rotacoes: ")

    lixadeira = Furadeira(nome, tensao, preco, potencia)

    estoque.append(lixadeira)

    lixadeira.getInformacoes()


def cadastrarFuradeira():
    nome = input("Nome: ")
    tensao = input("Tensao:")
    preco = input("Preço:")
    rotacoes = input("Rotacoes")

    furadeira = Lixadeira(nome, tensao, preco, rotacoes)

    estoque.append(furadeira)

    furadeira.getInformacoes()


if __name__ == '__main__':
    while True:
        escolha = mostramenu()
        if escolha == 0:
            print("Obrigado! Volte Sempre!")
            break
        elif escolha == 1:
            cadastrar()
        else:
            print("Escolha uma opção válida do Menu.")
