from ecr.prioridade import Prioridade
from .aproximar_dir import AproximarDir
from sae import Direccao

class AproximarAlvo(Prioridade):
    """
    Caso seja disparado o estímulo do alvo, este comportamento composto é 
    responsável por gerar uma resposta para mover o agente através da classe 
    de aproximação direcional

    Serão criadas 4 instâncias de aproximação direcional, que dinamicamente vão
    se alterar para poder se aproximar do alvo detetado pelo estímulo
    """

    def __init__(self):
        """
        Utilizando um gerador, gera-se uma lista de instâncias de AproximarDir passando todas as direções
        do enumerado dinamicamente

        Desta forma é mais concisa para gerar o comportamento composto e passar como parâmetro da classe 
        parente (Prioridade)
        """
        super().__init__([AproximarDir(direccao) for direccao in Direccao])