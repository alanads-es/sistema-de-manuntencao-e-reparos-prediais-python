from classOrdemDeServico import OrdemDeServico
from pathlib import Path

"""def dirCreate():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)"""

def loadData():
    data = []

    archive = Path("ordensdeservico.txt")

    if not archive.is_file():
        return data
    
    archive = open("ordensdeservico.txt", "r", enconding = "utf-8")

    for line in archive:
        requisitante, telefone, descricao, dataOrdSer = line.strip().split(":")
        data.append(OrdemDeServico(requisitante, telefone, descricao, dataOrdSer))
    archive.close()

    return data

def saveData(data):
    archive = open("ordensdeservico.txt", "w", enconding = "utf-8")

    for ordem in data:
        archive.write(f"{ordem.StorageLine()}\n")
    archive.close()