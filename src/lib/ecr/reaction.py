from .behaviour import Behaviour

class Reaction(Behaviour):
    """
    Classe que representa uma reação de um agente reativo

    Atributos
    ---------
    self.__stimulus : Stimulus
        Atributo privado da instância da interface Stimulus passada por parâmetro no construtor da classe
    self.__response : Response
        Atributo privado da instância da classe Response passada por parâmetro no construtor da classe
    """

    def __init__(self, stimulus, response):
        """
        Construtor da classe de reação
        
        Parâmetros
        ----------
        stimulus : Stimulus
            Instância da interface Stimulus
        response : Response
            Instância da classe Response
        """
        self.__stimulus = stimulus
        self.__response = response
    
    def activate(self, perception):
        """
        Método de ativação da reação do agente reativo

        Parâmetros
        ----------
        perception : Perception
            Perceção do agente
        
        Retorna
        -------
        action : Action
            Ação processada pelo agente
        """
        intensity = self.__stimulus.detect(perception).priority

        if intensity > 0:
            action = self.__response.activate(perception, intensity)
        
        return action