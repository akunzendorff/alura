# class Musica:
#     nome = ''
#     artista = ''
#     duracao = int

# musica1 = Musica()
# musica1.nome = 'HUMBLE.'
# musica1.artista = 'Kendrick Lamar'
# musica1.duracao = '257'

# musica2 = Musica()
# musica2.nome = 'LOYALTY.FEAT.RIHANNA'
# musica2.artista = 'Kendrick Lamar'
# musica2.duracao = '347'

# musica3 = Musica()
# musica3.nome = 'Money Trees'
# musica3.artista = 'Kendrick Lamar'
# musica3.duracao = '626'

# # # refatoração da criação da classe Musica utiliando os métodos especiais do python

# class Musica:
#     def __init__(self, nome = '', artista = '', duracao = 0):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao

# musica1 = Musica(nome = 'HUMBLE.', artista = 'Kendrick Lamar', duracao = 257)
# musica2 = Musica(nome = 'LOYALTY.FEAT.RIHANNA', artista = 'Kendrick Lamar', duracao = 347)
# musica3 = Musica(nome = 'Money Trees', artista = 'Kendrick Lamar', duracao = 626)


# # Exercícios

# # Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

# class Carro:

#     def __init__(self, modelo = '', cor = '', ano = 0):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano

# carro1 = Carro(modelo = 'i30', cor = 'branco', ano = 2015)

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

# class Restaurante:
#     nome = ''
#     categoria = ''
#     capacidade = 0
#     avaliacao = 0
#     ativo = False

# restaurante1 = Restaurante()
# restaurante1.nome = 'Tr3s'
# restaurante1.categoria = 'Churrascaria'
# restaurante1.capacidade = 100
# restaurante1.avaliacao = 5
# restaurante1.ativo = True

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

# class Restaurante:

#     def __init__(self, nome = '', categoria = '', capacidade = 0, avaliacao = 0 , ativo = False):
#         self.nome = nome
#         self.categoria = categoria
#         self.capacidade = capacidade
#         self.avaliacao = avaliacao
#         self.ativo = ativo

# restaurante1 = Restaurante(nome = 'Tr3s', categoria = 'churrascaria', capacidade = 100, avaliacao = 5)

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

# class Restaurante:

#     def __init__(self, nome = '', categoria = '', capacidade = 0, avaliacao = 0 , ativo = False):
#         self.nome = nome
#         self.categoria = categoria
#         self.capacidade = capacidade
#         self.avaliacao = avaliacao
#         self.ativo = ativo

#     def __str__(self):
#         return f' Nome: {self.nome} | Categoria: {self.categoria} | Capacidade: {self.capacidade} | Avaliação: {self.avaliacao} | Status: {'ativo' if self.ativo else 'inativo'}'

# restaurante1 = Restaurante(nome = 'Tr3s', categoria = 'churrascaria')
    

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

# class Cliente:

#     def __init__(self, nome = '', idade = 0, endereco = '', telefone = ''):
#         self.nome = nome
#         self.idade = idade
#         self.endereco = endereco
#         self.telefone = telefone

# cliente1 = Cliente(nome= 'Ana Flávia', idade= 18, endereco= 'Rua das flores, 123', telefone= '13 999999999')
# cliente3 = Cliente(nome= 'Bárbara', idade= 35, endereco= 'Rua São Paulo, 11', telefone= '13 999999997')
# cliente4 = Cliente(nome= 'Laura', idade= 23, endereco= 'Rua Europa, 56', telefone= '13 999994599')

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #  Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

# class Pessoa:
     
#     def __init__(self, nome = '', idade = 0, profissao = ''):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao

#     def __str__(self):
#         return f'Nome: {self.nome} | Idade : {self.idade} anos | Profissão: {self.profissao}'
    
#     def aniversario(self):
#         self.idade += 1
#         return f'Feliz Aniversário! Agora você tem {self.idade} anos.'

#     @property 
#     def saudacao(self):
#         if self.profissao:
#             return f'Boas vindas, {self.profissao}!'
#         else:
#             return f'Boas vindas, {self.nome}'
    
# pessoa = Pessoa('Ana Flávia', 18, 'Estudante')

# print(pessoa)
# print(pessoa.saudacao)
# print(pessoa.aniversario())

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

# # class ContaBancaria():

# #     ativo = False

# #     def __init__(self, titular = '', saldo = 0):
# #         self.titular = titular
# #         self.saldo = saldo

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

# # class ContaBancaria():

# #     def __init__(self, titular = '', saldo = 0):
# #         self.titular = titular
# #         self.saldo = saldo
# #         self._ativo = False

# #     def __str__(self):
# #         return f'Titular: {self.titular} | Saldo: {self.saldo}'
    
# # conta1 = ContaBancaria('Ana Flávia', 1.200)
# # conta2 = ContaBancaria('Vinicius', 2.000)

