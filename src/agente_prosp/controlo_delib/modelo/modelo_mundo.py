from .operador_mover import OperadorMover
from sae.ambiente.direccao import Direccao
import math
from .estado_agente import EstadoAgente
from sae.ambiente.elemento import Elemento

class ModeloMundo:
    """
    Classe que representa o modelo do mundo.
    O modelo do mundo é a representação interna que o agente
    mantém sobre o ambiente onde atua.
    Permite reagir ao presente e antecipar estados futuros.

    Atributos
    ---------
    self.__alterado : Boolean
        Atributo que indica se o modelo do mundo foi alterado
    self.__estado : EstadoAgente
        Estado do agente
    self.__estados : List<EstadoAgente>
        Lista de estados do agente
    self.__elementos : Dict<Elemento, Posicao>
        Dicionário de elementos associados a posições
    self.__operadores : List<OperadorMover>
        Lista de operadores de movimento
    """

    def __init__(self):
        """
        Construtor da classe do modelo do mundo que inicializa os 
        atributos.
        """
        self.__alterado = False
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]

    def __contains__(self, estado):
        """
        O método __contains__ permite verificar se um dado 
        estado pertence à lista de estados armazenado no atributo
        self.__estados.

        Parâmetros
        ----------
        estado : EstadoAgente
            Estado a verificar se existe em self.__estados
        
        Retorna
        : boolean
            Retornar True caso o estado esteja em self.__estados,
            caso contrário, retornar False
        """
        return estado in self.__estados

    def obter_estado(self):
        """
        Retorna o estado atual do agente armazenado no atributo
        self.__estado.

        Retorna
        -------
        : EstadoAgente
            Estado atual do agente
        """
        return self.__estado
    
    def obter_estados(self):
        """
        Retorna a lista de estados armazenada no atributo
        self.__estados.

        Retorna
        -------
        : List<EstadoAgente>
            Lista de estados do agente
        """
        return self.__estados
    
    def obter_operadores(self):
        """
        Retorna a lista de operadores de movimento armazenada
        no atributo self.__operadores.

        Retorna
        -------
        : List<OperadorMover>
            Lista de operadores de movimento
        """
        return self.__operadores
    
    def obter_elemento(self, estado):
        """
        Retorna o elemento associado ao estado do agente.
        Como é utilizado o método 'get', caso este não 
        exista, retorna None.

        Parâmetros
        ----------
        estado : EstadoAgente
            Estado a obter do dicionário de elementos
        
        Retorna
        -------
        : Elemento
            Elemento associado à posição do estado passado
        """
        return self.__elementos.get(estado.posicao)
    
    def distancia(self, estado):
        """
        Calcula e retorna a distância entre o agente e a posição
        do estado recebido como parâmetro.

        Parâmetros
        ----------
        estado : EstadoAgente
            Estado a comparar ao estado do agente
        
        Retorna
        -------
        dist : double
            Distância entre o agente e a posição do estado
        """
        return math.dist(estado.posicao, self.__estado.posicao)
    
    def actualizar(self, percepcao):
        """
        Atualiza o modelo do mundo alterando o estado atual do
        agente para uma nova instância de EstadoAgente com a 
        posição atual do agente obtida através da perceção,
        atualiza o valor do atributo self.__alterado, o 
        dicionário de elementos e a lista de estados para serem
        correspondentes às da perceção.
        """
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__alterado = self.__elementos != percepcao.elementos

        if self.__alterado:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
    
    def mostrar(self, vista):
        """
        Invoca o método de mostrar elemento da vista com os 
        elementos que são alvos ou obstáculos.

        Parâmetros
        ----------
        vista : VistaAmb
            Vista do ambiente
        """
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        
        vista.marcar_posicao(self.__estado.posicao)
    
    @property
    def alterado(self):
        """
        Propriedade pública read-only do atributo self.__alterado

        Retorna
        self.__alterado : boolean
            Atributo que indica se o modelo do mundo foi alterado
        """
        return self.__alterado
    
    @property
    def elementos(self):
        """
        Propriedade pública read-only do dicionário de elementos

        Retorna
        self.__elementos : Dict<Elemento, Posicao>
            Dicionário de elementos associados a posições
        """
        return self.__elementos