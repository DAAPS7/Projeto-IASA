from enum import Enum

class ComandoJogo(Enum):
    """
    Enumerado dos comandos de jogo
    """

    PROCURAR = 1
    APROXIMAR = 2
    OBSERVAR = 3
    FOTOGRAFAR = 4

    def mostrar(self):
        """
        Método que mostra ao utilizador qual é a ação atual
        """
        print(f"\nAção: {self.name}")