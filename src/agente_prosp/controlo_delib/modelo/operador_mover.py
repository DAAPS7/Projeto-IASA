from mod.operador import Operador
from accoes.mover import Mover
import math

class OperadorMover(Operador):
    """
    Classe que representa o operador de movimento do agente.
    Realiza a classe Operador.

    Atributos
    ---------
    self.__modelo_mundo : ModeloMundo
        Modelo do mundo
    self.__ang : double
        Ângulo da direção do movimento
    self.__accao : Accao
        Ação do movimento
    """

    def __init__(self, modelo_mundo, direccao):
        """
        Construtor do operador

        Parâmetros
        ----------
        modelo_mundo : ModeloMundo
            Modelo do mundo
        direccao : Direccao
            Direção do movimento 
        """
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value
        self.__accao = Mover(direccao)

    def __repr__(self):
        """
        Método que define a representação da classe em String.
        Neste caso, retorna 'OperadorMover' com a ação da operação
        dentro de parênteses.

        Retorna
        -------
        : String
            String de representação da classe
        """
        return f"OperadorMover({self.accao})"

    def aplicar(self, estado):
        """
        Retorna o estado do agente
        """

    def custo(self, estado, estado_suc):
        """
        Retorna o custo do operador com o valor mínimo de 1.
        """

        return max(math.dist(estado.posicao, estado_suc.posicao), 1)

    @property
    def ang(self):
        """
        Propriedade públic read-only que retorna o ângulo da 
        direção do movimento.

        Retorna
        -------
        self.__ang : double
            Ângulo da direção do movimento
        """
        return self.__ang
    
    @property
    def accao(self):
        """
        Propriedade públic read-only que retorna a ação do
        movimento.

        Retorna
        -------
        self.__accao : Accao
            Ação do movimento
        """
        return self.__accao