from agente.controlo import Controlo
from agente.accao_jogo import AccaoJogo
from ambiente.comando_jogo import ComandoJogo
from maqest.maquina_estados import MaquinaEstados
from .estado_personagem import EstadoPersonagem
from ambiente.evento_jogo import EventoJogo

class ControloPersonagem(Controlo):
    """
    Classe que representa o controlo da personagem

    Atributos
    ---------
    __maquina_estados : MaquinaEstados
        Máquina de estados da personagem
    """

    def __init__(self):
        """
        Construtor da classe do controlo da personagem. Chama o construtur da classe parente a partir do método super()
        
        Instancia a máquina de estados, preenchendo a lista de transições com as regras de transição de estado e ação

        Variáveis Locais
        ----------------
        procurar : AccaoJogo
            Ação de jogo de procura
        aproximar : AccaoJogo
            Ação de jogo de aproximação
        observar : AccaoJogo
            Ação de jogo de observação
        fotografar : AccaoJogo
            Ação de jogo de fotografia 
        """
        super().__init__()

        procurar = AccaoJogo(ComandoJogo.PROCURAR)
        aproximar = AccaoJogo(ComandoJogo.APROXIMAR)
        observar = AccaoJogo(ComandoJogo.OBSERVAR)
        fotografar = AccaoJogo(ComandoJogo.FOTOGRAFAR)

        self.__maquina_estados = MaquinaEstados(
            EstadoPersonagem.PROCURA,
            [
                (EstadoPersonagem.PROCURA, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, aproximar),
                (EstadoPersonagem.PROCURA, EventoJogo.RUIDO, EstadoPersonagem.INSPECCAO, aproximar),
                (EstadoPersonagem.PROCURA, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA, procurar),

                (EstadoPersonagem.INSPECCAO, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA),
                (EstadoPersonagem.INSPECCAO, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, aproximar),
                (EstadoPersonagem.INSPECCAO, EventoJogo.RUIDO, EstadoPersonagem.INSPECCAO, procurar),

                (EstadoPersonagem.OBSERVACAO, EventoJogo.FUGA, EstadoPersonagem.INSPECCAO),
                (EstadoPersonagem.OBSERVACAO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, observar),

                (EstadoPersonagem.REGISTO, EventoJogo.FUGA, EstadoPersonagem.PROCURA),
                (EstadoPersonagem.REGISTO, EventoJogo.FOTOGRAFIA, EstadoPersonagem.PROCURA),
                (EstadoPersonagem.REGISTO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, fotografar)
            ]
        )

    @property
    def estado(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        __maquina_estados.estado : EstadoPersonagem
            Estado atual obtido pela máquina de estados
        """
        return self.__maquina_estados.estado
    
    def processar(self, percepcao):
        """
        Implementação do método abstrato do processamento da perceção do ambiente de jogo

        Processa a perceção para obter a ação de jogo
        
        Retorna
        -------
        accao : AccaoJogo
            Ação atual do jogo
        """
        accao = self.__maquina_estados.processar(percepcao.evento)

        return accao