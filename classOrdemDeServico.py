'''/classOrdemDeServico.py'''

'''Classe responsável por representar uma Ordem de Serviço, armazenando todas as informações necessárias'''

class OrdemDeServico:

    '''Método construtor que inicializa os atributos da ordem de serviço no momento da criação do objeto'''
    def __init__(self, requisitante: str, telefone: str, descricao: str, dataOrdSer: str):
        self.requisitante = requisitante
        self.telefone = telefone
        self.descricao = descricao
        self.dataOrdSer = dataOrdSer

    '''Retorna os dados da ordem formatados para exibição'''
    def listarOrdemServico(self):
        return f"{self.requisitante}, {self.telefone}, {self.descricao}, {self.dataOrdSer}"
    
    '''Retorna os dados da ordem formatados para armazenamento em arquivo'''
    def StorageLine(self):
        return f"{self.requisitante}:{self.telefone}:{self.descricao}:{self.dataOrdSer}"