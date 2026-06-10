from datetime import date

class OrdemDeServico:
    def _init_(self, requisitante: str, telefone: str, descricao: str, dataOrdSer: date):
        self.requisitante = requisitante
        self.telefone = telefone
        self.descricao = descricao
        self.dataOrdSer = dataOrdSer

    def listarOrdemServico(self):
        return f"{self.requisitante}, {self.telefone}, {self.descricao}, {self.dataOrdSer}"
    
    def StorageLine(self):
        return f"{self.requisitante}:{self.telefone}:{self.descricao}:{self.dataOrdSer}"