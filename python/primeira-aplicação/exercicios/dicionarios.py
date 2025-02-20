# # Exercícios

# # 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

# dados_pessoa = {'nome': 'Ana Flávia', 'idade': 18, 'cidade': 'Registro'}
# print(dados_pessoa)

# # -----------------------------------------------------------------------------------------------

# # 2 - Utilizando o dicionário criado no item 1:

# # Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);

# dados_pessoa['idade'] = 19
# print(dados_pessoa)

# # Adicione um campo de profissão para essa pessoa;

# dados_pessoa['profissão'] = 'Estudante'
# print(dados_pessoa)

# # Remova um item do dicionário.

# del dados_pessoa['cidade']
# print(dados_pessoa)

# # -----------------------------------------------------------------------------------------------

# # 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

# quadrados = {num: num ** 2 for num in range(1,6)}
# print(quadrados)

# # -----------------------------------------------------------------------------------------------

# # 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# gatos = [{'nome': 'matilda', 'raça': 'siamês', 'idade': 4}, {'nome': 'tereza', 'raça': 'tricolor', 'idade': 0}]

# chave_verificar = 'idade'

# for i, gato in enumerate(gatos):
#     if chave_verificar in gato:
#         print(f'A chave {chave_verificar} existe no dicionário do gato {i+1}')
#     else:
#         print(f'A chave {chave_verificar} não existe no dicionário do gato {i+1}')

# # -----------------------------------------------------------------------------------------------

# # 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

# frase = input("Digite uma frase: ")

# palavras = frase.lower().split()

# frequencia_palavras = {}

# for palavra in palavras:
#     frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1

# print("Frequência das palavras na frase:")
# for palavra, frequencia in frequencia_palavras.items():
#     print(f"{palavra}: {frequencia}")
