from classOrdemDeServico import OrdemDeServico
from pathlib import Path

def loadData():
    data = []

    archive = Path("ordensdeservico.txt")

    if not archive.is_file():
        open("ordensdeservico.txt", "w", encoding = "utf-8").close()
        return data
    
    archive = open("ordensdeservico.txt", "r", encoding = "utf-8")

    for line in archive:
        if line.strip() != "":
            requisitante, telefone, descricao, dataOrdSer = line.strip().split(":")
            data.append(OrdemDeServico(requisitante, telefone, descricao, dataOrdSer))
    archive.close()

    return data

def saveData(data):
    archive = open("ordensdeservico.txt", "w", encoding = "utf-8")

    for ordem in data:
        archive.write(f"{ordem.StorageLine()}\n")
    archive.close()