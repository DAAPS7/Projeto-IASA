from mod.operador import Operador
from agente_prosp.accoes.mover import Mover
from .estado_agente import EstadoAgente
from sae.ambiente.posicao import Posicao
import math

class OperadorMover(Operador):
    """
    Classe que representa o operador de movimento do agente.
    Responsável pela simuação das ações de movimento do agente.
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
        Construtor da classe do operador de movimento do agente.

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
        Aplica a ação do movimento do agente.

        Calcula a diferença das posições entre o estado seguinte
        e o estado atual (dx e dy) e soma-as aos eixos correspondentes
        da posição atual do agente.

        Verifica se a posição calculada é válida, ou seja, pertence ao
        modelo mundo a partir do método __contains__ implementado na
        classe ModeloMundo.

        Retorna um estado com a posição calculada anteriormente.

        Parâmetros
        ----------
        estado : EstadoAgente
            Estado atual do agente

        Retorna
        -------
        estado_suc : EstadoAgente
            Estado seguinte do agente        
        """

        dx = self.__accao.passo * math.cos(self.__ang)
        dy = -self.__accao.passo * math.sin(self.__ang)

        x = dx + estado.posicao[0]
        y = dy + estado.posicao[1]

        estado_suc = EstadoAgente(Posicao((x, y)))

        if estado_suc in self.__modelo_mundo:
            return estado_suc


    def custo(self, estado, estado_suc):
        """
        Retorna o custo do operador com o valor mínimo de 1.

        Parâmetros
        ----------
        estado : EstadoAgente
            Estado atual do agente
        estado_suc : EstadoAgente
            Estado sucessor do agente
        
        Retorna
        -------
        : double
            Custo do operador
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