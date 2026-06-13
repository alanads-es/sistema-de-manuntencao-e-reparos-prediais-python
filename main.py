'''/main.py'''

from dataManager import loadData, saveData
from options import addOrdemDeServico, viewOrdemDeServico, delOrdemDeServico

'''A seção da função menu exibe o menu principal,
valida a entrada do usuário e retorna uma opção válida entre 1 e 4
além de que caso a entrada seja inválida, o menu é solicitado novamente'''
def menu():
    opcao = ""
    while opcao not in ("1", "2", "3", "4"):
        print("\n=========================================")
        print("\nSistema de Manutenção e Reparos Prediais\n")
        print("=========================================\n")
        print("[1] Adicionar ordem de serviço")
        print("[2] Remover a ordem de serviço")
        print("[3] Listar as ordens de serviço")
        print("[4] Sair")
        opcao = input("Digite uma opção: ")

        if opcao not in ("1", "2", "3", "4"):
            print("\nOpção indisponível, escolha uma opção entre 1 e 4!\n")
    return opcao


'''Obtém a opção escolhida pelo usuário'''
opcao = menu()
'''Carrega os dados armazenados no sistema'''
dataBase = loadData()

'''Mantém o programa em execução até que o usuário escolha sair, 
executando a funcionalidade correspondente à opção escolhida'''
while opcao != "4":
    if opcao == "1":
        addOrdemDeServico(dataBase)
    elif opcao == "2":
        delOrdemDeServico(dataBase)
    elif opcao == "3":
        viewOrdemDeServico(dataBase)

    '''Salva as alterações realizadas no arquivo de dados a cada iteração'''
    saveData(dataBase)
    '''Solicita uma nova opção ao usuário'''
    opcao = menu()
print("\nSistema encerrado!")
