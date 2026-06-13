'''/options.py'''

from classOrdemDeServico import OrdemDeServico
from datetime import datetime
import re

'''Adiciona uma nova ordem de serviço após validar os dados informados pelo usuário'''
def addOrdemDeServico(data):

    '''Solicita os dados da ordem de serviço e remove espaços extras no início e no final'''
    requisitante = input("Digite o nome do requisitante: ").strip()
    telefone = input("Digite o telefone: ").strip()
    descricao = input("Digite a descrição da ordem de serviço: ").strip()
    dataOrdSer = input("Digite a data da ordem de serviço: ").strip()

    '''Verifica se os campos obrigatórios foram preenchidos'''
    if requisitante == "" or telefone == "" or descricao == "" or dataOrdSer == "":
        print("\nRequisitante, Telefone, Descrição e Data são campos obrigatórios. Digite novamente!\n")
        return

    '''Valida se a data está no formato DD/MM/AAAA e se representa uma data existente'''
    try:
        datetime.strptime(dataOrdSer, "%d/%m/%Y")
    except ValueError:
        print("\nFormato de data inválido ou data inválida. Utilize o formato DD/MM/AAAA\n")
        return

    '''Remove caracteres não numéricos do telefone'''
    clearPhoneNumber = re.sub(r"\D", "", telefone)

    '''Define o padrão esperado para o telefone'''
    standardPhoneNumber = r"(\d{2})(\d{4,5})(\d{4})"

    '''Verifica se o telefone possui formato válido'''
    if not re.match(f"^{standardPhoneNumber}$", clearPhoneNumber):
        print("\nTelefone inválido!\n")
        return
    
    '''Formata o telefone para o padrão (XX) XXXXX-XXXX'''
    phoneNumberFormated = re.sub(standardPhoneNumber, r"(\1) \2-\3", clearPhoneNumber)

    '''Cria e adiciona a nova ordem de serviço na lista'''
    data.append(OrdemDeServico(requisitante, phoneNumberFormated, descricao, dataOrdSer))
    print("\nOrdem de serviço cadastrada com sucesso.\n")


'''Exibe todas as ordens de serviço cadastradas'''
def viewOrdemDeServico(data):

    '''Verifica se existem registros cadastrados'''
    if len(data) == 0:
        print("\nNenhuma ordem de serviço cadastrada.\n")
        return

    '''Percorre e exibe cada ordem cadastrada'''
    for (pos, ordem) in enumerate(data):
        print(f"{pos + 1}. Requisitante: {ordem.requisitante}\t Telefone: {ordem.telefone}\t Descrição: {ordem.descricao}\t Data da ordem de serviço: {ordem.dataOrdSer}")


'''Remove uma ordem de serviço escolhida pelo usuário'''
def delOrdemDeServico(data):
    
    '''Verifica se existem registros cadastrados'''
    if len(data) == 0:
        print("\nNenhuma ordem de serviço cadastrada.\n")
        return
    
    '''Exibe as ordens cadastradas'''
    viewOrdemDeServico(data)

    '''Solicita a posição da ordem a ser removida, e verifica se um número inteiro foi inserido'''
    try:
        pos = int(input("Digite o número da posição da ordem de serviço a ser removida: "))
    except ValueError:
        print("\nA posição deve ser um número inteiro.\n")
        return

    '''Verifica se a posição informada existe'''
    if pos < 1 or pos > len(data):
        print("\nPosição inválida. Tente novamente.\n")
        return

    '''Remove a ordem selecionada da lista'''
    data.pop(pos - 1)
    print(f"\nOrdem de serviço da posição {pos} removida.\n")