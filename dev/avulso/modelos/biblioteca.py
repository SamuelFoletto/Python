from avaliacao import Avaliacao

class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome

    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Status'.ljust(25)} | {'Nota Média'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f'{biblioteca.nome.ljust(25)} | {biblioteca.ativo.ljust(25)} | {biblioteca.media_avaliacoes}')

    # SET
    def alterna_estado(self):
        self._ativo = not self._ativo

    #GET
    @property
    def ativo(self):
        if self._ativo:
            return 'Ativada'
        else:
            return 'Desativada'

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = soma / len(self._avaliacao)

        return f'{media:.2f}'