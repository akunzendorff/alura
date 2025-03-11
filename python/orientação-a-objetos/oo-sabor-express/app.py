from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_risoto = Prato('Risoto', 40.0, 'O melhor risoto da cidade!')

def main():
    pass

if __name__ == '__main__':
    main()