from ecr.comportamento import Comportamento
from agente_prosp.accoes.rodar import Rodar
from agente_prosp.accoes.avancar import Avancar
from sae import Direccao
from random import random, choice

class Explorar(Comportamento):
    """
    Este comportamento tem o propósito de colocar o agente reativo a explorar o ambiente

    Atributos
    ---------
    self.__prob_rotacao : float
        Probabilidade de rotação do agente
    """

    def __init__(self, prob_rotacao=0.7):
        """
        Construtor do comportamento de exploração

        Parâmetros
        ----------
        prob_rotacao : float
            Probabilidade de rotação do agente, 0.7 por omissão
        """
        self.__prob_rotacao = prob_rotacao
    
    def activar(self, percepcao):
        """
        Baseado na probabilidade de rotação, escolhe entre a ação de avançar e de rodar

        Escolhe uma direção aleatória através do método choice() do módulo random

        O parâmetro percepcao não é utilizado

        Retorna
        -------
        accao : Accao
            Ação escolhida probabilisticamente
        """

        if random() < self.__prob_rotacao:
            """Escolhe um valor aleatório entre 0 e 1 e roda caso este seja menor que 0.7"""
            
            """Transforma o enumerado de direções numa lista"""
            lista_direccoes = list(Direccao)
            """Escolhe um dos elementos da lista aleatoriamente"""
            dir_aleatoria = choice(lista_direccoes)

            """Instancia a ação de rodar com a direção escolhida aleatoriamente"""
            accao = Rodar(dir_aleatoria)
        else:
            """Caso o valor aleatório seja maior ou igual a 0.7, escolhe a ação de avançar"""
            accao = Avancar()

        return accao