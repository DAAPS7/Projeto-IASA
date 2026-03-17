from abc import ABC, abstractmethod

class Comportamento(ABC):
    """
    Interface que representa um comportamento individual
    """

    @abstractmethod
    def activar(self, percepcao):
        """
        Método abstrato que processa uma perceção que obtém uma ação

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção a ser processada

        Retorna
        -------
        accao : Accao
            Ação obtida a partir do processamento
        """