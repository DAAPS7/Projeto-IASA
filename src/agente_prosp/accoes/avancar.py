from ecr.accao import Accao
from sae.agente.movimento import Movimento

class Avancar(Movimento, Accao):

    def __init__(self):
        """
        Construtor da classe de avanço do agente

        Invoca o construtor da super classe Movimento (por omissão) e passa None como parâmetro
        o que indica que o agente avançará para a sua direção atual, mantendo o trajeto.

        Tal como explicado no construtor da classe Mover, o passo por omissão tem o valor de 1.
        """
        super().__init__(None)