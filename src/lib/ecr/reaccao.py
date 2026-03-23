from .comportamento import Comportamento

class Reaccao(Comportamento):
    """
    Classe que representa uma reação de um agente reativo

    Associa estímulos a respostas, ou seja, gera a ação do agente

    Atributos
    ---------
    self.__estimulo : Estimulo
        Atributo privado da instância da interface Estimulo passada por parâmetro no construtor da classe
    self.__resposta : Resposta
        Atributo privado da instância da classe Resposta passada por parâmetro no construtor da classe
    """

    def __init__(self, estimulo, resposta):
        """
        Construtor da classe de reação
        
        Parâmetros
        ----------
        estimulo : Estimulo
            Instância da interface Estimulo
        resposta : Resposta
            Instância da classe Resposta
        """
        self.__estimulo = estimulo
        self.__resposta = resposta
    
    def activar(self, percepcao):
        """
        Método de ativação da reação do agente reativo

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção do agente
        
        Retorna
        -------
        accao : Accao
            Ação processada pelo agente
        """
        intensidade = self.__estimulo.detectar(percepcao).prioridade

        if intensidade > 0:
            accao = self.__resposta.activar(percepcao, intensidade)
        
        return accao