from agente.agente import Agente
import sae

class AgenteProsp(Agente):
    """
    Classe que representa um agente prospetor que especializa Agente
    """

    def _percepcionar(self):
        """
        Método que perceciona um ambiente

        Utiliza a instância já criada do Transdutor da biblioteca SAE

        Aqui é aplicada a delegação, o que significa que foi delegada a execução do método de
        percecionar para a classe AgenteProsp

        Retorna
        -------
        percepcao : Percepcao
            Perceção do ambiente
        """

        percepcao = sae.transdutor.percepcionar()

        return percepcao
    
    def _actuar(self, accao):
        """
        Método que efetua o movimento do agente no ambiente

        Semelhante ao método _percepcionar, a delegação da execução do método de atuar da classe
        Transdutor, foi passada para este método

        Parâmetros
        ----------
        accao : Accao
            Ação que também é um movimento devido à herança múltipla que será o movimento a
            efetuar pelo agente
        """
        sae.transdutor.actuar(accao)