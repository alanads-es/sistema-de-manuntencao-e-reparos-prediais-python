'''/classOrdemDeServico.py'''

'''Classe responsável por representar uma Ordem de Serviço, armazenando os dados da solicitação e seu identificador'''

class OrdemDeServico:

    '''Método construtor que inicializa os atributos da ordem de serviço no momento da criação do objeto'''
    def __init__(self, idOrdem: int, requisitante: str, telefone: str, descricao: str, dataOrdSer: str):
        self.idOrdem = idOrdem
        self.requisitante = requisitante
        self.telefone = telefone
        self.descricao = descricao
        self.dataOrdSer = dataOrdSer

    '''Retorna os dados da ordem formatados para exibição'''
    def listarOrdemServico(self):
        return f"{self.idOrdem}, {self.requisitante}, {self.telefone}, {self.descricao}, {self.dataOrdSer}"
    
    '''Retorna o identificador e os dados da ordem formatados para armazenamento em arquivo'''
    def StorageLine(self):
        return f"{self.idOrdem}:{self.requisitante}:{self.telefone}:{self.descricao}:{self.dataOrdSer}"