from classOrdemDeServico import OrdemDeServico
from datetime import datetime
import re


def addOrdemDeServico(data):
    requisitante = input(str("Digite o nome do requisitante: ")).strip()
    telefone = input(str("Digite o telefone: ")).strip()
    descricao = input(str("Digite a descrição da ordem de serviço: ")).strip()
    dataOrdSer = input(("Digite a data da ordem de serviço: ")).strip()

    if requisitante == "" or telefone == "" or descricao == "" or dataOrdSer == "":
        print("\nRequisitante, Telefone, Descrição e Data são campos obrigatórios. Digite novamente!\n")
        return

    try:
        datetime.strptime(dataOrdSer, "%d/%m/%Y").date()
    except ValueError:
        print("\nFormato de data inválido ou data inválida. Utilize o formato DD/MM/AAAA\n")
        return

    clearPhoneNumber = re.sub(r"\D", "", telefone)
    standardPhoneNumber = r"(\d{2})(\d{4,5})(\d{4})"

    if not re.match(f"^{standardPhoneNumber}$", clearPhoneNumber):
        print("\nTelefone inválido!\n")
        return
    
    phoneNumberFormated = re.sub(standardPhoneNumber, r"(\1) \2-\3", clearPhoneNumber)

    data.append(OrdemDeServico(requisitante, phoneNumberFormated, descricao, dataOrdSer))


def viewOrdemDeServico(data):
    if len(data) == 0:
        print("Nenhuma ordem de serviço cadastrada.")
        return

    data.sort(key=lambda c: c.requisitante)
    for (pos, ordem) in enumerate(data):
        print(f"{pos + 1}. Requisitante: {ordem.requisitante}\t Telefone: {ordem.telefone}\t Descrição: {ordem.descricao}\t Data da ordem de serviço: {ordem.dataOrdSer}")


def delOrdemDeServico(data):
    viewOrdemDeServico(data)
    pos = int(input("Digite o número da posição da ordem de serviço a ser removida: "))
    if pos < 1 or pos > len(data):
        print("\nPosição inválida. Tente novamente.\n")
        return
    print(f"\nA ordem de chegada da posição {pos} foi removida.\n")
    data.pop(pos - 1)