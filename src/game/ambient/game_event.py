from enum import Enum

class GameEvent(Enum):
    """Enumerado dos eventos de jogo"""

    SILENCE = 's'
    NOISE = 'n'
    ANIMAL = 'a'
    FLEE = 'f'
    PICTURE = 'p'
    TERMINATE = 't'

    def display(self):
        """Método que mostra ao utilizador qual é o evento atual"""
        print(f"\nEvento: {self.name}")