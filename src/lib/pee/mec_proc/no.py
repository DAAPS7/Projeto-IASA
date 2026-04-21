class No:
    """
    Classe que representa um nó do grafo do problema de procura.
    Representa a etapa de procura do problema.

    Atributos
    ---------
    self.__estado : Estado
        Estado do nó
    self.__operador : Operador
        Operador que gerou o estado
    self.__antecessor : No
        Nó antecessor
    self.__custo : double
        Custo da raíz até ao nó
    self.__prioridade : int
        Atributo de suporte à comparação de nós
    self.__profundidade : int
        Profundidade do nó
    """

    def __init__(self, estado, operador=None, antecessor=None, custo=0):
        """
        Construtor da classe de nó.
        Inicializa o atributo de profundidade somando 1 à profundidade do nó
        antecessor, caso este exista. Se não existir, o nó é a raíz e tem 
        profundidade 0.

        Parâmetros
        ----------
        estado : Estado
            Estado do nó
        operador : Operador
            Operador que gerou o estado
        antecessor : No
            Nó antecessor
        custo : double
            Custo da raíz até ao nó
        """
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
        """
        Para tornar esta classe comparável, implementa a comparação 
        "menor que" com base na prioridade.

        Compara a prioridade deste nó com outro nó.
        """
        return self.prioridade < no.prioridade

    @property
    def estado(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__estado : Estado
            Estado do nó
        """
        return self.__estado
    
    @property
    def custo(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__custo : double
            Custo da raíz até ao nó
        """
        return self.__custo
    
    @property
    def operador(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__operador : Operador
            Operador que gerou o estado
        """
        return self.__operador
    
    @property
    def antecessor(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__antecessor : No
            Nó antecessor
        """
        return self.__antecessor
    
    @property
    def profundidade(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__profundidade : int
            Profundidade do nó
        """
        return self.__profundidade
    
    @property
    def prioridade(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__prioridade : int
            Atributo de suporte à comparação de nós
        """
        return self.__prioridade
    
    @prioridade.setter
    def prioridade(self, valor):
        """
        Setter do atributo de prioridade

        Parâmetros
        ----------
        valor : int
            Valor a atribuir à prioridade
        """
        self.__prioridade = valor