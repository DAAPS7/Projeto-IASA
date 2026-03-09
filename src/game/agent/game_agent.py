from agent.agent import Agent
from .game_perception import GamePerception

class GameAgent(Agent):
    """
    Classe que representa o agente do jogo e herda da classe 'Agent'

    Atributos
    ---------
    __game_ambient : GameAmbient
        Instância privada do ambiente de jogo
    """
    
    def __init__(self, game_ambient, control):
        """
        Construtor da classe de agente de jogo

        Chama o construtor da classe parente a partir do método super() e passa a variável 'control' como argumento
        
        Parâmetros
        ----------
        game_ambient : GameAmbient
            Instância passada do ambiente de jogo
        control : CharacterControl
            Instância passada do controlo da personagem
        """

        super().__init__(control)
        self.__game_ambient = game_ambient
    
    def _perceive(self):
        """
        Implementação do método abstrato da classe Agent

        Observa o ambiente de jogo para receber o evento e criar uma perceção de jogo

        Retorna
        -------
        game_perception : GamePerception
            Perceção do ambiente de jogo
        """
        event = self.__game_ambient.observe()
        game_perception = GamePerception(event)
        return game_perception

    def _act(self, action):
        """
        Implementação do método abstrato da classe Agent

        Executa o ambiente de jogo a partir do comando de jogo da ação passada como parâmetro

        Parâmetros
        ----------
        action : GameAction
            Ação de jogo
        """
        self.__game_ambient.execute(action.command)