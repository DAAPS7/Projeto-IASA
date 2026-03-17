from ecr.accao import Accao
from sae.agente.movimento import Movimento

class Mover(Movimento, Accao):

    def __init__(self, direccao):
        """
        Construtor da classe de movimento do agente prospetor
        
        Invoca o construtor da super classe Movimento e passa como parâmetro a direção 
        para qual o agente se vai deslocar. Não passa o segundo parâmetro 'passo',
        porque este tem o valor 1 por omissão.

        Parâmetros
        ----------
        direccao : Direccao
            Direção para onde o agente se deslocará 
        """
        super().__init__(direccao)