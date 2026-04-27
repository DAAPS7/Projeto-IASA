from .procura_informada import ProcuraInformada
from .aval.avaliador_aa import AvaliadorAA

class ProcuraAA(ProcuraInformada):
    """
    Classe que especializa ProcuraInformada e representa
    o mecanismo de procura A*.
    """

    def __init__(self):
        """
        Construtor da classe de procura A* que invoca o 
        construtor da super classe com uma instância de 
        avaliador A*.
        """
        super().__init__(AvaliadorAA())