# # print(conta1)
# # print(conta2)

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

# class ContaBancaria:

#     def __init__(self, titular = '', saldo = 0):
#         self.titular = titular
#         self.saldo = saldo
#         self._ativo = False
        
#     def __str__(self):
#         return f'Titular: {self.titular} | Saldo: {self.saldo}\n'
    
#     @classmethod
#     def ativar_conta(cls, conta):
#         conta.ativo = True

# conta3 = ContaBancaria('Matilda', 200)
# print(conta3._ativo)
# conta3.ativar_conta()
# print(f'{conta3._ativo}')
        
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

# class ContaBancariaPythonica:

#     def __init__(self, titular, saldo):
#         self._titular = titular
#         self._saldo = saldo
#         self._ativo = False

#     @property
#     def titular(self):
#         return self._titular
    
#     @property
#     def saldo(self):
#         return self._saldo
    
#     @property
#     def ativo(self):
#         return self._ativo

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Crie uma instância da classe e imprima o valor da propriedade titular.

# conta4 = ContaBancariaPythonica('Tereza', 100)
# print(f'Titular da conta 4: {conta4.titular}')

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

# class ClinteBanco:

#     def __init__(self, nome = '', idade = 0, endereco = '', cpf = '', profissao = '' ):
#         self.nome = nome
#         self.idade = idade
#         self.endereco = endereco
#         self.cpf = cpf
#         self.profissao = profissao

# cliente1 = ClinteBanco('Bárbara', 23, 'Rua 6', '345.567.789-12', 'Estudante')
# cliente2 = ClinteBanco('Laura', 24, 'Rua 4', '345.567.789-23', 'Estudante')
# cliente3 = ClinteBanco('Ana Julia', 28, 'Rua 9', '345.567.789-13', 'Estudante')



# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Crie um método de classe para a conta ClienteBanco.

# class ClienteBanco:

#     @classmethod
#     def criar_conta(cls, titular, saldo_inicial):
#         conta = ContaBancariaPythonica(titular, saldo_inicial)
#         return conta
    
# contacliente1 = ClienteBanco.criar_conta('Ana Flávia', 2000)
# print(f'Conta de {contacliente1.titular} criada com saldo inicial de R${contacliente1.saldo_inicial}')

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

# class Livro:

#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

#     def __str__(self):
#         return f'Título: {self.titulo.ljust(20)} | Autor: {self.autor.ljust(20)} | Ano de publicação: {self.ano_publicacao}'
    
# livro1 = Livro('A Seleção', 'Kiera Cass', 2012)
# livro2 = Livro('A Elite', 'Kiera Cass', 2013)

# print(livro1)
# print(livro2)

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

# class Livro:

#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#     def __str__(self):
#         return f'Título: {self.titulo.ljust(20)} | Autor: {self.autor.ljust(20)} | Ano de publicação: {self.ano_publicacao}'

#     def emprestar(self):
#         self.disponivel = False

# livro3 = Livro('A Escolha', 'Kiera Cass', 2014)
# livro3.emprestar()
# print(livro3.disponivel)

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

# class Livro:

#     livros = []

#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#     def __str__(self):
#         return f'Título: {self.titulo.ljust(20)} | Autor: {self.autor.ljust(20)} | Ano de publicação: {self.ano_publicacao}'

#     def emprestar(self):
#         self.disponivel = False

#     @staticmethod
#     def verificar_disponibilidade(ano):
#         livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
#         return livros_disponiveis
    
# livro1 = Livro('A Seleção', 'Kiera Cass', 2012)
# livro2 = Livro('A Elite', 'Kiera Cass', 2013)
# livro3 = Livro('A Escolha', 'Kiera Cass', 2014)

# Livro.livros = [livro1, livro2, livro3]

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# from exercicios import Livro

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

# livro_biblioteca = Livro('A Seleção', 'Kiera Cass', 2012)
# print(f'Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}')
# livro_biblioteca.emprestar()
# print(f'Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}')

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

# ano_especifico = 2020
# livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
# print(f'Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}')

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

# from exercicios import Livro

# livro_main1 = Livro('A Seleção', 'Kiera Cass', 2012)
# livro_main2 = Livro('A Elite', 'Kiera Cass', 2013)

# print(livro_main1)
# print(livro_main2)

# # Com base no que vimos nessa aula sobre herança, crie uma classe Banco com dois atributos: nome e endereco. Em seguida, derive uma classe chamada Agencia que herda os atributos da classe Banco e inclua um atributo adicional chamado numero. Ambas as classes devem ter apenas o construtor.

# class Banco:
#   def __init__(self, nome, endereco):
#     self._nome = nome
#     self._endereco = endereco

# # from banco import Banco
 
# class Agencia(Banco):
#   def __init__(self, nome, endereco, numero):
#     super().__init__(nome, endereco)
#     self._numero = numero
