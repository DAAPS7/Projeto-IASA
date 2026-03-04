from game_event import GameEvent

class GameAmbient:
    """Classe que represente o ambiente de jogo"""

    def __init__(self):
        # Gera um dicionário iterando o enumerado dos eventos de jogo em que a chave é o 'char' do evento e o valor é o nome em si
        self.__events = {event.value: event for event in GameEvent}
        self.__event = None

    @property
    def event(self):
        """
            Propriedade pública que retorna o atributo privado (self.__event) em read-only

            Esta propriedade @property em Python cria um getter read-only para aceder a um atributo privado da classe. 
            Permite ler self.__event como se fosse um atributo público.
        """
        return self.__event
    
    def observe(self):
        """Retorna o atributo evento privado"""
        return self.__event

    def execute(self, command):
        """Sobre o comando do parâmetro invoca o método mostrar"""

        # Mostra o comando caso este exista
        if command is not None:
            command.display()

    def evolve(self):
        """Atribui um valor ao atributo privado de evento"""
        self.__event = self.__generate_event()

        # Mostra o evento caso este exista
        if self.__event is not None:
            self.__event.display()

    def __generate_event(self):
        """Obtém um evento a partir do teclado"""
        key = input("\nEvento? ")
        return self.__events.get(key)