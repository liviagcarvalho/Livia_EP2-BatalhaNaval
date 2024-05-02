#BATALHA NAVAL: JOGO FINAL 

##############################################################################################################################################
#   CONSTANTES  #

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

ALFABETO = 'ABCDEFGHIJ'

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

##############################################################################################################################################
#   FUNÇÕES OBRIGATÓRIAS  #

import random

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

##############################################################################################################################################
#   OUTRAS FUNÇÕES  #

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

    # Função para o jogador real alocar seus navios
def aloca_navios_humano(mapa, nome_pais):
    for tipo_navio, quantidade in PAISES[nome_pais].items():
        print(f"Aloque os navios do tipo {tipo_navio}:")
        for i in range(quantidade):
            sucesso = False
            while not sucesso:
                imprime_mapa(mapa)
                print(f"\nAlocação do {i+1}º {tipo_navio}")
                linha = input("Digite o número da linha (1 a 10): ")
                if not linha.isdigit() or int(linha) < 1 or int(linha) > 10:
                    print("Linha inválida, tente novamente.")
                else:
                    linha = int(linha) - 1
                    coluna = input("Digite a letra da coluna (A a J): ").upper()
                    if coluna not in ALFABETO:
                        print("Coluna inválida, tente novamente.")
                    else:
                        coluna = ALFABETO.index(coluna)
                        orientacao = input("Digite a orientação do navio (v para vertical, h para horizontal): ").lower()
                        if posicao_suporta(mapa, CONFIGURACAO[tipo_navio], linha, coluna, orientacao):
                            if orientacao == 'v':
                                for j in range(linha, linha + CONFIGURACAO[tipo_navio]):
                                    mapa[j][coluna] = 'N'
                            else:
                                for j in range(coluna, coluna + CONFIGURACAO[tipo_navio]):
                                    mapa[linha][j] = 'N'
                            sucesso = True
                        else:
                            print("Posição inválida, tente novamente.")

    # Função para o jogador real realizar um ataque
def ataque_humano(mapa):
    sucesso = False
    while not sucesso:
        imprime_mapa(mapa)
        print("\nAtaque:")
        linha = input("Digite o número da linha (1 a 10): ")
        if not linha.isdigit() or int(linha) < 1 or int(linha) > 10:
            print("Linha inválida, tente novamente.")
        else:
            linha = int(linha) - 1
            coluna = input("Digite a letra da coluna (A a J): ").upper()
            if coluna not in ALFABETO:
                print("Coluna inválida, tente novamente.")
            else:
                coluna = ALFABETO.index(coluna)
                if mapa[linha][coluna] == ' ':
                    print("Água!")
                    mapa[linha][coluna] = 'O'
                    sucesso = True
                elif mapa[linha][coluna] == 'N':
                    print("Acertou um navio!")
                    mapa[linha][coluna] = 'X'
                    sucesso = True
                else:
                    print("Já atacou essa posição, tente novamente.")

    # Função para o jogador computador realizar um ataque
def ataque_computador(mapa):
    sucesso = False
    while not sucesso:
        linha = random.randint(0, len(mapa)-1)
        coluna = random.randint(0, len(mapa)-1)
        if mapa[linha][coluna] == ' ':
            print("O computador atacou: ", ALFABETO[coluna] + str(linha+1))
            print("Água!")
            mapa[linha][coluna] = 'O'
            sucesso = True
        elif mapa[linha][coluna] == 'N':
            print("O computador atacou: ", ALFABETO[coluna] + str(linha+1))
            print("Acertou um navio!")
            mapa[linha][coluna] = 'X'
            sucesso = True

# Função para escolher aleatoriamente o país do computador
def escolher_pais_computador():
    return random.choice(list(PAISES.keys()))

# Função para imprimir a lista de países
def imprime_paises():
    print("Escolha seu país:")
    for i, (pais, navios) in enumerate(PAISES.items(), 1):
        print(f"{i}: {pais}")
        for tipo_navio, quantidade in navios.items():
            print(f"{quantidade} {tipo_navio}")
        print()

##############################################################################################################################################
#   Colocando o jogo para funcionar!  #

def batalha_naval():
    print("\033[1;30;47m======================================\033[m")
    print("\033[1;30;47m|                                    |\033[m")
    print("\033[1;30;47m|   \033[1;35m Bem-vindo ao Batalha Naval (:  \033[1;30;47m |\033[m")
    print("\033[1;30;47m|                                    |\033[m")
    print("\033[1;30;47m =====================================\033[m")
    nome_pais_computador = escolher_pais_computador()
    print(f"Computador está alocando os navios de guerra do país {nome_pais_computador}...")
    print("Computador está pronto para jogar!")
    mapa_jogador = cria_mapa(10)
    mapa_computador = cria_mapa(10)
    imprime_paises()
    escolha = int(input("Qual o número da nação da sua frota? "))
    while escolha < 1 or escolha > len(PAISES):
        print("Escolha inválida, tente novamente.")
        escolha = int(input("Qual o número da nação da sua frota? "))
    nome_pais_jogador = list(PAISES.keys())[escolha - 1]
    aloca_navios_humano(mapa_jogador, nome_pais_jogador)
    aloca_navios(mapa_computador, [CONFIGURACAO[tipo] for tipo in PAISES[random.choice(list(PAISES.keys()))].keys()])
    jogador_venceu = False
    computador_venceu = False
    vez_jogador = random.choice([True, False])
    print("Preparando para iniciar o jogo:")
    for i in range(5, 0, -1):
        print(i)
    print("Iniciando o jogo...")
    while not jogador_venceu and not computador_venceu:
        if vez_jogador:
            print("\nSua vez de atacar!")
            ataque_humano(mapa_computador)
            if foi_derrotado(mapa_computador):
                jogador_venceu = True
        else:
            print("\nVez do computador atacar!")
            ataque_computador(mapa_jogador)
            if foi_derrotado(mapa_jogador):
                computador_venceu = True
        vez_jogador = not vez_jogador
    print("\nJogo encerrado!")
    if jogador_venceu:
        print(f"Parabéns! Você venceu representando o país {nome_pais}!")
    else:
        print("Você perdeu! O computador venceu.")

    # EXECUÇÃO DO JOGO
if __name__ == "__main__":
    batalha_naval() 