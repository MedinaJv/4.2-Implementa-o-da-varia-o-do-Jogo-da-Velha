# Retorna X ou O
def jogador(tabuleiro):
    return 'X' if tabuleiro.count('X') == tabuleiro.count('O') else 'O'

# Retorna todas as jogadas disponíveis
def acoes(tabuleiro):
    return [i for i, marca in enumerate(tabuleiro) if marca == ' ']

# Retorna o tabuleiro que resulta ao fazer uma jogada do vetor de ações
def resultado(tabuleiro, acao):
    novo_tabuleiro = list(tabuleiro)
    novo_tabuleiro[acao] = jogador(tabuleiro)
    return novo_tabuleiro

# Retorna o ganhador, se houver
def ganhador(tabuleiro):
    linhas = [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15), (0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15), (0, 5, 10, 15), (3, 6, 9, 12)]
    for linha in linhas:
        if tabuleiro[linha[0]] == tabuleiro[linha[1]] == tabuleiro[linha[2]] == tabuleiro[linha[3]] != ' ':
            return tabuleiro[linha[0]]
    return None

# Retorna Verdadeiro se o jogo acabou, Falso caso contrário
def final(tabuleiro):
    return ganhador(tabuleiro) or ' ' not in tabuleiro

# Retorna 1 se X ganhou, -1 se O ganhou, 0 caso contrário.
def custo(tabuleiro):
    vencedor = ganhador(tabuleiro)
    if vencedor == 'X':
        return 1
    elif vencedor == 'O':
        return -1
    else:
        return 0

# Retorna a jogada ótima para o jogador atual
def minimax(tabuleiro):
    if jogador(tabuleiro) == 'X':
        return maxValor(tabuleiro, float('-inf'), float('inf'))[1]
    else:
        return minValor(tabuleiro, float('-inf'), float('inf'))[1]

def maxValor(tabuleiro, alfa, beta):
    if final(tabuleiro):
        return custo(tabuleiro), None

    valor_max = float('-inf')
    melhor_acao = None

    for acao in acoes(tabuleiro):
        resultado_tabuleiro = resultado(tabuleiro, acao)
        valor, _ = minValor(resultado_tabuleiro, alfa, beta)
        if valor > valor_max:
            valor_max = valor
            melhor_acao = acao
        alfa = max(alfa, valor_max)
        if alfa >= beta:
            break

    return valor_max, melhor_acao

def minValor(tabuleiro, alfa, beta):
    if final(tabuleiro):
        return custo(tabuleiro), None

    valor_min = float('inf')
    pior_acao = None

    for acao in acoes(tabuleiro):
        resultado_tabuleiro = resultado(tabuleiro, acao)
        valor, _ = maxValor(resultado_tabuleiro, alfa, beta)
        if valor < valor_min:
            valor_min = valor
            pior_acao = acao
        beta = min(beta, valor_min)
        if alfa >= beta:
            break

    return valor_min, pior_acao

# Exemplo de uso
tabuleiro_inicial = [' '] * 16

# Preenchendo as DUAS células nas posições predefinidas
tabuleiro_inicial[0] = 'X'
tabuleiro_inicial[4] = 'O'


while not final(tabuleiro_inicial):
    for i in range(4):
        print(tabuleiro_inicial[i*4:(i+1)*4])

    if jogador(tabuleiro_inicial) == 'X':
        acao_jogador = int(input("Digite a posição (0-15) para jogar: "))
        if acao_jogador not in acoes(tabuleiro_inicial):
            print("Jogada inválida. Tente novamente.")
            continue
    else:
        acao_jogador = minimax(tabuleiro_inicial)
    
    tabuleiro_inicial = resultado(tabuleiro_inicial, acao_jogador)

    # Adicionando uma linha em branco após cada jogada
    print()

vencedor_final = ganhador(tabuleiro_inicial)
for i in range(4):
    print(tabuleiro_inicial[i*4:(i+1)*4])

if vencedor_final:
    print(f"\nO jogador {vencedor_final} venceu!")
else:
    print("\nEmpate!")
