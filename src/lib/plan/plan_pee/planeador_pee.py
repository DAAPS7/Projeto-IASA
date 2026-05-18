from ..planeador import Planeador
from pee.melhor_prim.procura_aa import ProcuraAA
from .mod_prob.problema_plan import ProblemaPlan
from .mod_prob.heur_dist import HeurDist
from .plano_pee import PlanoPEE

class PlaneadorPEE(Planeador):
    """
    Classe que representa um planeador de procura em espaço
    de estados.

    Implementa a interface Planeador.

    Atributos
    ---------
    self.__mec_pee : ProcuraInformada
        Mecanismo de procura informada
    """

    def __init__(self):
        """
        Construtor da classe do planeador de procura em espaço
        de estados.

        Atribui uma instância da procura A* ao atributo do mecanismo
        de procura informada utilizado para o problema de planeamento.
        """
        self.__mec_pee = ProcuraAA()
    
    def planear(self, modelo_plan, objectivos):
        """
        Realiza o mecanismo de planeamento.
        Obtém o objetivo (sendo o primeiro elemento da lista de 
        objetivos), instância o problema de planeamento com o
        modelo de planeamento passado por parâmetro e o objetivo 
        obtido anteriormente, instância uma heurística de distância
        com o mesmo objetivo, obtém a solução através do mecanismo
        de procura em espaço de estados e finalmente retorna uma
        instância do plano de procura em espaço de estados com a 
        solução passada como parâmetro.

        Parâmetros
        ----------
        modelo_plan : ModeloPlan
            Modelo de planeamento
        objectivos : List<Estado>
            Lista de objetivos
        
        Retorna
        -------
        : PlanoPEE
            Plano de ação com base na solução obtida
        """
        objectivo = objectivos[0]
        problema = ProblemaPlan(modelo_plan, objectivo)
        heuristica = HeurDist(objectivo)

        solucao = self.__mec_pee.procurar(problema, heuristica)

        return PlanoPEE(solucao)