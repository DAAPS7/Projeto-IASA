from ..mec_proc.fronteira import Fronteira
from heapq import heappush, heappop

class FronteiraPrioridade(Fronteira):

    def __init__(self, avaliador):
        super().__init__()
        self.__avaliador = avaliador
    
    def inserir(self, no):
        """
        O método heappush insere os nós por ordem. Isto é possível,
        sendo que a classe No é comparável.
        """
        no.prioridade = self.__avaliador.prioridade(no)
        heappush(self._nos, no)
    
    def remover(self):
        return heappop(self._nos)