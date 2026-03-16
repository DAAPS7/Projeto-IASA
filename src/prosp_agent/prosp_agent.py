from agent.agent import Agent
import sae

class ProspAgent(Agent):
    """
    Classe que representa um agente prospetor que especializa Agent
    """

    def _perceive(self):
        """
        Método que perceciona um ambiente

        Utiliza a instância já criada do Transdutor da biblioteca SAE

        Aqui é aplicada a delegação, o que significa que foi delegada a execução do método de
        percecionar para a classe ProspAgent

        Retorna
        -------
        perception : Perception
            Perceção do ambiente
        """

        perception = sae.transdutor.percepcionar()

        return perception
    
    def _act(self, action):
        """
        Método que efetua o movimento do agente no ambiente

        Semelhante ao método _perceive, a delegação da execução do método de atuar da classe
        Transdutor, foi passada para este método

        Parâmetros
        ----------
        action : Action
            Ação que também é um movimento devido à herança múltipla que será o movimento a
            efetuar pelo agente
        """
        sae.transdutor.actuar(action)