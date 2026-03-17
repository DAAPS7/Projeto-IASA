from agente.agente_jogo import AgenteJogo
from .controlo_personagem import ControloPersonagem

class Personagem(AgenteJogo):
    """
    Classe que representa a personagem do jogo

    Extende a classe parente GameAgent
    """

    def __init__(self, ambiente_jogo):
        """
        Construtor da classe da personagem
        
        Invoca o construtor da classe parente a partir do método super() passando o parâmetro ambiente_jogo e instanciando um
        novo controlo de personagem, ControloPersonagem

        Parâmetros
        ----------
        ambiente_jogo : AmbienteJogo
            Ambiente de jogo
        """
        super().__init__(ambiente_jogo, ControloPersonagem())

    def mostrar(self):
        """
        Método que mostra o estado da personagem do jogo
        """
        print(f"\nEstado: {self._controlo.estado}")