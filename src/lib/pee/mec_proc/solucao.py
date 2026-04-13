from .passo_solucao import PassoSolucao

class Solucao:
    """
    Classe iterável e indexável
    """

    def __init__(self, no_final):
        """Construtor"""
        self.__dimensao = no_final.profundidade
        self.__custo = no_final.custo
        self.__passos = []

        no = no_final
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0, passo) # inserir na posição 0 para a lista ficar bem ordenada

            no = no.antecessor
    
    def __iter__(self):
        return iter(self.__passos)

    def __getitem__(self, index):
        return self.__passos[index]

    @property
    def dimensao(self):
        return self.__dimensao
    
    @property
    def custo(self):
        return self.__custo
