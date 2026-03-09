from agent.perception import Perception

class GamePerception(Perception):
    """Classe que implementa a interface Perception e representa a perceção do jogo"""
    
    def __init__(self, event):
        self.__event = event

    @property
    def event(self):
        """Propriedade pública que retorna o atributo privado (self.__event) em read-only"""
        return self.__event