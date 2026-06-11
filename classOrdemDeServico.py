class OrdemDeServico:
    def __init__(self, requisitante: str, telefone: str, descricao: str, dataOrdSer: str):
        self.requisitante = requisitante
        self.telefone = telefone
        self.descricao = descricao
        self.dataOrdSer = dataOrdSer

    def listarOrdemServico(self):
        return f"{self.requisitante}, {self.telefone}, {self.descricao}, {self.dataOrdSer}"
    
    def StorageLine(self):
        return f"{self.requisitante}:{self.telefone}:{self.descricao}:{self.dataOrdSer}"