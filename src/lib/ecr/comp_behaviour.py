from .behaviour import Behaviour
from abc import abstractmethod

class CompBehaviour(Behaviour):
    """
    Classe que representa um comportamento composto

    Atributos
    ---------
    self.__behaviours : List<Behaviour>
        Lista de comportamentos internos
    """

    def __init__(self, behaviours):
        """
        Construtor da classe do comportamento composto

        Parâmetros
        ----------
        behaviours : List<Behaviour>
            Lista de comportamentos internos
        """

        self.__behaviours = behaviours
    
    def activate(self, perception):
        """
        Percorre os comportamentos individuais, recebe todas as ações e invoca o método de seleção de ação

        Parâmetros
        ----------
        perception : Perception
            Perceção para ativar comportamentos internos

        Retorna
        -------
        action : Action
            Ação individual selecionada pelo método select_action
        """
        actions = []

        for behaviour in self.__behaviours:
            action = behaviour.activate(perception)

            if action is not None:
                actions.append(action)
        
        if actions:
            action = self.select_action(actions)

        return action
    
    @abstractmethod
    def select_action(self, actions):
        """
        Método abstrato que obriga subclasses a implementarem a sua própria lógica
        de seleção de ação, permitindo polimorfismo onde diferentes agentes 
        respondem ao mesmo método select_action() de forma específica

        Na linguagem do diagrama UML, é distinguido um método abstrato por estar escrito em
        itálico
        
        Abstração: define o contrato (o que fazer) sem implementação (como fazer)
        Polimorfismo: com a mesma interface podem existir várias implementações diferentes

        Parâmetros
        ----------
        actions : List<Action>
            Lista de ações a selecionar

        Retorna
        -------
        action : Action
            Ação selecionada
        """