from ecr.reaccao import Reaccao
from .estimulo_obst import EstimuloObst
from .resposta_evitar import RespostaEvitar

class EvitarObst(Reaccao):
    """
    Reação com o objetivo de colocar o agente a evitar obstáculos do ambiente
    """

    def __init__(self):
        """
        Invoca o construtor da classe de reação passando uma instância de estímulo de obstáculo e
        a respetiva resposta
        """
        super().__init__(EstimuloObst(), RespostaEvitar())