from script_principal import cadastrar
from script_principal import mensagem
from script_principal import sair

def exibir_menu():
    while True:
        print("1-cadastrar")
        print("2-exibir frase")
        print("3-sair")

        opcao = int(input("digite sua opçao"))
        if opcao < 1:
            print('opçaõ invalida')
            return exibir_menu()
        elif opcao == 1:
            print("Voce selecionou a opção cadastrar")
            return cadastrar()
        elif opcao == 2:
            print("voce selecionou exibir frase")
            return mensagem()
        elif opcao == 3:
            print("voce selecionou sair")
            return sair()
        else:
            return exibir_menu()
escolha = print(exibir_menu())