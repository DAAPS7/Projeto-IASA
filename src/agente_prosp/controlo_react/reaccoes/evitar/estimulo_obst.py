from ecr.estimulo import Estimulo

class EstimuloObst(Estimulo):

    """
    Constante estática que representa a intensidade do obstáculo

    As variáveis estáticas são definidas para todas as instâncias, sendo relativa à classe e não à instância.
    """
    
    INTENS_OBST = 1

    def detectar(self, percepcao):
        """
        A perceção da biblioteca SAE, possui um método que retorna verdadeiro ou falso
        se estiver em contacto com um obstáculo ou não. A partir de um operador ternário,
        retorna-se a constante estática INTENS_OBST caso este esteja em contacto com um
        obstáculo.

        Retorna
        -------
        intensidade : float
            Intensidade do estímulo
        """
        return EstimuloObst.INTENS_OBST if percepcao.contacto_obst() else 0