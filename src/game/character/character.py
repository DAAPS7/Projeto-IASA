from game.agent import GameAgent
from character_control import CharacterControl

class Character(GameAgent):
    """Classe que representa a personagem do jogo"""

    def __init__(self, game_ambient):
        """Construtor da classe da personagem que toma ambiente de jogo como parâmetro"""
        super.__init__(game_ambient, CharacterControl())

    def display(self):
        """Método que mostra a personagem do jogo"""
        raise NotImplementedError