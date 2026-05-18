from ..plano import Plano

class PlanoPEE(Plano):
    """
    Classe que representa o plano de procura em espaço de
    estados.

    Implementa a interface Plano.

    Atributos
    ---------
    self.__passos : List<PassoSolucao>
        Lista de passos de solução
    """

    def __init__(self, solucao):
        """
        Construtor da classe do plano de procura em espaço de
        estados.

        Parâmetros
        ----------
        solucao : Solucao
            Solução do problema de planeamento
        """
        self.__passos = [passo for passo in solucao]
    
    def obter_accao(self, estado):
        """
        Obtém o passo seguinte dos passos, remove-a da lista
        de passos e verifica se o estado do mesmo passo 
        corresponde ao estado atual para o qual se pretende
        obter a ação. Isto é, o passo do estado está sincronizado
        com a realidade.

        Parâmetros
        ----------
        estado : Estado
            Estado atual do agente

        Retorna
        -------
        : Operador
            Operador da ação do passo
        """
        if self.__passos:
            passo = self.__passos.pop(0)
        
            if passo.estado == estado:
                return passo.operador

    def mostrar(self, vista):
        """
        Mostra os passos na vista do ambiente da
        biblioteca SAE.

        Parâmetros
        ----------
        vista : VistaAmb
            Vista da biblioteca SAE
        """
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao,
                                     passo.operador.ang)