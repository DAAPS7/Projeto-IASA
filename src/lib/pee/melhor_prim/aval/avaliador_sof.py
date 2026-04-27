from .avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):
    """
    Classe que representa um avaliador sôfrego, especializando
    um avaliador heurístico.
    """

    def prioridade(self, no):
        """
        Implementação do f(n) da procura sôfrega que é igual
        a h(n) (heurística).

        Retorna
        -------
        f(n) : double
            Prioridade do nó avaliado pelo avaliador sôfrego
        """
        # f(n) = h(n)
        return self.heuristica.h(no.estado)