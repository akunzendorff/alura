class Avaliacao:

    def __init__(self, cliente, nota):
        self.cliente = cliente
        self.nota = nota


    @property #torna capaz ler as informações
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media