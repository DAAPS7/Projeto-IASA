from abc import ABC, abstractmethod

class Avaliador(ABC):
    """
    Classe abstrata que reprsenta um avaliador de nós.
    """

    @abstractmethod
    def prioridade(self, no):
        """
        Método abstrato que retorna a prioridade do
        nó atual.
        """