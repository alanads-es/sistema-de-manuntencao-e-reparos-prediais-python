'''/dataManager.py'''

from classOrdemDeServico import OrdemDeServico
from pathlib import Path

'''Carrega as ordens de serviço armazenadas no arquivo'''
def loadData():

    '''Lista que armazenará as ordens carregadas'''
    data = []

    '''Cria uma referência para o arquivo de armazenamento'''
    archive = Path("ordensdeservico.txt")

    '''Verifica se o arquivo existe'''
    if not archive.is_file():

        '''Cria o arquivo caso ele não exista'''
        open("ordensdeservico.txt", "w", encoding = "utf-8").close()
        return data
    
    '''Abre o arquivo para leitura'''
    archive = open("ordensdeservico.txt", "r", encoding = "utf-8")

    '''Lê cada linha armazenada no arquivo'''
    for line in archive:

        '''Ignora linhas vazias'''
        if line.strip() != "":

            '''Separa o identificador e os demais dados da ordem de serviço'''
            idOrdem, requisitante, telefone, descricao, dataOrdSer = line.strip().split(":")

            '''Cria um objeto e adiciona na lista'''
            data.append(OrdemDeServico(int(idOrdem), requisitante, telefone, descricao, dataOrdSer))
    
    '''Fecha o arquivo após a leitura'''
    archive.close()

    return data


'''Salva todas as ordens de serviço no arquivo'''
def saveData(data):

    '''Abre o arquivo em modo de escrita'''
    archive = open("ordensdeservico.txt", "w", encoding = "utf-8")

    '''Percorre todas as ordens cadastradas'''
    for ordem in data:

        '''Escreve cada ordem no arquivo'''
        archive.write(f"{ordem.StorageLine()}\n")

    '''Fecha o arquivo após a gravação'''
    archive.close()