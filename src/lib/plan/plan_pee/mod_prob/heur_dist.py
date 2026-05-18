from pee.melhor_prim.heuristica import Heuristica
import math

class HeurDist(Heuristica):
    """
    Classe que representa a heurística de distância.

    Implementa a interface Heuristica.

    Atributos
    ---------
    self.__estado_final : Estado
        Estado final do problema
    """

    def __init__(self, estado_final):
        """
        Construtor da classe de heurística de distância.

        Parâmetros
        ----------
        estado_final : Estado
            Estado final do problema
        """
        self.__estado_final = estado_final
    
    def h(self, estado):
        """
        Retorna a heurística da distância.

        Parâmetros
        ----------
        estado : Estado
            Estado atual
        
        Retorna
        -------
        : double
            Distância euclidiana entre a posição do estado atual e
            a posição do estado final do problema.
        """

        return math.dist(self.__estado_final.posicao, estado.posicao)