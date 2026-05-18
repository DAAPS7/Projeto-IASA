from abc import ABC, abstractmethod

class ModeloPlan(ABC):
    """
    Interface de um modelo de planeamento.
    """

    @abstractmethod
    def obter_estado(self):
        """
        Obtém o estado planeado e retorna-o.
        
        Retorna
        -------
        : Estado
            Estado planeado
        """
    
    @abstractmethod
    def obter_estados(self):
        """
        Obtém os estados planeados e retorna uma lista com os mesmos.

        Retorna
        -------
        : List<Estado>
            Lista de estados planeados
        """
    
    @abstractmethod
    def obter_operadores(self):
        """
        Retorna uma lista de operadores.
        """