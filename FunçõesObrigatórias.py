    #FUNÇÕES OBRIGATÓRIAS 
#Cria matriz quadrada de espaços
def cria_mapa(N):
    mapa = []
    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(' ')
        mapa.append(linha)
    return mapa

#Navio pode ser alocado na posição?
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

#Alocando navios para o computador
import random
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

#Verifica se acabou os 'N's da matriz
def foi_derrotado(matriz):
    for linha in matriz:
        if 'N' in linha:
            return False
    return True