from ecr.accao import Accao
from sae.agente.movimento import Movimento

class Rodar(Movimento, Accao):
    """
    Ação de rotação do agente prospetor que especializa as classes Accao e Movimento (Herança múltipla)

    Ao contrário do Java, o Python permite herança múltipla (Herdar de mais que uma super classe)
    Ao invocar o método super(), podemos especificar qual a super classe a que nos referimos
    No caso de não se especificar, o método super() invoca a primeira super classe na ordem da herança (Neste caso Movimento)
    """

    def __init__(self, direccao):
        """
        Construtor da classe de rotação do agente

        Invoca o construtor da super classe Movimento (por omissão) e como parâmetros passa a direção e o passo,
        que neste caso é 0, para indicar que o agente não se move e apenas roda.

        Parâmetros
        ----------
        direccao : Direccao
            Direção para onde o agente rodará
        """
        super().__init__(direccao, 0)
