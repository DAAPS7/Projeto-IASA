from abc import ABC, abstractmethod

class Operador(ABC):
    """
    Classe abstrata que representa o operador de geração de estado.
    Gera transições de estado e é o motor da procura.
    """

    @abstractmethod
    def aplicar(self, estado):
        """
        Aplicando o operador ao estado atual este retornará o 
        estado seguinte.
        """

    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Retorna o custo do estado sucessor que é produzido somando
        ao custo do estado atual que é acumulado ao longo da árvore.
        """