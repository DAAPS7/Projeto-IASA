from .avaliador import Avaliador
from abc import ABC

class AvaliadorHeur(Avaliador, ABC):
    """
    Classe abstrata de um avaliador heurístico.

    Atributos
    ---------
    self.__heuristica : Heuristica
        Heurística do avaliador abstrato
    """

    def __init__(self):
        """
        Construtor da classe abstrata de um avaliador heurístico.

        Parâmetros
        ----------
        heuristica : Heuristica
            Heurística do avaliador abstrato
        """
        self.__heuristica = None

    @property
    def heuristica(self):
        return self.__heuristica
    
    @heuristica.setter
    def heuristica(self, h):
        self.__heuristica = h