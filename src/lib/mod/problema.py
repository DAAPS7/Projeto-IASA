from abc import abstractmethod

class Problema:
    """
    Classe que representa o problema inicial.
    Define qual é o estado inicial e o objetivo final e utiliza as 
    classes Estado e Problema para resolver o caminho na árvore de
    procura.

    Atributos
    ----------
    self.__estado_inicial : Estado
        Estado inicial do problema
    self.__operadores : List<Operador>
        Lista de operadores
    """

    def __init__(self, estado_inicial, operadores):
        """
        Construtor da classe do problema

        Parâmetros
        ----------
        estado_inicial : Estado
            Estado inicial do problema
        operadores : List<Operador>
            Lista de operadores
        """
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores
    
    @abstractmethod
    def objectivo(self, estado):
        """
        Retorna True caso o estado seja o estado final do problema.
        """
    
    @property
    def estado_inicial(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__estado_inicial : Estado
            Estado inicial do problema
        """
        return self.__estado_inicial
    
    @property
    def operadores(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__operadores : List<Operador>
            Lista de operadores
        """
        return self.__operadores