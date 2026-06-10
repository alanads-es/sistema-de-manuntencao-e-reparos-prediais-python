from dataManager import loadData, saveData
from classOrdemDeServico import OrdemDeServico
from datetime import date
import re

def addOrdemDeServico(data):
    requisitante = input(str("Digite o nome do requisitante: ")).strip()
    telefone = input(str("Digite o telefone: ")).strip()
    descricao = input(str("Digite a descrição da ordem de serviço: ")).strip()
    dataOrdSer = input(date("Digite o nome do requisitante: ")).strip()

    standardPhoneNumber = r"(\d{2})(\d{4,5})(\d{4})"
    phoneNumberFormated = re.sub(standardPhoneNumber, r"(\1) \2-\3", telefone)

    if requisitante == "" or telefone == "" or descricao == "" or dataOrdSer == "":
        print("Requisitante, Telefone, Descrição e Data são campos obrigatórios. Digite novamente!")
        return
    
    data.append(OrdemDeServico(requisitante, telefone, descricao, dataOrdSer))