"""
Como GameEvent também está localizado na package 'ambient', é feito o import a partir do caminho relativo em vez do absoluto.
"""
from .game_event import GameEvent

class GameAmbient:
    """
    Classe que represente o ambiente de jogo
    
    Atributos
    ---------
    __events : Dict[str, GameEvent]
        Dicionário privado de eventos de jogo como chave e GameEvent como valor
    __event : GameEvent
        Instância privada de um evento de jogo do enumerado GameEvent inicializada como 'None'
    """

    def __init__(self):
        """
        Construtor da classe de ambiente de jogo

        Gera um dicionário, iterando o enumerado dos eventos de jogo, em que a chave é o 'char' do evento e o valor é o GameEvent
        """
        self.__events = {event.value: event for event in GameEvent}
        self.__event = None

    @property
    def event(self):
        """
            Propriedade pública read-only

            Esta propriedade @property em Python cria um getter read-only para aceder a um atributo privado da classe. 
            Permite ler self.__event como se fosse um atributo público.

            Retorna
            -------
            __event : GameEvent
                Atributo privado (self.__event)
        """
        return self.__event
    
    def observe(self):
        """
        Observa o ambiente, ou seja, o evento atual em que o jogo se encontra
        
        Retorna
        -------
        __event : GameEvent
            Atributo privado do evento de jogo
        """
        return self.__event

    def execute(self, command):
        """
        Sobre o comando passado por parâmetro, invoca o seu método mostrar, no caso do comando existir
        
        Parâmetros
        ----------
        command : GameCommand
            Comando a ser mostrado
        """
        if command is not None:
            command.display()

    def evolve(self):
        """
        Atribui um valor ao atributo privado de evento a partir do método da classe '__generate_event'

        Mostra o evento introduzido pelo utilizador, caso exista
        """
        self.__event = self.__generate_event()

        if self.__event is not None:
            self.__event.display()

    def __generate_event(self):
        """
        Guarda em variável local o 'char' introduzido pelo utilizador que representa um evento de jogo

        Retorna
        -------
        __events.get(key) : GameEvent
            Evento de jogo atribuído ao 'char' do enumerado
        """
        key = input("\nEvento? ")
        return self.__events.get(key)