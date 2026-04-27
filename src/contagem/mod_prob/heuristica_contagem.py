from pee.melhor_prim.heuristica import Heuristica

class HeuristicaContagem(Heuristica):
    """
    Realização da interface de heurística para o problema
    de contagem.

    Atributos
    ---------
    self.__valor_final : int
        Valor final do problema de contagem
    """

    def __init__(self, valor_final):
        self.__valor_final = valor_final

    def h(self, estado):
        return abs(self.__valor_final) - abs(estado.contagem)