from mod.problema import Problema

class ProblemaPlan(Problema):
    """
    Classe que representa o problema de planeamento.

    Especializa Problema.

    Atributos
    ---------
    self.__estado_final : Estado
        Objetivo final do problema (estado do agente)
    """

    def __init__(self, modelo_plan, estado_final):
        """
        Construtor da classe do problema de planeamento.

        Parâmetros
        ----------
        modelo_plan : ModeloPlan
            Modelo de planeamento
        estado_final : Estado
            Objetivo final do problema (estado do agente)
        """
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final
    
    def objectivo(self, estado):
        """
        Verifica se o estado atual do agente é o estado de objetivo.

        Parâmetros
        ----------
        estado : Estado
            Estado atual do agente

        Retorna
        -------
        : boolean
            True, caso o estado atual seja o estado final, False
            caso contrário
        """
        return estado == self.__estado_final