from agente_prosp.agente_prosp import AgenteProsp
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.controlo_react.reaccoes.explorar.explorar import Explorar
from agente_prosp.controlo_react.reaccoes.recolher.recolher import Recolher
from sae import Simulador

"""Caso este seja o módulo que está a ser executado"""
if __name__ == "__main__":
    """
    Instancia um agente prospetor que recebe por parâmetro uma nova instância do controlo reativo,
    que por sua vez, recebe por parâmetro uma instância de um comportamento, neste caso, o explorar
    """
    agente = AgenteProsp(ControloReact(Recolher()))
    
    """
    É criada uma instância do simulador, que faz parte da biblioteca SAE, e passam-se o número de
    ambiente e a instância do agente prospetor como parâmetros

    Finalmente executamos o simulador
    """
    simulador = Simulador(1, agente)
    simulador.executar()

    """
    O agente, ao explorar o ambiente, quando colide com um obstáculo fica vermelho.
    
    Esta colisão é definida ao percecionar o ambiente a partir do módulo Transdutor da biblioteca SAE.
    A deteção da perceção a partir de um estímulo vai definir se existe um obstáculo.

    Para evitar as colisões seria necessário adicionar um comportamento de evitar obstáculos.
    """