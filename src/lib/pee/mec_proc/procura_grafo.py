from .mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura):
    
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
        """
        if self._manter(no):
            self._explorados[no.estado] = no
            super()._memorizar(no)
    
    def _manter(self, no):
        raise NotImplementedError