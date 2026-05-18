from agente_prosp.agente_prosp import AgenteProsp
from agente_prosp.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae import Simulador

"""Caso este seja o módulo que está a ser executado"""
if __name__ == "__main__":
    """
    Instancia um agente prospetor que recebe por parâmetro uma nova instância do controlo deliberativo,
    que por sua vez, recebe por parâmetro uma instância de um planeador, neste caso, o planeador de procura
    em espaço de estados.
    """
    planeador = PlaneadorPEE()
    controlo = ControloDelib(planeador)
    agente = AgenteProsp(controlo)
    
    """
    É criada uma instância do simulador, que faz parte da biblioteca SAE, e passam-se o número de
    ambiente, a instância do agente prospetor como parâmetros e o parâmetros vista_modelo a True.

    Finalmente executamos o simulador
    """
    simulador = Simulador(1, agente, vista_modelo=True)
    simulador.executar()