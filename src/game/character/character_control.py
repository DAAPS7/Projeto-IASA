from lib.agent.control import Control

class CharacterControl(Control):
    """Classe que representa o controlo da personagem"""

    def __init__(self):
        """Construtor da classe do controlo da personagem"""
        super().__init__()
    
    def process(self, perception):
        """Implementação do método abstrato do processamento da perceção do ambiente de jogo"""
        raise NotImplementedError