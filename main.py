from dataManager import loadData, saveData
from options import addOrdemDeServico, viewOrdemDeServico

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
        addOrdemDeServico(dados)
    elif opcao == 3:
        viewOrdemDeServico(dados)

    opcao = menu()