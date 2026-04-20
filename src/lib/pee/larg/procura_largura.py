from ..mec_proc.procura_grafo import ProcuraGrafo
from .fronteira_fifo import FronteiraFIFO

class ProcuraLargura(ProcuraGrafo):
    """
    Classe que implementa um mecanismo de procura em largura.
    Utiliza uma fronteira do tipo FIFO (First-in First-out).
    Esta classe especializa ProcuraGrafo para ter capacidade
    de memorizar os nós explorados.
    """

    def __init__(self):
        """
        Invoca o construtor da super classe passando uma instância
        da classe de fronteira do tipo FIFO.
        """
        super().__init__(FronteiraFIFO())