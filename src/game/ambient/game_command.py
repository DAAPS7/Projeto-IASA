from enum import Enum

class GameCommand(Enum):
    """
    Enumerado dos comandos de jogo
    """

    SEEK = 1
    APPROACH = 2
    OBSERVE = 3
    PHOTOGRAPH = 4

    def display(self):
        """
        Método que mostra ao utilizador qual é a ação atual
        """
        print(f"\nAção: {self.name}")