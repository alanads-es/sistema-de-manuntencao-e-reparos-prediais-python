from dataManager import loadData, saveData
from options import addOrdemDeServico

def menu():
    print("Sistema de Manuntenção e Reparos Prediais")
    print("[1] Adicionar ordem de serviço")
    print("[2] Remover a ordem de serviço")
    print("[3] Listar as ordens de serviço")
    print("[4] Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao >= 1 and opcao <= 4:
        return opcao
    else:
        print("Opção indisponível, escolha uma opção entre 1 e 5!")
        return menu()


opcao = menu()

dados = loadData()

while menu != 4:
    if opcao == 1:
        dados = addOrdemDeServico()
    """elif opcao == 2:
        delOrdemDeServico(dados)
    elif opcao == 3:
        listarOrdemDeServico(dados)"""

    opcao = menu()