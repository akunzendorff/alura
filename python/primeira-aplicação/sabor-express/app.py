import os

restaurantes = [{"nome": "SushiGrill", "categoria": "Sushi", "ativo": False}, {"nome": "PPizzas", "categoria": "Pizzaria", "ativo": True}]

def exibir_nome_do_programa():
    print("sabor express")

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Finalizando o app.')

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal

    '''
    print("Opção Inválida!")
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal

    '''
    input("\nDigite uma tecla para voltar para o menu inicial: ")
    main()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 

     Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Essa função é responsável por listar os restaurantes 

    Outputs:
    - Exibe a lista de restaurantes na tela

    '''
    exibir_subtitulo("Listando os restaurantes.")

    print(f"{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alterar_status_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação

    '''
    exibir_subtitulo("Alterar o status do restaurante.")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o status: ").strip().lower()
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante["nome"].strip().lower() == nome_restaurante:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = (f"O status do restaurante {nome_restaurante} foi alterado com sucesso!")
            print(mensagem)

    if not restaurante_encontrado:
        print(f"O restaurante {nome_restaurante} não foi encontrado...")

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário

    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
            return False
    except: 
        opcao_invalida()

    return True

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

