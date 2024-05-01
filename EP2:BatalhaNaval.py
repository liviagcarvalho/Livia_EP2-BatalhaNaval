#BATALHA NAVAL: JOGO FINAL 

#CONSTANTES
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

import random
# FUNÇÕES OBRIGATÓRIAS
# Cria matriz quadrada de espaços
def cria_mapa(N):
    mapa = []
    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(' ')
        mapa.append(linha)
    return mapa

# Navio pode ser alocado na posição?
def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    if linha < 0 or coluna < 0 or linha >= len(mapa) or coluna >= len(mapa):
        return False
    if orientacao not in ['v', 'h']:
        return False
    if orientacao == 'v':
        if linha + blocos > len(mapa):
            return False
        for i in range(linha, linha + blocos):
            if mapa[i][coluna] != ' ':
                return False
    elif coluna + blocos > len(mapa):
        return False
    else:
        for j in range(coluna, coluna + blocos):
            if mapa[linha][j] != ' ':
                return False
    return True

# Alocando navios para o computador
def aloca_navios(mapa, blocos):
    n = len(mapa)
    for navio in blocos:
        alocando_navio = False
        while not alocando_navio:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            if posicao_suporta(mapa, navio, linha, coluna, orientacao):
                if orientacao == 'v':
                    for i in range(linha, linha + navio):
                        mapa[i][coluna] = 'N'
                else:
                    for j in range(coluna, coluna + navio):
                        mapa[linha][j] = 'N'
                alocando_navio = True
    return mapa

# Verifica se acabou os 'N's da matriz
def foi_derrotado(matriz):
    for linha in matriz:
        if 'N' in linha:
            return False
    return True

# Função para imprimir o mapa
def imprime_mapa(mapa):
    N = len(mapa)
    print("   " + "  ".join([ALFABETO[i] for i in range(N)]))
    for i in range(N):
        print(f"{i+1:2} ", end="")
        for j in range(N):
            if mapa[i][j] == ' ':
                print(CORES['cyan'] + mapa[i][j] + CORES['reset'], end="  ")
            elif mapa[i][j] == 'X':
                print(CORES['red'] + mapa[i][j] + CORES['reset'], end="  ")
            else:
                print(CORES['yellow'] + mapa[i][j] + CORES['reset'], end="  ")
        print(f" {i+1}")
    print("   " + "  ".join([ALFABETO[i] for i in range(N)]))