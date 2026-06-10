from dataManager import loadData, saveData
from classOrdemDeServico import OrdemDeServico
from datetime import datetime
import re

data = loadData()

def addOrdemDeServico(data):
    requisitante = input(str("Digite o nome do requisitante: ")).strip()
    telefone = input(str("Digite o telefone: ")).strip()
    descricao = input(str("Digite a descrição da ordem de serviço: ")).strip()
    dataOrdSer = input(("Digite a data da ordem de serviço: ")).strip()

    try:
        dataObject = datetime.strptime(dataOrdSer, "%d/%m/%Y").date()
    except ValueError:
        print("Formato de data inválido ou data inválida. Utilize o formato DD/MM/AAAA")
        return

    clearPhoneNumber = re.sub(r"\D", "", telefone)
    standardPhoneNumber = r"(\d{2})(\d{4,5})(\d{4})"

    if re.match(f"^{standardPhoneNumber}$", clearPhoneNumber):
        phoneNumberFormated = re.sub(standardPhoneNumber, r"(\1) \2-\3", telefone)
        return phoneNumberFormated
    else:
        print("Telefone inválido. Preencha o input novamente!")

    if requisitante == "" or telefone == "" or descricao == "" or dataOrdSer == "":
        print("Requisitante, Telefone, Descrição e Data são campos obrigatórios. Digite novamente!")
        return
    
    data.append(OrdemDeServico)

def viewOrdemDeServico(data):
    if len(data) == 0:
        print("Nenhuma ordem de serviço cadastrada.")
        return

    data.sort(key=lambda c: c.requisitante)
    for (pos, ordem) in enumerate(data):
        print(f"{pos + 1}. {ordem.requisitante}\t{ordem.telefone}\t{ordem.descricao}\t{ordem.dataObject}")