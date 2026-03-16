from agent.action import Action as AgentAction
"""
Na página 3 do projeto, é indicado que deve ser utilizado um alias para evitar ambiguidade e tornar
a herança mais clara e legível.
"""

class Action(AgentAction):
    """
    Classe de uma ação de um agente reativo que herda da classe Action da package agente da biblioteca

    Atributos
    ---------
    self.__priority : float
        Prioridade da ação
    """

    def __init__(self, priority=0):
        """
        Construtor da classe de ação de um agente reativo

        Invoca o construtor da classe parente através do método super()

        Parâmetros
        ----------
        priority : float
            Prioridade da ação que é por omissão igual a 0
        """
        super().__init__()
        self.__priority = priority

    @property
    def priority(self):
        """Getter"""
        return self.__priority

    @priority.setter
    def priority(self, value):
        """Setter"""
        self.__priority = value