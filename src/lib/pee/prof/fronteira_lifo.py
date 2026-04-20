from ..mec_proc.fronteira import Fronteira

class FronteiraLIFO(Fronteira):
    """
    Classe que representa uma fronteira do tipo LIFO, utilizada para implementar
    o mecanismo de procura em profundidade.
    """

    def inserir(self, no):
        """
        Insere o nó passado como parâmetro no índice 0 da lista de nós.
        Ao remover o último elemento desta lista, remove-se o mais antigo
        e, portanto, torna a manipulação desta lista, uma manipulação do
        tipo LIFO.

        Parâmetros
        ----------
        no : No
            Nó a inserir
        """
        self._nos.insert(0, no)