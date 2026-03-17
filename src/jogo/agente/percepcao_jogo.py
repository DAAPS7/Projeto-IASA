from agente.percepcao import Percepcao

class PercepcaoJogo(Percepcao):
    """
    Classe que implementa a interface Perception e representa a perceção do jogo
    
    Atributos
    ---------
    __evento : EventoJogo
        Instância privada de um evento de jogo do enumerado EventoJogo
    """
    
    def __init__(self, evento):
        """
        Construtor da classe da perceção de jogo

        Parâmetros
        ----------
        evento : EventoJogo
            Evento de jogo associado à perceção do jogo
        """
        self.__evento = evento

    @property
    def evento(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        __evento : EventoJogo
            Atributo privado (self.__evento)
        """
        return self.__evento