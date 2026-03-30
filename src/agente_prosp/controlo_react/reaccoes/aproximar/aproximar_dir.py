from ecr.reaccao import Reaccao
from .estimulo_alvo import EstimuloAlvo
from .resposta_mover import RespostaMover

class AproximarDir(Reaccao):
    """Aproximar direcional"""

    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))