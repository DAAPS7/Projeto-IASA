from enum import Enum

class EventoJogo(Enum):
    """
    Enumerado dos eventos de jogo
    """

    SILENCIO = 's'
    RUIDO = 'r'
    ANIMAL = 'a'
    FUGA = 'f'
    FOTOGRAFIA = 'o'
    TERMINAR = 't'

    def mostrar(self):
        """
        Método que mostra ao utilizador qual é o evento atual
        """
        print(f"\nEvento: {self.name}")