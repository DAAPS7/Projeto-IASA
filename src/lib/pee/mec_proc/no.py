class No:
    def __init__(self, estado, operador=None, antecessor=None, custo=0):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo
        self.__prioridade = 0
        
        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0
    
    def __lt__(self, no):
        return self.prioridade < no.prioridade

    @property
    def estado(self):
        return self.__estado
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor
    
    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def prioridade(self):
        return self.__prioridade
    
    @prioridade.setter
    def prioridade(self, valor):
        self.__prioridade = valor