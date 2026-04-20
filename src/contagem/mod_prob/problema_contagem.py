from mod.problema import Problema
from .estado_contagem import EstadoContagem
from .operador_incremento import OperadorIncremento

class ProblemaContagem(Problema):
    """
    Especialização da classe do problema para o problema da contagem.

    Atributos
    ---------
    self.__valor_final : int 
        Valor final de contagem
    """

    def __init__(self, valor_inicial, valor_final, incrementos):
        """
        Construtor da classe do problema de contagem.
        Invoca o construtor da super classe inicializando o estado de contagem
        com o seu valor inicial passado como argumento deste construtor e uma
        lista de operadores de incremento com os incrementos da lista do
        parâmetro 'incrementos'.

        Parâmetros
        ----------
        valor_inicial : int
            Valor inicial do estado de contagem
        valor_final : int
            Valor final da contagem
        incrementos : List<int>
            Lista de incrementos possíveis
        """
        super().__init__(EstadoContagem(valor_inicial), 
                         [OperadorIncremento(inc) for inc in incrementos])
        self.__valor_final = valor_final

    def objectivo(self, estado):
        """
        Implementa o método abstrato da super classe, retornando True caso
        a contagem do estado seja superior ou igual ao valor final.
        """
        return estado.contagem >= self.__valor_final