# tte - tabela de transição de estado -> stt - state transition table
# tae - tabela de ação de estado -> sat - state action table

class StateMachine:

    def __init__(self, initial_state, transitions=None):
        """
        Construtor da classe que representa uma máquina de estados.
        Preenche também os dicionários com as tables de transição e ação de estado com a lista de tuplos de transições do parâmetro do construtor.

        Parâmetros
        -----------
        initial_state : State
            Estado inicial da máquina de estados
        transitions : List<Tuple>
            Lista de tuplos que representam as transições (padrão é None)
        
        Atributos
        ---------
        __stt : Dict<(STATE, EVENT), STATE>
            Dicionário que atribui um estado a um tuplo de estado e evento
        __sat : Dict<(STATE, EVENT), ACTION>
            Dicionário que atribui um evento a um tuplo de estado e evento
        """

        self.__stt = {}
        self.__sat = {}
        self.__state = initial_state
        self.__transitions = transitions


        # Caso a transição não tenha 4 elementos (terá 3), junta um None para que tenha 4
        if(transitions):
            for transition in transitions:
                last_state, event, next_state, action = transition \
                if len(transition) == 4 else transition + (None,)

                self.define_transition(last_state, event, next_state, action)

    @property
    def state(self):
        return self.__state
    
    def define_transition(self, last_state, event, next_state, action=None):
        """Preenche as tabelas de transição de estado e de ação de estado baseado nos parâmetros do estado"""

        self.__stt[(last_state, event)] = next_state
        if action is not None:
            self.__sat[(last_state, event)] = action
                
    def process(self, event):
        """Atualiza o estado da máquina e retorna a ação"""

        action = self.__sat.get((self.__state, event))
        next_state = self.__stt.get((self.__state, event))

        if next_state is not None:
            self.__state = next_state

        return action