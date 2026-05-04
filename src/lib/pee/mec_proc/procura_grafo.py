from .mecanismo_procura import MecanismoProcura
from abc import ABC

class ProcuraGrafo(MecanismoProcura, ABC):
    """
    Classe que especializa MecanismoProcura que implementa sobre essa classe abstrata,
    a capacidade de apenas inserir nós não explorados na fronteira.

    Atributos
    ---------
    self._explorados : Dict
        Dicionário de nós explorados associados ao seu estado
    """

    def _iniciar_memoria(self):
        """
        Invoca o método da super classe e inicializa o atributo self._explorados.
        """
        super()._iniciar_memoria()
        self._explorados = {}
    
    def _memorizar(self, no):
        """
        Caso seja para manter o nó, memoriza-o e adiciona-o à fronteira, a partir
        do método da super classe.

        Parâmetros
        ----------
        no : No
            Nó a memorizar
        """
        if self._manter(no):
            self._explorados[no.estado] = no
            super()._memorizar(no)
    
    def _manter(self, no):
        """
        Retorna True, caso o estado do nó ainda não for presente na lista dos
        nós explorados.

        Parâmetros
        ----------
        no : No
            Nó a manter
        """
        return no.estado not in self._explorados