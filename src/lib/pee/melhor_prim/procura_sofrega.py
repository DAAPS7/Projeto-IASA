from .procura_informada import ProcuraInformada
from .aval.avaliador_sof import AvaliadorSof

class ProcuraSofrega(ProcuraInformada):
    """
    Classe que especializa ProcuraInformada e representa
    o mecanismo de procura sôfrega.
    """

    def __init__(self):
        """
        Construtor da classe de procura sôfrega que invoca
        o construtor da super classe com uma instância de
        avaliador sôfrego.
        """
        super().__init__(AvaliadorSof())