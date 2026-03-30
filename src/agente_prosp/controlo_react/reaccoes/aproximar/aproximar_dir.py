from ecr.reaccao import Reaccao
from .estimulo_alvo import EstimuloAlvo
from .resposta_mover import RespostaMover

class AproximarDir(Reaccao):
    """
    Classe que representa o comportamento de uma aproximação direcional
    """

    def __init__(self, direccao):
        """
        Invoca o construtor da classe parente através do método super() passando-lhe uma
        instância de um estímulo de alvo e da resposta de mover na direção recebida 
        como parâmetro

        Parâmetros
        ----------
        direccao : Direccao
            Direção da aproximação
        """
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))