from agente.controlo import Controlo
from .mec_delib import MecDelib
from .modelo.modelo_mundo import ModeloMundo

class ControloDelib(Controlo):
    """
    Classe que representa o controlo deliberativo, ou seja,
    controlo sobre o raciocínio deliberativo que se baseia em
    representações de conhecimento do domínio do problema.

    Atributos
    ---------
    self.__planeador : Planeador
        Planeador do raciocínio
    self.__modelo_mundo : ModeloMundo
        Modelo mundo
    self.__mec_delib : MecDelib
        Mecanismo de deliberação
    self.__objectivos : List<EstadoAgente>
        Lista de objetivos
    self.__plano : Plano?
        Plano do raciocínio?
    """

    def __init__(self, planeador):
        """
        Construtor da classe de controlo deliberativo.
        Inicializa o modelo mundo e o mecanismo de deliberação.
        
        Parâmetros
        ----------
        planeador : Planeador
            Planeador de raciocínio
        """
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__objectivos = []
        self.__plano = None

    def processar(self, percepcao):
        """
        Processa a perceção e retorna uma ação

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção do ambiente

        Retorna
        -------
        accao : Accao
            Ação do agente
        """
    
    def assimilar(self, percepcao):
        """
        Método que atualiza o modelo do mundo passando a perceção
        do ambiente.

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção do ambiente
        """
        self.__modelo_mundo.actualizar(percepcao)
    
    def __reconsiderar(self):
        """
        Reavalia as opções caso o modelo mundo tenha sido alterado
        ou o plano não exista.

        Retorna
        -------
        : boolean
            Retorna True caso seja necessário deliberar e planear
        """
        return self.__modelo_mundo.alterado or not self.__plano
    
    def __deliberar(self):
        """
        Gera os objetivos a concretizar, a partir do mecanismo de
        deliberação.
        """
        self.__objectivos = self.__mec_delib.deliberar()
    
    def __planear(self):
        """
        Método que realiza o processo de planeamento.
        """
    
    def __executar(self):
        """
        Executa.
        """
    
    def __mostrar(self):
        """
        Mostra.
        """