from .avaliador_heur import AvaliadorHeur

class AvaliadorAA(AvaliadorHeur):

    def prioridade(self, no):
        """
        Implementação do f(n) da procura A* que é igual
        à soma de g(n) (Custo até ao nó atual) e h(n) 
        (heurística).

        Retorna
        -------
        f(n) : double
            Prioridade do nó avaliado pelo avaliador de A*
        """
        # f(n) = g(n) + h(n)
        return no.custo + self.heuristica.h(no.estado)