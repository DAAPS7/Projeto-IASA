"""
Como EventoJogo também está localizado na package 'ambient', é feito o import a partir do caminho relativo em vez do absoluto.
"""
from .evento_jogo import EventoJogo

class AmbienteJogo:
    """
    Classe que represente o ambiente de jogo
    
    Atributos
    ---------
    __eventos : Dict[str, EventoJogo]
        Dicionário privado de eventos de jogo como chave e EventoJogo como valor
    __evento : EventoJogo
        Instância privada de um evento de jogo do enumerado EventoJogo inicializada como 'None'
    """

    def __init__(self):
        """
        Construtor da classe de ambiente de jogo

        Gera um dicionário, iterando o enumerado dos eventos de jogo, em que a chave é o 'char' do evento e o valor é o EventoJogo
        """
        self.__eventos = {evento.value: evento for evento in EventoJogo}
        self.__evento = None

    @property
    def evento(self):
        """
            Propriedade pública read-only

            Esta propriedade @property em Python cria um getter read-only para aceder a um atributo privado da classe. 
            Permite ler self.__evento como se fosse um atributo público.

            Retorna
            -------
            __evento : EventoJogo
                Atributo privado (self.__evento)
        """
        return self.__evento
    
    def observar(self):
        """
        Observa o ambiente, ou seja, o evento atual em que o jogo se encontra
        
        Retorna
        -------
        __evento : EventoJogo
            Atributo privado do evento de jogo
        """
        return self.__evento

    def executar(self, comando):
        """
        Sobre o comando passado por parâmetro, invoca o seu método mostrar, no caso do comando existir
        
        Parâmetros
        ----------
        comando : ComandoJogo
            Comando a ser mostrado
        """
        if comando is not None:
            comando.mostrar()

    def evoluir(self):
        """
        Atribui um valor ao atributo privado de evento a partir do método da classe '__gerar_evento'

        Mostra o evento introduzido pelo utilizador, caso exista
        """
        self.__evento = self.__gerar_evento()

        if self.__evento is not None:
            self.__evento.mostrar()

    def __gerar_evento(self):
        """
        Guarda em variável local o 'char' introduzido pelo utilizador que representa um evento de jogo

        Retorna
        -------
        __eventos.get(chave) : EventoJogo
            Evento de jogo atribuído ao 'char' do enumerado
        """
        chave = input("\nEvento? ")
        return self.__eventos.get(chave)