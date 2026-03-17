from abc import ABC, abstractmethod

class Controlo(ABC):
    """
    Classe abstrata que representa o controlo de um agente de jogo
    """

    @abstractmethod
    def processar(self, percepcao):
        """
        Retorna a ação do agente baseada na sua perceção

        Parâmetros
        ----------
        percepcao : Percepcao
            Instância da classe Percepcao
        """