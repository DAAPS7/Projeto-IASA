from ecr.resposta import Resposta
from agente_prosp.accoes.rodar import Rodar

class RespostaEvitar(Resposta):
    """
    Classe que representa a resposta do agente ao estímulo de evitar um obstáculo
    """

    def _obter_accao(self, percepcao):
        """
        Causa uma rotação no agente caso este encontre um obstáculo

        Parâmetros
        ----------
        percepcao : Percepcao
            Perceção do ambiente
        
        Retorna
        -------
        Rodar(dir_resposta) : Rodar
            Ação de rotação
        """

        dir_agente = percepcao.direccao
        dir_resposta = dir_agente.rodar()

        return Rodar(dir_resposta)