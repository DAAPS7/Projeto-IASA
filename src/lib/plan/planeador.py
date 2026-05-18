from abc import ABC, abstractmethod

class Planeador(ABC):
    """
    Interface de um planeador.
    Responsável pelo planeamento da simulação de ações.
    Gera um plano de ação.
    """

    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        """
        Realiza o planeamento e retorna o plano.

        Parâmetros
        ----------
        modelo_plan : ModeloPlan
            Modelo de planeamento
        objectivos : List<Estado>
            Lista de objetivos

        Retorna
        -------
        : Plano
            Plano de ação
        """