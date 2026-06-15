'''/options.py'''

from classOrdemDeServico import OrdemDeServico
from datetime import datetime
import re
from classCor import Cor

'''Adiciona uma nova ordem de serviço após validar os dados informados pelo usuário'''
def addOrdemDeServico():

    '''Solicita os dados da ordem de serviço e remove espaços extras no início e no final'''
    requisitante = input("Digite o nome do requisitante: ").strip()
    telefone = input("Digite o telefone: ").strip()
    descricao = input("Digite a descrição da ordem de serviço: ").strip()
    dataOrdSer = input("Digite a data da ordem de serviço: ").strip()

    '''Verifica se os campos obrigatórios foram preenchidos'''
    if requisitante == "" or telefone == "" or descricao == "" or dataOrdSer == "":
        print(f"\n{Cor.AVISO}⚠️ Requisitante, Telefone, Descrição e Data são campos obrigatórios. Digite novamente!{Cor.RESET}\n")
        return

    '''Valida se a data está no formato DD/MM/AAAA e se representa uma data existente'''
    try:
        datetime.strptime(dataOrdSer, "%d/%m/%Y")
    except ValueError:
        print(f"\n{Cor.ERRO}❌ Formato de data inválido ou data inválida. Utilize o formato DD/MM/AAAA{Cor.RESET}\n")
        return

    '''Remove caracteres não numéricos do telefone'''
    clearPhoneNumber = re.sub(r"\D", "", telefone)

    '''Define o padrão esperado para o telefone'''
    standardPhoneNumber = r"(\d{2})(\d{4,5})(\d{4})"

    '''Verifica se o telefone possui formato válido'''
    if not re.match(f"^{standardPhoneNumber}$", clearPhoneNumber):
        print(f"\n{Cor.ERRO}❌ Telefone inválido!{Cor.RESET}\n")
        return
    
    '''Formata o telefone para o padrão (XX) XXXXX-XXXX'''
    phoneNumberFormated = re.sub(standardPhoneNumber, r"(\1) \2-\3", clearPhoneNumber)
    return requisitante, phoneNumberFormated, descricao, dataOrdSer

def novaOrdemDeServico(data):

    dados = addOrdemDeServico()

    if dados is None:
        return

    requisitante, phoneNumberFormated, descricao, dataOrdSer = dados
    '''Gera um identificador único para a nova ordem de serviço'''
    if len(data) == 0:
        idOrdem = 1
    else:
        idOrdem = data[-1].idOrdem + 1

    '''Cria a ordem de serviço com seu identificador e adiciona na lista'''
    data.append(OrdemDeServico(idOrdem, requisitante, phoneNumberFormated, descricao, dataOrdSer))
    print(f"\n{Cor.SUCESSO}✅ Ordem de serviço cadastrada com sucesso.{Cor.RESET}\n")

def editOrdemDeServico(data):
    '''Verifica se existem registros cadastrados'''
    if len(data) == 0:
        print(f"\n{Cor.AVISO}⚠️ Nenhuma ordem de serviço cadastrada.{Cor.RESET}\n")
        return

    '''Exibe as ordens cadastradas'''
    viewOrdemDeServico(data)

    '''Solicita o ID da ordem a ser editada'''
    try:
        idOrdem = int(input("\nDigite o ID da ordem de serviço a ser editada: "))
    except ValueError:
        print(f"\n{Cor.ERRO}❌ O ID deve ser um número inteiro.{Cor.RESET}\n")
        return

    '''Procura a ordem correspondente ao ID informado'''
    for ordem in data:

        '''Verifica se encontrou a ordem'''
        if ordem.idOrdem == idOrdem:

            dados = addOrdemDeServico()

            if dados is None:
                return

            requisitante, phoneNumberFormated, descricao, dataOrdSer = dados

            '''Atualiza os dados da ordem'''
            ordem.requisitante = requisitante
            ordem.telefone = phoneNumberFormated
            ordem.descricao = descricao
            ordem.dataOrdSer = dataOrdSer

            print(f"\n{Cor.SUCESSO}✅ Ordem de serviço de ID {idOrdem} atualizada.{Cor.RESET}\n")
            return

    '''Executado caso o ID não exista'''
    print(f"\n{Cor.ERRO}❌ ID não encontrado.{Cor.RESET}\n")


'''Exibe todas as ordens de serviço cadastradas'''
def viewOrdemDeServico(data):

    '''Verifica se existem registros cadastrados'''
    if len(data) == 0:
        print(f"\n{Cor.AVISO}⚠️ Nenhuma ordem de serviço cadastrada.{Cor.RESET}\n")
        return

    '''Percorre e exibe cada ordem cadastrada'''
    for ordem in data:
        print(f"{Cor.TITULO}📋 {ordem.idOrdem}.{Cor.RESET} Requisitante: {ordem.requisitante}\t Telefone: {ordem.telefone}\t Descrição: {ordem.descricao}\t Data da ordem de serviço: {ordem.dataOrdSer}")

'''Remove uma ordem de serviço escolhida pelo usuário'''
def delOrdemDeServico(data):
    
    '''Verifica se existem registros cadastrados'''
    if len(data) == 0:
        print(f"\n{Cor.AVISO}⚠️ Nenhuma ordem de serviço cadastrada.{Cor.RESET}\n")
        return
    
    '''Exibe as ordens cadastradas'''
    viewOrdemDeServico(data)

    '''Solicita o ID da ordem a ser removida, e verifica se o ID informado no input é um número inteiro'''
    try:
        idOrdem = int(input("\nDigite o ID da ordem de serviço a ser removida: "))
    except ValueError:
        print(f"\n{Cor.ERRO}❌ O ID deve ser um número inteiro.{Cor.RESET}\n")
        return

    '''Procura a ordem correspondente ao ID informado'''
    for ordem in data:

        '''Verifica se o ID da ordem atual corresponde ao ID informado'''
        if ordem.idOrdem == idOrdem:

            '''Remove a ordem de serviço encontrada da lista'''
            data.remove(ordem)
            print(f"\n{Cor.SUCESSO}✅ Ordem de serviço de ID {idOrdem} removida.{Cor.RESET}\n")
            return

    '''Executado caso nenhuma ordem com o ID informado seja encontrada'''
    print(f"\n{Cor.ERRO}❌ ID não encontrado.{Cor.RESET}\n")