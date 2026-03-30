from .comportamento_comp import ComportamentoComp
class Hierarquia(ComportamentoComp):
    """
    Comportamento composto responsável pela implementação hierárquica da seleção
    de um conjunto de ações individuais
    """

    def seleccionar_accao(self, accoes):
        """
        Seleciona a ação de maior prioridade que neste caso é a primeira ação da lista
        
        Parâmetros
        ----------
        accoes : List<Accao>
            Lista de ações a ser processada
        
        Retorna
        -------
        accoes[0] : Accao
            Ação selecionada
        """

        if accoes:
            return accoes[0]