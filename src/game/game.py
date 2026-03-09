from character.character import Character
from ambient.game_ambient import GameAmbient
from ambient.game_event import GameEvent

class Game:
    
    def __init__(self):
        """
        Instancia-se primeiro o ambiente de jogo, sendo que a personagem necessita que seja passado um ambiente de jogo como parâmetro de construtor.
        
        Atributos
        """

        self.__game_ambient = GameAmbient()
        self.__character = Character(self.__game_ambient)
        self.__character.display()

    def execute(self):
        """
        Método público que executa o jogo.
        Do while como loop de jogo para correr o jogo pelo menos 1 vez antes de verificar a condição.
        """

        while True:
            self.__game_ambient.evolve()
            self.__character.execute()
            self.__character.display()

            if self.__game_ambient.observe() == GameEvent.TERMINATE:
                break
    
if __name__ == "__main__":
    Game().execute()