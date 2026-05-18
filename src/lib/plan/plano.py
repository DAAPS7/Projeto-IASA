from abc import ABC, abstractmethod

class Plano(ABC):
    """
    Interface de um plano de ação.
    """

    @abstractmethod
    def obter_accao(self, estado):
        """
        Retorna o operador

        Parâmetros
        ----------
        estado : Estado
            Estado atual do agente
        """
    
    @abstractmethod
    def mostrar(self, vista):
        """
        Mostra a vista ambiente?

        Parâmetros
        ----------
        vista : VistaAmb
            Vista do ambiente
        """