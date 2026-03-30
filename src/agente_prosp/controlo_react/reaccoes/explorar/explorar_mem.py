from ecr.comportamento import Comportamento
from agente_prosp.accoes.avancar import Avancar

class ExplorarMem(Comportamento):
    """
    Classe de comportamento de exploração com memória

    Guarda em memória as posições e direções dos últimos 100 movimentos e
    não altera o movimento caso a situação não seja nova.

    Atributos
    ---------
    self.__dim_max_mem : int
        Valor máximo de situações em memória
    self.__accao : Accao
        Ação de avançar
    self.__memoria : List<Tuple(Posicao, Direccao)>
        Lista das situações em memória
    """

    def __init__(self, dim_max_mem=100):
        """
        Construtor da classe de exploração com memória

        Parâmetros
        ----------
        dim_max_mem : int
            Valor máximo de situações em memória com valor de 100 por omissão
        """
        self.__dim_max_mem = dim_max_mem
        self.__accao = Avancar()
        self.__memoria = []

    def activar(self, percepcao):
        """
        Ativa a ação do agente baseando-se nas situações em memória

        As situações são tuplos com a posição e a direção do agente

        Percorrendo a lista da memória podemos verificar se a situação atual já existe em memória.
        Caso não exista, guarda-se essa situação em memória. Caso exista, retorna-se None.

        Para não exceder o a dimensão máxima de memória retira-se a primeira situação da lista,
        que corresponde à mais antiga, e adiciona-se a atual.

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção do ambiente
        
        Retorna
        -------
        self.__accao : Accao
            Ação a efetuar pelo agente
        """

        situacao = (percepcao.posicao, percepcao.direccao)

        if situacao not in self.__memoria:
            if(len(self.__memoria) >= self.__dim_max_mem):
                self.__memoria.pop(0)

            self.__memoria.append(situacao)

            return self.__accao
        
        return None