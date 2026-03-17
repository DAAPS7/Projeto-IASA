class MaquinaEstados:
    """
    Classe que representa a máquina de estados do agente

    Atributos
    ---------
    __tte : Dict<(ESTADO, EVENTO), ESTADO>
        Dicionário que atribui um estado a um tuplo de estado e evento 
        (Tabela de Transição de Estado)
    __tae : Dict<(ESTADO, EVENTO), ACCAO>
        Dicionário que atribui um evento a um tuplo de estado e evento
        (Tabela de Ação de Estado)
    """

    def __init__(self, estado_inicial, transicoes=None):
        """
        Construtor da classe que representa uma máquina de estados

        Preenche os dicionários com as tables de transição e ação de estado com 
        a lista de tuplos de transições do parâmetro do construtor.

        Parâmetros
        -----------
        estado_inicial : Estado
            Estado inicial da máquina de estados
        transicoes : List<Tuple>
            Lista de tuplos que representam as transições (padrão é None)
        """

        self.__tte = {}
        self.__tae = {}
        self.__estado = estado_inicial

        # Caso a transição não tenha 4 elementos (terá 3), junta um None para que tenha 4
        if(transicoes):
            for transicao in transicoes:
                estado_ant, evento, estado_suc, accao = transicao \
                if len(transicao) == 4 else transicao + (None,)

                self.definir_transicao(estado_ant, evento, estado_suc, accao)

    @property
    def estado(self):
        """
        Propriedade pública read-only

        Retorna
        -------
        __estado : EstadoPersonagem
            Atributo privado (self.__estado)    
        """
        return self.__estado
    
    def definir_transicao(self, estado_ant, evento, estado_suc, accao=None):
        """
        Preenche as tabelas de transição de estado e de ação de estado baseado nos parâmetros do estado

        Verifica se 'accao' não é None para evitar problemas com ações cujo valor é 0 na conversão para bool pelo interpretador

        Parâmetros
        ----------
        estado_ant : EstadoPersonagem
            Estado antecessor da personagem
        evento : EventoJogo
            Evento do jogo
        estado_suc : EstadoPersonagem
            Estado sucessor da personagem
        accao : AccaoJogo
            Ação de jogo
        """

        self.__tte[(estado_ant, evento)] = estado_suc
        if accao is not None:
            self.__tae[(estado_ant, evento)] = accao
                
    def processar(self, evento):
        """
        Obtém a ação e o estado seguintes a partir das tabelas de transição

        Atualiza o estado atual da personagem

        Retorna
        -------
        accao : AccaoJogo
            Ação do jogo obtida na tabela
        """

        accao = self.__tae.get((self.__estado, evento))
        estado_suc = self.__tte.get((self.__estado, evento))

        if estado_suc is not None:
            self.__estado = estado_suc

        return accao