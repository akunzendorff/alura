from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_risoto = Prato('Risoto', 40.0, 'O melhor risoto da cidade!')

bebida_agua = Bebida('Água', 5.0, 'pequena')
prato_lasanha = Prato('Lasanha', 60.0, 'A melhor lasanha da cidade!')

bebida_suco.aplicar_desconto()
bebida_agua.aplicar_desconto()

restaurante_praca.adicionar_item_ao_cardapio(bebida_suco)
restaurante_praca.adicionar_item_ao_cardapio(prato_risoto)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()