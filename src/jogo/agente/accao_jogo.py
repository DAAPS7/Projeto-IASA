from agente.accao import Accao

class AccaoJogo(Accao):
    """
    Classe que implementa a interface 'Accao' e representa a ação do jogo
    
    Atributos
    ---------
    __comando : ComandoJogo
        Instância privada de um comando de jogo do enumerado ComandoJogo
    """

    def __init__(self, comando):
        """
        Construtor da classe
        
        Parâmetros
        ----------
        comando : ComandoJogo
            Comando de jogo
        """
        self.__comando = comando

    @property
    def comando(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        __comando : ComandoJogo
            Atributo privado (self.__comando) que representa um comando de jogo
        """
        return self.__comando