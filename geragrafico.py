from leitorarquivo import LeitorArquivo


def main():
    leitor = LeitorArquivo('dado.txt')
    valores = leitor.getValores()
    print(valores)


main()