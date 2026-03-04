from abc import ABC, abstractmethod

class Control(ABC):
    """Classe abstrata que representa o controlo de um agente de jogo"""

    @abstractmethod
    def process(self, perception):
        """Retorna a ação do agente baseada na sua perceção"""