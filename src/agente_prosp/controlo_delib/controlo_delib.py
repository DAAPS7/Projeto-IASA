from agente.controlo import Controlo
from .mec_delib import MecDelib
from .modelo.modelo_mundo import ModeloMundo
import sae

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
        Realiza o processo de tomada de decisão e ação.

        Atualiza o modelo do mundo, verifica se é necessário
        reconsiderar e se for o caso, delibera e planeia.
        Finalmente executa a ação e retorna-a. 

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção do ambiente

        Retorna
        -------
        accao : Accao
            Ação executada pelo agente
        """

        self.__assimilar(percepcao)

        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        
        accao = self.__executar()
        return accao

    def __assimilar(self, percepcao):
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
        Atualiza o valor do atributo self.__plano caso existam objetivos.
        """
        if self.__objectivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
        else:
            self.__plano = None


    def __executar(self):
        """
        Obtém o estado atual do agente sobre o modelo do mundo,
        obtém o operador sobre o plano de procura e retorna a 
        ação associada ao operador.

        Caso o operador não exista, o plano está dessincronizado
        e, por isso, altera-se o seu valor para None para que volte
        a ser atualizado.

        Retorna
        -------
        : Accao
            Ação do agente
        """
        self.__mostrar()
        
        if self.__plano:
            estado = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado)

            if operador:
                return operador.accao
            
            self.__plano = None
    
    def __mostrar(self):
        """
        Limpa a vista da biblioteca SAE, mostra o modelo do mundo,
        se o plano existir mostra-o e marca as posições na janela 
        da vista nas posições dos objetivos existentes.
        """
        sae.vista.limpar()
        self.__modelo_mundo.mostrar(sae.vista)
        if self.__plano:
            self.__plano.mostrar(sae.vista)
        
        if self.__objectivos:
            for objectivo in self.__objectivos:
                sae.vista.marcar_posicao(objectivo.posicao)