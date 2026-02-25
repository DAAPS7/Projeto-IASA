from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, control):
        self._control = control

    @abstractmethod
    def _perceive(self):
        """Obter perceção do ambiente"""

    @abstractmethod
    def _act(self, action):
        """Executar ação do ambiente"""

    def execute(self):
        """Executar ação"""