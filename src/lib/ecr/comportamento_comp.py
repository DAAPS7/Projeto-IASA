from .comportamento import Comportamento
from abc import abstractmethod

class ComportamentoComp(Comportamento):
    """
    Classe que representa um comportamento composto

    Atributos
    ---------
    self.__comportamentos : List<Comportamento>
        Lista de comportamentos internos
    """

    def __init__(self, comportamentos):
        """
        Construtor da classe do comportamento composto

        Parâmetros
        ----------
        comportamentos : List<Comportamento>
            Lista de comportamentos internos
        """

        self.__comportamentos = comportamentos
    
    def activate(self, percepcao):
        """
        Percorre os comportamentos individuais, recebe todas as ações e invoca o método de seleção de ação

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção para ativar comportamentos internos

        Retorna
        -------
        accao : Accao
            Ação individual selecionada pelo método seleccionar_accao
        """
        accoes = []

        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)

            if accao is not None:
                accoes.append(accao)
        
        if accoes:
            accao = self.seleccionar_accao(accoes)

        return accao
    
    @abstractmethod
    def seleccionar_accao(self, accoes):
        """
        Método abstrato que obriga subclasses a implementarem a sua própria lógica
        de seleção de ação, permitindo polimorfismo onde diferentes agentes 
        respondem ao mesmo método seleccionar_accao() de forma específica

        Na linguagem do diagrama UML, é distinguido um método abstrato por estar escrito em
        itálico
        
        Abstração: define o contrato (o que fazer) sem implementação (como fazer)
        Polimorfismo: com a mesma interface podem existir várias implementações diferentes

        Parâmetros
        ----------
        accoes : List<Accao>
            Lista de ações a selecionar

        Retorna
        -------
        accao : Accao
            Ação selecionada
        """