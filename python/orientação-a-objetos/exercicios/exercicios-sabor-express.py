
#  o 'self' nas funções acima é usado para indicar que se refere ao restaurante que está requerindo a função, e não todos
#  não é necessário ser chamado de self. Apesar de ser o padrão do python, podemos usar qualquer nome, como 'this', por exemplo

# print(vars(restaurante_praca))
# print(vars(restaurante_pizza)

# .title() - serve para deixar a primeira letra maiúscula
# .upper() - deixa tudo maiúsculo
# _ torna o atributo privado, que não deve ser mexido


# # --------------------------------------------------------------------------------------------------------------------------------

# # Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
# restaurante_praca.categoria = 'Italiana'

# # --------------------------------------------------------------------------------------------------------------------------------

# # Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
# print(f'O nome do restaurante é {restaurante_praca.nome}.')

# # --------------------------------------------------------------------------------------------------------------------------------

# # Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
# if restaurante_praca.ativo:
#     print(f"O restaurante {restaurante_praca.nome} está ativo.")
# else:
#     print(f"O restaurante {restaurante_praca.nome} está inativo.")

# # --------------------------------------------------------------------------------------------------------------------------------

# # Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.

# categoria = Restaurante.categoria
# print(categoria)

# # --------------------------------------------------------------------------------------------------------------------------------

# # Altere o valor do atributo nome para 'Bistrô'.

# restaurante_praca.nome = 'Bistrô'

# # --------------------------------------------------------------------------------------------------------------------------------

# # Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

# restaurante_pizza = Restaurante()
# restaurante_pizza.nome = 'Pizza Place'
# restaurante_pizza.categoria = 'Fast Food'

# # --------------------------------------------------------------------------------------------------------------------------------

# # Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

# if restaurante_pizza.categoria == 'Fast Food':
#     print(f"A categoria do restaurante {restaurante_pizza.nome} é {restaurante_pizza.categoria}.")
# else:
#     print(f"A categoria do restaurante {restaurante_pizza.nome} não é Fast Food.")

# # --------------------------------------------------------------------------------------------------------------------------------

# # Mude o estado da instância restaurante_pizza para ativo.

# print(f"O restaurante {restaurante_pizza.nome} está {'ativo' if restaurante_pizza.ativo else 'inativo'}.")

# restaurante_pizza.ativo = not restaurante_pizza.ativo

# print(f"O restaurante {restaurante_pizza.nome} está {'ativo' if restaurante_pizza.ativo else 'inativo'}.")

# # --------------------------------------------------------------------------------------------------------------------------------

# # Imprima no console o nome e a categoria da instância restaurante_praca.

# print(f"Nome do restaurante: {restaurante_praca.nome} - Categoria: {restaurante_praca.categoria}")