from abc import ABC, abstractmethod

class Stimulus(ABC):
    """
    Interface que representa o estímulo de um agente reativo
    """

    @abstractmethod
    def detect(self, perception):
        """
        Método abstrato que processa a perceção e obtém uma ação
        
        Parâmetros
        ----------
        perception : Perception
            Perceção a processar

        Retorna
        -------
        action : Action
            Ação processada
        """