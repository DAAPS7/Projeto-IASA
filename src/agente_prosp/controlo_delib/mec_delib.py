from sae.ambiente.elemento import Elemento

class MecDelib:
    """
    Classe que representa o mecanismo de deliberação.
    É responsável pela geração e seleção de objetivos.

    Atributos
    ---------
    self.__modelo_mundo : ModeloMundo
        Modelo do mundo
    """

    def __init__(self, modelo_mundo):
        """
        Construtor da classe do mecanismo de deliberação.

        Parâmetros
        ----------
        modelo_mundo : ModeloMundo
            Modelo do mundo
        """
        self.__modelo_mundo = modelo_mundo
    
    def deliberar(self):
        """
        Gera os objetivos possíveis, seleciona os objetivos a concretizar
        e retorna-os.

        Retorna
        -------
        objectivos : List<EstadoAgente>
            Lista de objetivos selecionados
        """
        objectivos = self.__gerar_objectivos()
        
        if objectivos:
            return self.__seleccionar_objectivos(objectivos)
    
    def __gerar_objectivos(self):
        """
        Obtém a lista de estados do modelo mundo, filtra os alvos, gera
        uma lista de alvos e retorna-a.

        Retorna
        -------
        : List<EstadoAgente>
            Lista de objetivos
        """
        return [estado for estado in self.__modelo_mundo.obter_estados() \
                if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
    
    def __seleccionar_objectivos(self, objectivos):
        """
        Seleciona o objetivo a concretizar, que é o alvo mais próximo, 
        e retorna uma lista com o objetivo.
        """
        objectivos.sort(key=self.__modelo_mundo.distancia)

        return objectivos[:1]
