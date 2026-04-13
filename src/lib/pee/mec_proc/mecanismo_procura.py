from abc import ABC
from .no import No
from .solucao import Solucao

class MecanismoProcura(ABC):
    """
    Classe que representa um mecanismo de procura.
    O mecanismo utiliza o atributo da fronteira para procurar
    uma solução para o problema.
    Memoriza os nós explorados e tem a função de atingir o estado
    de objetivo final.

    Atributos
    ---------
    self._fronteira : Fronteira
        Fronteira de nós
    """

    def __init__(self, fronteira):
        """
        Construtor da classe de mecanismo de procura que atribui uma
        fronteira inicial ao respetivo atributo.

        Parâmetros
        ----------
        fronteira : Fronteira
            Fronteira de nós
        """
        self._fronteira = fronteira
    
    def _iniciar_memoria(self):
        """
        Invoca o método de iniciar a fronteira.
        """
        self._fronteira.iniciar()
    
    def _memorizar(self, no):
        """
        Coloca o nó passado por parâmetro na memória da fronteira.

        Parâmetros
        ----------
        no : No
            Nó a memorizar
        """
        self._fronteira.inserir(no)

    def procurar(self, problema):
        """
        Este método realiza o processo de procura.
        Enquanto a fronteira não estiver vazia, verifica se o nó atual
        é a solução e, se for, retorna essa solução indicando que a
        procura foi resolvida. Caso contrário, expande esse nó e 
        memoriza os nós sucessores.

        Parâmetros
        ----------
        problema : Problema
            Problema da procura
        
        Retorna
        -------
        solucao : Solucao
            Solução da procura
        """
        self._iniciar_memoria()

        no = No(problema.estado_inicial)
        self._memorizar(no)
        
        while not self._fronteira.vazia:
            no = self._fronteira.remover()

            if problema.objectivo(no.estado):
                return Solucao(no)
                
            for no_suc in self._expandir(problema, no):
                self._memorizar(no_suc)
    
    def _expandir(self, problema, no):
        """
        Aplicam-se os operadores do problema para se obterem os estados
        seguintes e, a partir desses estados, calcula-se o custo e criam-se
        os nós dos estados seguintes.
        Finalmente, retorna-se uma lista de todos esses nós sucessores.

        Parâmetros
        ----------
        problema : Problema
            Problema da procura
        no : No
            Nó atual

        Retorna
        -------
        sucessores : List<No>
            Lista de nós sucessores
        """
        sucessores = []
        estado = no.estado

        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)

            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                no_suc = No(estado_suc, operador, no, custo) 

                sucessores.append(no_suc)
        
        return sucessores