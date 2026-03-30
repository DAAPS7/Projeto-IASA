from sae import Elemento
from ecr.estimulo import Estimulo

class EstimuloAlvo(Estimulo):
    """
    Classe que representa o estímulo detetado pela presença de um alvo

    Atributos
    ---------
    self.__direccao : Direccao
        Direção atual do agente
    self.__gama : float
        Valor amortecedor da exponencial
    """

    def __init__(self, direccao, gama=0.9):
        """
        Construtor da classe de estímulo do alvo

        Parâmetros
        ----------
        direccao : Direccao
            Direção atual do agente
        gama : float
            Valor amortecedor da exponencial que por omissão tem o valor de 0.9
        """
        self.__direccao = direccao
        self.__gama = gama
    
    def detectar(self, percepcao):
        """
        Retorna a intensidade a qual o alvo está a ser detetado que é exponencialmente definido na
        presença de perceção de um alvo

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção do ambiente
        
        Retorna
        -------
        intensidade : float
            Intensidade do estímulo
        """
        elemento, distancia, _ = percepcao[self.__direccao]

        return self.__gama ** distancia \
        if elemento == Elemento.ALVO else 0