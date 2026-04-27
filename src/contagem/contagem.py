from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.melhor_prim.procura_informada import ProcuraInformada
from mod_prob.heuristica_contagem import HeuristicaContagem
from mod_prob.problema_contagem import ProblemaContagem

"""
Problema da contagem:

Dado um valor inicial, um valor final e um conjunto de incrementos possíveis, que
incrementos realizar para atingir ou superar o valor final.

Para observar o efeito do custo na procura, o custo dos operadores corresponde
ao quadrado do incremento.
"""

"""
Módulo da aplicação do problema da contagem.
"""

"""
Inicialização das constantes iniciais do problema.
"""
MECANISMOS_PROCURA = [
    ProcuraProfundidade(),
    ProcuraLargura(),
    ProcuraProfLim(),
    ProcuraProfIter(),
    ProcuraCustoUnif(),
    ProcuraAA(),
    ProcuraSofrega()
]

VALOR_INICIAL = 0
VALOR_FINAL = 8
INCREMENTOS = [1, 2, 3]
INCREM_CICLO = [1, 2, 3, -1]

def teste_contagem(valor_inicial, valor_final, incrementos, mecanismos_procura):
    print()
    print("Valor inicial: ", valor_inicial)
    print("Valor final: ", valor_final)
    print("Incrementos: ", incrementos)

    """Problema formulado com os valores definidos"""
    problema = ProblemaContagem(valor_inicial, valor_final, incrementos)

    """Corre o problema com os diferentes mecanismos de procura implementados"""
    for mec_proc in mecanismos_procura:
        if isinstance(mec_proc, ProcuraInformada):
            """Cria heurística"""
            heuristica = HeuristicaContagem(valor_final)
            """Procura solução passando o problema e a heurística criada"""
            solucao = mec_proc.procurar(problema, heuristica)
        else:
            """Sem heurística, procura a solução ao problema"""
            solucao = mec_proc.procurar(problema)
        
        print()
        print("Mecanismo de Procura: ", mec_proc.__class__.__name__)
        print("Solução: ", [passo.operador.incremento for passo in solucao])
        print("Dimensão: ", solucao.dimensao)
        print("Custo: ", solucao.custo)


"""Corre o teste do problema sem ciclos"""
print("\nTeste sem ciclos")
teste_contagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS, MECANISMOS_PROCURA)

"""Corre o teste do problema com ciclos"""
print("\nTeste com ciclos")
# Remove o mecanismo de procura em profundidade porque este não irá acabar com um ciclo
teste_contagem(VALOR_INICIAL, VALOR_FINAL, INCREM_CICLO, MECANISMOS_PROCURA[1:])