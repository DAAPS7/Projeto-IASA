from abc import abstractmethod

class Estado:
    """
    Classe que representa o estado atual do processo de procura.
    Este estado é a configuração gerada pelo operador que será comparada
    ao objetivo final para determinar se a procura foi resolvida.
    """

    def __hash__(self):
        """
        Como esta classe é hashable, requer um hash para identificar elementos 
        únicos de forma eficiente.
        O hash é calculado a partir do ID único do estado produzido pelo método
        id_valor(), garantindo que estados equivalentes gerem o mesmo valor hash.
        """
        return self.id_valor()

    def __eq__(self, objecto):
        """
        Método de igualdade que compara a instância de Estado passada 
        por parâmetro, com esta instância a partir dos seus hashes (IDs). 
        """
        if isinstance(objecto, Estado):
            return self.__hash__() == objecto.__hash__()

    @abstractmethod
    def id_valor(self):
        """
        Método abstrato que produz uma identificação para poder 
        comparar estados diferentes mas, com configurações idênticas,
        sob a forma de um inteiro.
        """