from lib.agent.agent import Agent
from game_perception import GamePerception

class GameAgent(Agent):
    """Classe que representa o agente do jogo e herda da classe 'Agent'"""
    
    def __init__(self, game_ambient, control):
        """Construtor da classe de agente de jogo"""

        # Chama o construtor da classe parente e passa a variável 'control' como argumento
        super().__init__(control)
        self.__game_ambient = game_ambient
    
    def _perceive(self):
        """Implementação do método abstrato da classe Agent que retorna a perceção do ambiente do jogo"""
        event = self.__game_ambient.observe()
        return GamePerception(event)

    def _act(self, action):
        """Implementação do método abstrato da classe Agent que executa a ação do ambiente do jogo"""
        self.__game_ambient.execute(action.command)