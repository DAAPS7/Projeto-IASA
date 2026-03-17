from enum import Enum

class EstadoPersonagem(Enum):
    """
    Enumerado dos estados da personagem
    """

    PROCURA = 1
    INSPECCAO = 2
    OBSERVACAO = 3
    REGISTO = 4
