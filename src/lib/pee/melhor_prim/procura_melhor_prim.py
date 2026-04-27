from ..mec_proc.procura_grafo import ProcuraGrafo
from .fronteira_prioridade import FronteiraPrioridade
from abc import ABC

class ProcuraMelhorPrim(ProcuraGrafo, ABC):
    """
    Classe que representa um mecanismo de procura "melhor primeiro".
    É uma classe abstrata que é utilizada para implementar outros
    mecanismos de procura.

    Atributos
    ---------
    self._avaliador : Avaliador
        Avaliador da fronteira de prioridade
    """

    def __init__(self, avaliador):
        """
        Construtor da classe de procura "melhor primeiro".

        Parâmetros
        ----------
        avaliador : Avaliador
            Avaliador da fronteira de prioridade
        """
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador

    def _manter(self, no):
        """
        Implementação do método protegido que mantém o nó
        se ainda não foi explorado ou se o seu custo é 
        menor que o custo dos nós explorados.

        Parâmetros
        ----------
        no : No
            Nó a avaliar

        Retorna
        -------
        manter : boolean
            Valor booleano que indica se deve manter o nó ou não
        """

        return super()._manter(no) or \
               no.custo < self._explorados[no.estado].custo