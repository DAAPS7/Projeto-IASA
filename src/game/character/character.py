from agent.game_agent import GameAgent
from .character_control import CharacterControl

class Character(GameAgent):
    """
    Classe que representa a personagem do jogo

    Extende a classe parente GameAgent
    """

    def __init__(self, game_ambient):
        """
        Construtor da classe da personagem
        
        Invoca o construtor da classe parente a partir do método super() passando o parâmetro game_ambient e instanciando um
        novo controlo de personagem, CharacterControl

        Parâmetros
        ----------
        game_ambient : GameAmbient
            Ambiente de jogo
        """
        super().__init__(game_ambient, CharacterControl())

    def display(self):
        """
        Método que mostra o estado da personagem do jogo
        """
        print(f"\nEstado: {self._control.state}")