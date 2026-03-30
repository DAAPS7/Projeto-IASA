class Resposta:

    def __init__(self, accao=None):
        self._accao = accao

    def activar(self, percepcao, intensidade=0):
        """Retorna uma ação"""
        accao = self._obter_accao(percepcao)
        
        if accao is not None:
            accao.prioridade(intensidade)

        return accao
    
    def _obter_accao(self, percepcao):
        """Por omissão retorna a ação do atributo"""
        return self._accao