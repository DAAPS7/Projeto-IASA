from abc import ABC, abstractmethod

class Behaviour(ABC):
    """
    Interface que representa um comportamento individual
    """

    @abstractmethod
    def activate(self, perception):
        """
        Método abstrato que processa uma perceção que obtém uma ação

        Parâmetros
        ----------
        perception : Perception
            Perceção a ser processada

        Retorna
        -------
        action : Action
            Ação obtida a partir do processamento
        """