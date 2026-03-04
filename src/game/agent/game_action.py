from lib.agent.action import Action

class GameAction(Action):
    """Classe que implementa a interface 'Action' e representa a ação do jogo"""

    def __init__(self, command):
        """Construtor da classe que toma um comando como parâmetro"""
        self.__command = command

    @property
    def command(self):
        """Propriedade pública que retorna o atributo privado (self.__command) em read-only"""
        return self.__command