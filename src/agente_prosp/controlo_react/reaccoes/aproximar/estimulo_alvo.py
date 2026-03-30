from sae import Elemento
from ecr.estimulo import Estimulo

class EstimuloAlvo(Estimulo):

    def __init__(self, direccao, gama=0.9):
        self.__direccao = direccao
        self.__gama = gama
    
    def detectar(self, percepcao):
        """
        Retorna a intensidade a qual o alvo está a ser detetado

        """
        elemento, distancia, _ = percepcao[self.__direccao]

        """Retorna float??????????"""
        return self.__gama ** distancia \
        if elemento == Elemento.ALVO else 0