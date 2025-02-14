# # 1 - Crie uma lista para cada informação a seguir:

# # Lista de números de 1 a 10;
# numeros = list(range(1,11))
# print(numeros)

# # Lista com quatro nomes;
# nomes = ['Ana', 'Marina', 'Julia', 'Fernanda']
# print(nomes)

# # Lista com o ano que você nasceu e o ano atual.
# from datetime import datetime
# datas = [datetime(2006, 10, 12), datetime(2025, 2, 14)]
# print(datas)

# # -----------------------------------------------------------------------------------------------

# # 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# frutas = ["maçã", "uva", "banana"]
# for fruta in frutas:
#     print(f"{fruta}")

# # -----------------------------------------------------------------------------------------------

# # 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# numeros = list(range(1, 11))
# for numero in numeros:
#     if numero % 2 == 0:
#         print(numero)

# # -----------------------------------------------------------------------------------------------

# # 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# numeros = list(range(1,11))

# for numero in reversed(numeros):
#     print(numero)

# # -----------------------------------------------------------------------------------------------

# # 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# numero = int(input("Digite um número: "))

# for i in range(1,11):
#     print(f"{numero} x {i} = {numero * i}")

# # -----------------------------------------------------------------------------------------------

# # 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# numeros = [1, 3, 5, 7, 9]
# soma = 0

# try:
#     for numero in numeros:
#         soma += numero
#         print(f"A soma dos números é: {soma}")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# # -----------------------------------------------------------------------------------------------

# # 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

# valores = [2, 50, 100, 200]
# soma = 0
# media = 0

# try:
#     if not valores:
#         raise ZeroDivisionError("A lista está vazia. Não é possível dividir.")

#     for valor in valores:
#         soma += valor

#     media = soma / len(valores)

#     print(f"A média dos números é {media}")

# except ZeroDivisionError as e:
#     print(f"Erro: {e}")
