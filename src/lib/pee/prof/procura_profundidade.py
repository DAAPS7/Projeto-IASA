from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):
    """
    Classe que implementa um mecanismo de procura em profundidade.
    Utiliza uma fronteira do tipo LIFO (Last-in First-out).
    """

    def __init__(self):
        """
        Invoca o construtor da super classe passando uma instância
        da classe de fronteira do tipo LIFO.
        """
        super().__init__(FronteiraLIFO())