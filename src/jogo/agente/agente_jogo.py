from agente.agente import Agente
from .percepcao_jogo import PercepcaoJogo

class AgenteJogo(Agente):
    """
    Classe que representa o agente do jogo e herda da classe 'Agente'

    Atributos
    ---------
    __ambiente_jogo : AmbienteJogo
        Instância privada do ambiente de jogo
    """
    
    def __init__(self, ambiente_jogo, controlo):
        """
        Construtor da classe de agente de jogo

        Chama o construtor da classe parente a partir do método super() e passa a variável 'controlo' como argumento
        
        Parâmetros
        ----------
        ambiente_jogo : AmbienteJogo
            Instância passada do ambiente de jogo
        controlo : ControloPersonagem
            Instância passada do controlo da personagem
        """

        super().__init__(controlo)
        self.__ambiente_jogo = ambiente_jogo
    
    def _percepcionar(self):
        """
        Implementação do método abstrato da classe Agente

        Observa o ambiente de jogo para receber o evento e criar uma perceção de jogo

        Retorna
        -------
        percepcao_jogo : PercepcaoJogo
            Perceção do ambiente de jogo
        """
        evento = self.__ambiente_jogo.observar()
        percepcao_jogo = PercepcaoJogo(evento)
        return percepcao_jogo

    def _actuar(self, accao):
        """
        Implementação do método abstrato da classe Agente

        Executa o ambiente de jogo a partir do comando de jogo da ação passada como parâmetro

        Parâmetros
        ----------
        accao : AccaoJogo
            Ação de jogo
        """
        self.__ambiente_jogo.executar(accao.comando)