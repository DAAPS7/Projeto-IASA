from abc import ABC, abstractmethod

class Agente(ABC):
    """
    Classe abstrata que representa um agente autónomo

    Atributos
    ---------
    _controlo : Controlo
        Instância da classe Controlo protegida
    """
    
    def __init__(self, controlo):
        """
        Construtor da classe de agente

        Parâmetros
        ----------
        controlo : Controlo
            Instância da classe Controlo
        """
        self._controlo = controlo

    @abstractmethod
    def _percepcionar(self):
        """
        Método protegido abstrato de instância que retorna a perceção do ambiente
        """

    @abstractmethod
    def _actuar(self, accao):
        """
        Método protegido abstrato de instância que executa a ação do ambiente
        
        Parâmetros
        ----------
        accao : Accao
            Instância da classe Accao
        """

    def executar(self):
        """
        Método público de instância que executa a ação prdouzida pelo controlo do agente

        Invoca o método protegido que perceciona

        Invoca o método do controlo que retorna uma ação e, se a mesma existir, invoca o método de atuar com a ação obtida
        """

        percepcao = self._percepcionar()
        accao = self._controlo.processar(percepcao)
        if accao is not None:
            self._actuar(accao)