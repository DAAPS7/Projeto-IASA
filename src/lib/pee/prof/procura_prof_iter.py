from .procura_prof_lim import ProcuraProfLim

class ProcuraProfIter(ProcuraProfLim):
    """
    Classe que representa a procura em profundidade iterativa.
    Esta especializa a procura em profundidade limitada, sendo que
    são semelhantes. A diferença entre as duas é que na iterativa,
    o mecanismo incrementa o limite da profundidade dinamicamente.
    A principal vantagem deste mecanismo é o facto de não depender de
    acertar à partida na profundidade, pois esta é incrementada ao longo
    da exploração.
    """

    def procurar(self, problema, inc_prof=1, limite_prof=100):
        """
        Método de procura alterado para que a profundidade seja incrementada.

        Parâmetros
        ----------
        problema : Problema
            Problema da procura
        inc_prof : int
            Valor de incremento da profundidade
        limite_prof : int
            Valor máximo de profundidade

        Retorna
        -------
        solucao : Solucao
            Solução da procura
        """
        for prof_max in range(0, limite_prof + 1, inc_prof):
            solucao = super().procurar(problema, prof_max)
            if solucao:
                return solucao