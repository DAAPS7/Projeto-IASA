from mod.estado import Estado

class EstadoContagem(Estado):
    """
    Especialização da classe de estado para o problema da contagem.

    Atributos
    ---------
    self.__contagem : int 
        Contagem do estado
    """

    def __init__(self, contagem):
        """
        Construtor da classe de estado de contagem.

        Parâmetros
        ----------
        contagem : int
            Contagem do estado
        """
        self.__contagem = contagem

    def id_valor(self):
        """
        Método que retorna o valor de identidade do estado que corresponde à
        contagem em si.
        Este valor é crucial para a distinção de estados, sendo este, o valor
        do hash da classe.

        Retorna
        -------
        self.__contagem : int
            Valor de contagem
        """
        return self.__contagem

    @property
    def contagem(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__contagem : int
            Contagem do estado
        """
        return self.__contagem