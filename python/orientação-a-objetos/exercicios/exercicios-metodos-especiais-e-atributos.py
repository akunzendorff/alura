# Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
# No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
# Crie uma nova classe chamada Carro que herda da classe Veiculo.
# No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
# Em um arquivo chamado main.py, importe a classe Carro.
# No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.

from abc import ABC, abstractmethod

class Veiculo(ABC):

    veiculos = []

    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    def __str__(self):
        return f'{self._marca} {self._modelo}'

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def adicionar_veiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            Veiculo.veiculos.append(veiculo)

# --------------------------------------------------------------------------------------------------------------------------------

class Carro(Veiculo):

    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor

    def __str__(self):
        return f'{super().__str__()}{self._cor}'

    def ligar(self):
        print(f'O carro {self._modelo} está ligado')

    def adicionar_veiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            Veiculo.veiculos.append(veiculo)

# --------------------------------------------------------------------------------------------------------------------------------

# from modelos.veiculo import Veiculo

carro_hb20 = Carro('Hyundai', 'HB20 Sedan', 'Preto')
carro_i30 = Carro('Hyundai', 'i30', 'Branco')
carro_civic = Carro('Honda', 'Civic', 'Preto')

carro_hb20.adicionar_veiculo(carro_hb20)
carro_i30.adicionar_veiculo(carro_i30)
carro_civic.adicionar_veiculo(carro_civic)

for i, veiculo in enumerate(Veiculo.veiculos,  start = 1):
    print(f'Carro {i}: \nMarca: {veiculo._marca} | Modelo: {veiculo._modelo} | Cor: {veiculo._cor}')