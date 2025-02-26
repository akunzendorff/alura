from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_praca.receber_avaliacao('Ana', 10)
restaurante_praca.receber_avaliacao('Matilda', 8)
restaurante_praca.receber_avaliacao('Vinicius', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()