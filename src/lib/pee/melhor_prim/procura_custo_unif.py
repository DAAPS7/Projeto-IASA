from .procura_melhor_prim import ProcuraMelhorPrim
from .aval.avaliador_custo_unif import AvaliadorCustoUnif

class ProcuraCustoUnif(ProcuraMelhorPrim):
    """
    Procura "melhor primeiro" em que o avaliador é
    um avaliador de custo uniforme.
    """

    def __init__(self):
        """
        Construtor da classe de procura de custo uniforme.
        Invoca o construtor da super classe com uma instância de
        um avaliador de custo uniforme.
        """
        super().__init__(AvaliadorCustoUnif())