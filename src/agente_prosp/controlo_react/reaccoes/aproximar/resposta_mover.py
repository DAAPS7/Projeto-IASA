from ecr.resposta import Resposta
from agente_prosp.accoes.mover import Mover

class RespostaMover(Resposta):
    
    def __init__(self, direccao=None):
        """
        O construtor recebe como parâmetro uma direção que será utilizada para instanciar
        a ação de Mover que pede como parâmetro de construtor uma direção

        Invoca o construtor da classe parente passando a instância de Mover que foi criada
        """

        super().__init__(Mover(direccao))