from mod.operador import Operador
from .estado_contagem import EstadoContagem

class OperadorIncremento(Operador):
    """
    Especialização da classe de operador para o problema da contagem.

    Atributos
    ---------
    self.__incremento : int
        Incremento associado ao operador
    """

    def __init__(self, incremento):
        """
        Construtor da classe de operador de incremento.

        Parâmetros
        ----------
        incremento : int
            Incremento associado ao operador
        """
        self.__incremento = incremento

    def aplicar(self, estado):
        """
        Retorna um novo estado com valor de contagem correspondente à soma
        do estado atual e o incremento do operador.

        Parâmetros
        ----------
        estado : Estado
            Estado atual
        """
        return EstadoContagem(estado.contagem + self.__incremento)
    
    def custo(self, estado, estado_suc):
        """
        Como definido no problema, o custo dos operadores corresponde 
        ao quadrado do incremento do operador.

        Retorna
        -------
        self.__incremento**2 : double
            Custo do operador
        """
        return self.__incremento ** 2

    @property
    def incremento(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__incremento : int
            Incremento do operador
        """
        return self.__incremento