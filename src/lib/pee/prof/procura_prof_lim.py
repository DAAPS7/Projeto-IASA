from .procura_profundidade import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):
    """
    Classe que especializa ProcuraProfundidade e atua de modo parecido à mesma.
    Possui uma profundidade limitada que permite explorar em profundidade até
    esse mesmo limite.
    Isto garante que o mecanismo encontrará uma solução, porque não pode ficar
    preso num ciclo infinito de nós.

    Atributos
    ---------
    self.__prof_max : int
        Profundidade máxima de exploração
    """

    def procurar(self, problema, prof_max=10):
        """
        Este método é semelhante ao método da super classe, mas recebe como
        argumento a profundidade máxima e atualiza o atributo self.__prof_max.

        Parâmetros
        ----------
        problema : Problema 
            Problema da procura
        prof_max : int
            Profundidade máxima de exploração
        """
        self.__prof_max = prof_max
        return super().procurar(problema)

    def _expandir(self, problema, no):
        """
        Este método utiliza o método da super classe, mas apenas quando a 
        profundidade de exploração atual não excede a profundidade máxima.
        Caso isto aconteça, retorna uma lista vazia, indicando que o
        mecanismo deve explorar o nó paralelo.

        Parâmetros
        ----------
        problema : Problema
            Problema da procura
        no : No
            Nó a explorar
        """
        return super()._expandir(problema, no) if no.profundidade < self.__prof_max else []