from abc import ABC, abstractmethod

class Fronteira(ABC):
    """
    Classe que representa a fronteira do grafo que é constítuida
    pelos nós que ainda estão por expandir.

    Atributos
    ---------
    self._nos : List<No>
        Lista de nós da fronteira
    """

    def __init__(self):
        """
        Construtor da classe da fronteira que invoca o método de iníco 
        da fronteira que, por sua vez, inicializa o atributo self._nos.
        """
        self.iniciar()

    def iniciar(self):
        """
        Método que inicia a fronteira, inicializando o atributo da lista
        de nós respetivos.
        """
        self._nos = []

    @abstractmethod
    def inserir(self, no):
        """
        Método abstrato que insere um nó na lista da fronteira.

        Parâmetros
        ----------
        no : No
            Nó a inserir na lista
        """

    def remover(self):
        """
        Remove o primeiro nó da lista e retorna-o.
        """
        return self._nos.pop(0)
    
    @property
    def vazia(self):
        """
        Esta propriedade read-only é gerada dinamicamente e verifica se a 
        lista dos nós está vazia, retornando True se isso se verificar.
        """
        return len(self._nos) == 0