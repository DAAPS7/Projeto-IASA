from abc import ABC, abstractmethod

class Agent(ABC):
    """
    Classe abstrata que representa um agente autónomo

    Atributos
    ---------
    _control : Control
        Instância da classe Control protegida
    """
    
    def __init__(self, control):
        """
        Construtor da classe de agente

        Parâmetros
        ----------
        control : Control
            Instância da classe Control
        """
        self._control = control

    @abstractmethod
    def _perceive(self):
        """
        Método protegido abstrato de instância que retorna a perceção do ambiente
        """

    @abstractmethod
    def _act(self, action):
        """
        Método protegido abstrato de instância que executa a ação do ambiente
        
        Parâmetros
        ----------
        action : Action
            Instância da classe Action
        """

    def execute(self):
        """
        Método público de instância que executa a ação prdouzida pelo controlo do agente

        Invoca o método protegido que perceciona

        Invoca o método do controlo que retorna uma ação e, se a mesma existir, invoca o método de atuar com a ação obtida
        """

        perception = self._perceive()
        action = self._control.process(perception)
        if action is not None:
            self._act(action)