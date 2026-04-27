from .procura_melhor_prim import ProcuraMelhorPrim
from abc import ABC

class ProcuraInformada(ProcuraMelhorPrim, ABC):
    """
    Classe da procura informada que especializa ProcuraMelhorPrim.

    Atributos
    ---------
    self._heuristica : Heuristica
        Heurística da procura
    """

    def procurar(self, problema, heuristica):
        """
        Procura informada que retorna a invocação 
        do método procurar da super classe e guarda
        no atributo protegido a heurística. 
        """
        self._avaliador.heuristica = heuristica
        return super().procurar(problema)
