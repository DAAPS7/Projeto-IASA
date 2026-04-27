from agente.accao import Accao as AccaoAgente
"""
Na página 3 do projeto, é indicado que deve ser utilizado um alias para evitar ambiguidade e tornar
a herança mais clara e legível.
"""

class Accao(AccaoAgente):
    """
    Classe de uma ação de um agente reativo que herda da classe Accao da package agente da biblioteca

    Atributos
    ---------
    self.__prioridade : float
        Prioridade da ação
    """

    def __init__(self, prioridade=0):
        """
        Construtor da classe de ação de um agente reativo

        Invoca o construtor da classe parente através do método super()

        Parâmetros
        ----------
        prioridade : float
            Prioridade da ação que é por omissão igual a 0
        """
        super().__init__()
        self.__prioridade = prioridade

    @property
    def prioridade(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__prioridade : Estado
            Prioridade da ação
        """
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, valor):
        """
        Setter do atributo de prioridade

        Parâmetros
        ----------
        valor : int
            Valor a atribuir à prioridade
        """
        self.__prioridade = valor