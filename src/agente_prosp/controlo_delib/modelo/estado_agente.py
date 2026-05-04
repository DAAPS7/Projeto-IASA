from mod.estado import Estado

class EstadoAgente(Estado):
    """
    Classe que representa o estado do agente e possui a
    sua posição atual.

    Atributos
    ---------
    self.__posicao : Posicao
        Posição do agente
    self.__id_valor : int
        Hash do estado do agente
    """
    
    def __init__(self, posicao):
        """
        Construtor da classe do estado de agente.
        Atribui o hash da posição do agente ao atributo self.__id_valor.

        Parâmetros
        ----------
        posicao : Posicao
            Posição do agente
        """
        self.__posicao = posicao
        self.__id_valor = hash(posicao)
    
    def id_valor(self):
        """
        Método que retorna um valor de identificação do estado do
        agente.

        Retorna
        -------
        self.__id_valor : int
            Valor de identificação
        """
        return self.__id_valor
    
    @property
    def posicao(self):
        """
        Propriedade pública read-only da posição do agente

        Retorna
        self.__posicao : Posicao
            Posição do agente
        """
        return self.__posicao