
# # 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

# numero = int(input("Digite um número: "))

# if(numero % 2 == 0):
#     print("O número escolhido é par.")
# else:
#     print("O número escolhido é ímpar.")

# match numero:
#     case numero if numero % 2 == 0:
#         print("O número escolhido é par.")
#     case _:
#         print("O número escolhido é ímpar.")

# # --------------------------------------------------------------------------------------------------

# # 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# # Criança: 0 a 12 anos;
# # Adolescente: 13 a 18 anos;
# # Adulto: acima de 18 anos.

# idade = int(input("Digite sua idade: "))

# if(0 < idade <= 12):
#     print(f"Você tem {idade} anos, e é uma criança.")
# elif(12 < idade < 18):
#     print(f"Você tem {idade} anos, e é um adolescente.")
# elif(idade >= 18):
#     print(f"Você tem {idade} anos, e é um adulto.")
# else:
#     print("Valor inválido. Tente novamente!")

# match idade:
#     case idade if 0 <= idade <= 12:
#         print(f"Você tem {idade} anos, e é uma criança.")
#     case idade if 12 < idade < 18:
#         print(f"Você tem {idade} anos, e é um adolescente.")
#     case idade if idade >= 18:
#         print(f"Você tem {idade} anos, e é um adulto.")
#     case _:
#         print("Valor inválido. Tente novamente!")



# # --------------------------------------------------------------------------------------------------

# # 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

# nome_def = "Ana Flávia"
# senha_def = "alura123"

# nome = input("Digite seu nome: ")
# senha = input("Digite sua senha: ")

# if nome == nome_def and senha == senha_def:
#     print(f"Seja bem-vinda, {nome}!")
# else:
#     print("Usuário ou senha incorretos. Tente novamente!")

# match (nome, senha):
#     case (nome_def, senha_def):
#         print(f"Seja bem-vinda, {nome}!")
#     case _:
#         print("Usuário ou senha incorretos. Tente novamente!")

# # --------------------------------------------------------------------------------------------------

# # 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# # Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# # Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# # Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# # Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# # Caso contrário: o ponto está localizado no eixo ou origem.

# x = int(input("Digite a primeira coordenada: "))
# y = int(input("Digite a segunda coordenada: "))

# if x > 0 and y > 0 :
#     print("As coordenadas se encontram no primeiro quadrante!")
# elif x < 0 and y > 0 :
#     print("As coordenadas se encontram no segundo quadrante!")
# elif x < 0 and y < 0 :
#     print("As coordenadas se encontram no terceiro quadrante!")
# elif x > 0 and y < 0 :
#     print("As coordenadas se encontram no quarto quadrante!")
# else:
#     print("O ponto está localizado no eixo ou origem.")

# match (x, y):
#     case x,y if x > 0 and y > 0:
#         print("As coordenadas se encontram no primeiro quadrante!")
#     case x,y if x < 0 and y > 0:
#         print("As coordenadas se encontram no segundo quadrante!")
#     case x,y if x < 0 and y < 0:
#         print("As coordenadas se encontram no terceiro quadrante!")
#     case _:
#         print("O ponto está localizado no eixo ou origem.")

# # --------------------------------------------------------------------------------------------------