class Resposta:
    """
    Classe que representa a resposta gerada a partir do estímulo que irá obter uma ação 

    Atributos
    ---------
    self._accao : Accao
        Ação da resposta
    """


    def __init__(self, accao=None):
        """
        Construtor da classe de resposta

        Parâmetros
        ----------
        accao : Accao
            Ação da resposta que por omissão é None
        """
        self._accao = accao

    def activar(self, percepcao, intensidade=0):
        """
        Obtém a ação do atributo, altera a sua prioridade caso exista e retorna-a

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção do ambiente
        intensidade : float
            Prioridade da ação

        Retorna
        -------
        accao : Accao
            Ação do agente
        """
        accao = self._obter_accao(percepcao)
        
        if accao is not None:
            accao.prioridade = intensidade

        return accao
    
    def _obter_accao(self, percepcao):
        """
        Por omissão retorna a ação do atributo
        
        Parâmetros
        ----------
        percepcao : Percepcao
            Não utilizado
        """
        return self._accao