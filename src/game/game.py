from character.character import Character
from ambient.game_ambient import GameAmbient
from ambient.game_event import GameEvent

class Game:
    """
    Classe de jogo

    Atributos
    ---------
        __game_ambient : GameAmbient
            Instância privada do ambiente de jogo
        __character : Character
            Instância privada da personagem do jogo
    """

    def __init__(self):
        """
        Construtor da classe de jogo.

        Instancia-se primeiro o ambiente de jogo, sendo que a personagem necessita 
        que seja passado um ambiente de jogo como parâmetro de construtor.
                
        É mostrada a personagem após ser instanciada.
        """

        self.__game_ambient = GameAmbient()
        self.__character = Character(self.__game_ambient)
        self.__character.display()

    def execute(self):
        """
        Método público que executa o loop de jogo.

        Do while como loop de jogo para correr o jogo pelo menos 1 vez antes de verificar a condição.
        """

        while True:
            self.__game_ambient.evolve()
            self.__character.execute()
            self.__character.display()

            if self.__game_ambient.observe() == GameEvent.TERMINATE:
                break
    
"""
Caso este módulo esteja a ser executado, __name__ recebe '__main__' e cria uma instância da classe Game e executa, 
evitando que isso aconteça quando a classe for importada noutro módulo.
"""
if __name__ == "__main__":
    Game().execute()