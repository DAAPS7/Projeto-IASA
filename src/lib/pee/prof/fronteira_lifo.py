from ..mec_proc.fronteira import Fronteira

class FronteiraLIFO(Fronteira):

    def inserir(self, no):
        self._nos.insert(0, no)