from ecr.hierarquia import Hierarquia
from agente_prosp.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente_prosp.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from agente_prosp.controlo_react.reaccoes.explorar.explorar import Explorar
from agente_prosp.controlo_react.reaccoes.explorar.explorar_mem import ExplorarMem


class Recolher(Hierarquia):
    """
    Este comportamento tem o objetivo de reunir todos os comportamentos num único
    comportamento composto
    """

    def __init__(self):
        """
        Invoca o construtor da classe parente Hierarquia que especializa ComportamentoComp
        e coloca como parâmetro do construtor os comportamentos individuais em lista, formando
        um comportamento composto hierárquico.
        """
        super().__init__([AproximarAlvo(), EvitarObst(), ExplorarMem(), Explorar()])