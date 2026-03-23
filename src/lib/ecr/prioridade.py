from comportamento_comp import ComportamentoComp

class Prioridade(ComportamentoComp):
    """
    Comportamento composto responsável pela implementação prioritária da seleção
    de um conjunto de ações individuais
    """

    def seleccionar_accao(self, accoes):
        """
        Seleciona a ação com a maior prioridade obtida na propriedade da ação

        Parâmetros
        ----------
        accoes : List<Accao>
            Lista de ações a ser processada

        Retorna
        -------
        accao_seleccionada : Accao
            Ação de maior prioridade
        """

        if accoes:
            """
            A função lambda serve para criar uma função anónima, curta e inline, para fazer operações simples sem 
            definir uma função completa. Recebe argumentos antes dos dois pontos e devolve o resultado da 
            expressão que vem depois dos mesmos. É útil para simplificar este tipo de contextos em que se utiliza
            um critério especial na funcionalidade 'max'.
            """
            accao_seleccionada = max(accoes, key=lambda accao: accao.prioridade)

        return accao_seleccionada