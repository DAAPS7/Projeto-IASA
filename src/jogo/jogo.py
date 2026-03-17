from personagem.personagem import Personagem
from ambiente.ambiente_jogo import AmbienteJogo
from ambiente.evento_jogo import EventoJogo

class Jogo:
    """
    Classe de jogo

    Atributos
    ---------
        __ambiente_jogo : AmbienteJogo
            Instância privada do ambiente de jogo
        __personagem : Personagem
            Instância privada da personagem do jogo
    """

    def __init__(self):
        """
        Construtor da classe de jogo.

        Instancia-se primeiro o ambiente de jogo, sendo que a personagem necessita 
        que seja passado um ambiente de jogo como parâmetro de construtor.
                
        É mostrada a personagem após ser instanciada.
        """

        self.__ambiente_jogo = AmbienteJogo()
        self.__personagem = Personagem(self.__ambiente_jogo)
        self.__personagem.mostrar()

    def executar(self):
        """
        Método público que executa o loop de jogo.

        Do while como loop de jogo para correr o jogo pelo menos 1 vez antes de verificar a condição.
        """

        while True:
            self.__ambiente_jogo.evoluir()
            self.__personagem.executar()
            self.__personagem.mostrar()

            if self.__ambiente_jogo.observar() == EventoJogo.TERMINAR:
                break
    
"""
Caso este módulo esteja a ser executado, __name__ recebe '__main__' e cria uma instância da classe Game e executa, 
evitando que isso aconteça quando a classe for importada noutro módulo.
"""
if __name__ == "__main__":
    Jogo().executar()