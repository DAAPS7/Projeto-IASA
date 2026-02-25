from abc import ABC, abstractmethod

class Control(ABC):
    @abstractmethod
    def process(self, perception):
        """Retorna a ação baseada na perceção"""