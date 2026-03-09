from agent.perception import Perception

class GamePerception(Perception):
    """
    Classe que implementa a interface Perception e representa a perceção do jogo
    
    Atributos
    ---------
    __event : GameEvent
        Instância privada de um evento de jogo do enumerado GameEvent
    """
    
    def __init__(self, event):
        """
        Construtor da classe da perceção de jogo

        Parâmetros
        ----------
        event : GameEvent
            Evento de jogo associado à perceção do jogo
        """
        self.__event = event

    @property
    def event(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        __event : GameEvent
            Atributo privado (self.__event)
        """
        return self.__event