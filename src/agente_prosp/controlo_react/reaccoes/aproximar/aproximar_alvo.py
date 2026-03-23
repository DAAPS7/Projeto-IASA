from ecr.prioridade import Prioridade

class AproximarAlvo(Prioridade):
    """
    Caso seja disparado o estímulo do alvo, este comportamento composto é 
    responsável por gerar uma resposta para mover o agente através da classe 
    de aproximação direcional

    Serão criadas 4 instâncias de aproximação direcional, que dinamicamente vão
    se alterar para poder se aproximar do alvo detetado pelo estímulo
    """