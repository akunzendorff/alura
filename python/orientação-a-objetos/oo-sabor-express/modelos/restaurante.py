from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    #  Função construtor, define que um novo restaurante precisa ter nome e categoria
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False 
        self.avaliacao = []
        Restaurante.restaurantes.append(self) # adicionando este restaurante a lista de restaurantes da classe Restaurante 

    # Função que retorna o nome do restaurante
    def __srt__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria do restaurante'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status do restaurante'.ljust(25)}')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante._ativo}')
        
    @property
    def ativo(self):
        return 'ativo' if self.ativo else 'inativo'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append()
