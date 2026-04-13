class PassoSolucao:
    """
    Classe que representa uma estutura de informação (objeto) imutável.
    Recebe informação quando instanciada que não pode ser alterada,
    apenas visualizada.

    Atributos
    ---------
    self.__estado : Estado
        Estado do passo de solução
    self.__operador : Operador
        Operador do passo de solução
    """

    def __init__(self, estado, operador):
        """
        Construtor da classe de passo de solução.

        Parâmetros
        ----------
        estado : Estado
            Estado do passo de solução
        operador : Operador
            Operador do passo de solução
        """
        self.__estado = estado
        self.__operador = operador

    @property
    def estado(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__estado : Estado
            Estado do passo
        """
        return self.__estado
    
    @property
    def operador(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__operador : Operador
            Operador do passo
        """
        return self.__operador