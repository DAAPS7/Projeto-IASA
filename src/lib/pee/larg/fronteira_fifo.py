from ..mec_proc.fronteira import Fronteira

class FronteiraFIFO(Fronteira):
    """
    Classe que representa uma fronteira do tipo FIFO, utilizada para implementar
    o mecanismo de procura em largura.
    """

    def inserir(self, no):
        """
        Insere o nó passado como parâmetro na última posição da lista de nós.
        Ao remover o último elemento desta lista, remove-se o mais recente
        e, portanto, torna a manipulação desta lista, uma manipulação do
        tipo FIFO.

        Parâmetros
        ----------
        no : No
            Nó a inserir
        """
        self._nos.append(no)