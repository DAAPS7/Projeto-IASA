from agent.control import Control
from agent.game_action import GameAction
from ambient.game_command import GameCommand
from stamac.state_machine import StateMachine
from character.character_state import CharacterState
from ambient.game_event import GameEvent

class CharacterControl(Control):
    """Classe que representa o controlo da personagem"""

    def __init__(self):
        """
        Construtor da classe do controlo da personagem
        
        Variáveis
        ---------
        seek : GameAction

        approach : GameAction

        observe : GameAction

        photograph : GameAction

        Atributos
        ---------
        __state_machine : StateMachine
            Máquina de estados da personagem
        
        """
        super().__init__()

        seek = GameAction(GameCommand.SEEK)
        approach = GameAction(GameCommand.APPROACH)
        observe = GameAction(GameCommand.OBSERVE)
        photograph = GameAction(GameCommand.PHOTOGRAPH)

        self.__state_machine = StateMachine(
            CharacterState.SEEK,
            [
                (CharacterState.SEEK, GameEvent.ANIMAL, CharacterState.OBSERVATION, approach),
                (CharacterState.SEEK, GameEvent.NOISE, CharacterState.INSPECT, approach),
                (CharacterState.SEEK, GameEvent.SILENCE, CharacterState.SEEK, seek),

                (CharacterState.INSPECT, GameEvent.SILENCE, CharacterState.SEEK),
                (CharacterState.INSPECT, GameEvent.ANIMAL, CharacterState.OBSERVATION, approach),
                (CharacterState.INSPECT, GameEvent.NOISE, CharacterState.INSPECT, seek),

                (CharacterState.OBSERVATION, GameEvent.FLEE, CharacterState.INSPECT),
                (CharacterState.OBSERVATION, GameEvent.ANIMAL, CharacterState.REGISTER, observe),

                (CharacterState.REGISTER, GameEvent.FLEE, CharacterState.SEEK),
                (CharacterState.REGISTER, GameEvent.PICTURE, CharacterState.SEEK),
                (CharacterState.REGISTER, GameEvent.ANIMAL, CharacterState.REGISTER, photograph)
            ]
        )

    @property
    def state(self):
        return self.__state_machine.state
    
    def process(self, perception):
        """Implementação do método abstrato do processamento da perceção do ambiente de jogo"""
        return self.__state_machine.process(perception.event)