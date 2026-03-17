from abc import ABC, abstractmethod

class Estimulo(ABC):
    """
    Interface que representa o estímulo de um agente reativo
    """

    @abstractmethod
    def detectar(self, percepcao):
        """
        Método abstrato que processa a perceção e obtém uma ação
        
        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção a processar

        Retorna
        -------
        accao : Accao
            Ação processada
        """