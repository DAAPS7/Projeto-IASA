from .passo_solucao import PassoSolucao

class Solucao:
    """
    Classe iterável e indexável que representa a solução do problema
    de procura.

    Atributos
    ---------
    self.__dimensao : int
        Profundidade total da solução
    self.__custo : double
        Custo total da solução
    self.__passos : List<PassoSolucao>
        Lista dos passos de solução
    """

    def __init__(self, no_final):
        """
        Construtor da classe de solução.
        Cria o atributo dos passos de solução e preenche-o com instâncias
        da classe PassoSolucao com o respetivo nó e operador.

        Atributos
        ---------
        no_final : No
            Último nó da solução
        """
        self.__dimensao = no_final.profundidade
        self.__custo = no_final.custo
        self.__passos = []

        no = no_final
        while no.antecessor:
            """
            Como o operador do nó é o operador que o gerou, para obter o 
            operador desse nó, tem de se atribuir o operador do nó seguinte.
            """
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0, passo) # inserir na posição 0 para a lista ficar bem ordenada

            no = no.antecessor
    
    def __iter__(self):
        """
        Permite que objetos Solucao sejam utilizados em loops for e 
        com funções que esperam iteráveis.
        
        Retorna
        -------
        iterator
            Iterador sobre a lista self.__passos
        """
        return iter(self.__passos)

    def __getitem__(self, index):
        """
        Permite acesso aos passos da solução por índice usando a 
        notação de parênteses retos (solucao[0], solucao[1], etc.).
        
        Parâmetros
        ----------
        index : int
            Índice do passo a ser retornado
        
        Retorna
        -------
        PassoSolucao
            Passo da solução na posição index da lista self.__passos
        """
        return self.__passos[index]

    @property
    def dimensao(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__dimensao : int
            Profundidade total da solução
        """
        return self.__dimensao
    
    @property
    def custo(self):
        """
        Propriedade pública read-only
        
        Retorna
        -------
        self.__custo : double
            Custo total da solução
        """
        return self.__custo
