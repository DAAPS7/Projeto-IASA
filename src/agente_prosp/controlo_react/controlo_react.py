from agente.controlo import Controlo

class ControloReact(Controlo):
    """
    Classe que representa o controlo do agente reativo

    Implementa a classe Controlo do package agente
    
    Atributos
    ---------
    self.__comportamento : Comportamento
        Comportamento do agente
    """

    def __init__(self, comportamento):
        """
        Construtor da classe do controlo do agente reativo

        Parâmetros
        ----------
        comportamento : Comportamento
            Comportamento do agente
        """
        self.__comportamento = comportamento

    def processar(self, percepcao):
        """
        Processa a perceção através do atributo da classe do comportamento

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção a ser processada
        
        Retorna
        -------
        self.__comportamento.activar(percepcao) : Accao
            Ação retornada pelo método de ativar do comportamento
        """

        return self.__comportamento.activar(percepcao)