from agent.action import Action

class GameAction(Action):
    """
    Classe que implementa a interface 'Action' e representa a ação do jogo
    
    Atributos
    ---------
    __command : GameCommand
        Instância privada de um comando de jogo do enumerado GameComand
    """

    def __init__(self, command):
        """
        Construtor da classe
        
        Parâmetros
        ----------
        command : GameCommand
            Comando de jogo
        """
        self.__command = command

    @property
    def command(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        __command : GameCommand
            Atributo privado (self.__command) que representa um comando de jogo
        """
        return self.__command