from dev.avulso.modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca('Biblioteca da Cidade')

biblioteca_shopping = Biblioteca('Biblioteca da Shopping')



biblioteca_cidade.alterna_estado()
biblioteca_cidade.receber_avaliacao('Samuel', 10)
biblioteca_cidade.receber_avaliacao('Fernanda', 9.5)


def main():
    Biblioteca.listar_bibliotecas()

if __name__ == '__main__':
    main()