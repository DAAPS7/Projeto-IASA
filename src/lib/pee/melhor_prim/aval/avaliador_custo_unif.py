from .avaliador import Avaliador

class AvaliadorCustoUnif(Avaliador):

    def prioridade(self, no):
        """
        Método que retorna a prioridade do nó que 
        equivale ao custo até ao mesmo nó.

        Parâmetros
        ----------
        no : No
            Nó a avaliar

        Retorna
        -------
        no.custo : double
            Custo até ao nó
        """
        return no.custo