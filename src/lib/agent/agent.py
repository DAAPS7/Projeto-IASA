from abc import ABC, abstractmethod

class Agent(ABC):
    """Classe abstrata que representa um agente autónomo"""
    
    def __init__(self, control):
        self._control = control

    @abstractmethod
    def _perceive(self):
        """Método abstrato de instância que retorna a perceção do ambiente"""

    @abstractmethod
    def _act(self, action):
        """Método abstrato de instância que executa a ação do ambiente"""

    def execute(self):
        """Método público de instância que executa a ação prdouzida pelo controlo do agente"""

        perception = self._perceive()
        action = self._control.process(perception)
        if action is not None:
            self._act(action)