'''/main.py'''

from dataManager import loadData, saveData
from options import novaOrdemDeServico, viewOrdemDeServico, delOrdemDeServico, editOrdemDeServico
from classCor import Cor

'''A seção da função menu exibe o menu principal,
valida a entrada do usuário e retorna uma opção válida entre 1 e 5
além de que caso a entrada seja inválida, o menu é solicitado novamente'''
def menu():
    opcao = ""
    while opcao not in ("1", "2", "3", "4", "5"):
        print(f"""{Cor.TITULO}

███████╗███╗   ███╗██████╗ ██████╗
██╔════╝████╗ ████║██╔══██╗██╔══██╗
███████╗██╔████╔██║██████╔╝██████╔╝
╚════██║██║╚██╔╝██║██╔══██╗██╔═══╝
███████║██║ ╚═╝ ██║██║  ██║██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝

Sistema de Manutenção e Reparos Prediais

{Cor.RESET}""")
        print("➕ [1] Adicionar ordem de serviço")
        print("🗑️ [2] Remover a ordem de serviço")
        print("✏️ [3] Editar ordem de serviço")
        print("📋 [4] Listar as ordens de serviço")
        print("🚪 [5] Sair")
        print(Cor.RESET, end="")

        opcao = input("Digite uma opção: ")

        if opcao not in ("1", "2", "3", "4", "5"):
            print(f"\n{Cor.AVISO}⚠️ Opção indisponível, escolha uma opção entre 1 e 5!{Cor.RESET}\n")

    return opcao


'''Obtém a opção escolhida pelo usuário'''
opcao = menu()
'''Carrega os dados armazenados no sistema'''
dataBase = loadData()

'''Mantém o programa em execução até que o usuário escolha sair, 
executando a funcionalidade correspondente à opção escolhida'''
while opcao != "5":
    if opcao == "1":
        novaOrdemDeServico(dataBase)
    elif opcao == "2":
        delOrdemDeServico(dataBase)
    elif opcao == "3":
        editOrdemDeServico(dataBase)
    elif opcao == "4":
        viewOrdemDeServico(dataBase)

    '''Salva as alterações realizadas no arquivo de dados a cada iteração'''
    saveData(dataBase)
    '''Solicita uma nova opção ao usuário'''
    opcao = menu()
print(f"\n{Cor.TITULO}👋 Sistema encerrado!{Cor.RESET}")
