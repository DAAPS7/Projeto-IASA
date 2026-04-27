from abc import ABC, abstractmethod

class Heuristica(ABC):
    """
    Classe abstrata que representa a heurística de um
    mecanismo de procura informado.
    """

    @abstractmethod
    def h(self, estado):
        """
        Método abstrato público que retorna a heurística
        do tipo double.
        """