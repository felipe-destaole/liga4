from enum import Enum

class Jogadores(Enum):
    JOGADOR1 = 1
    JOGADOR2 = 2

TABULEIRO = [
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
]

JOGADORES = [Jogadores.JOGADOR1, Jogadores.JOGADOR2]

CONTADOR = 0


def mostrarTablueiro():
    for linha in TABULEIRO:
        print(linha)
        
def jogada(jogador: Jogadores, casa):
    casa = int(casa)
    if casa >= len(TABULEIRO):
        print('casa inválida')
        return False
    
    tamanho = len(TABULEIRO) - 1
    
    for i in range(len(TABULEIRO)):
        if TABULEIRO[tamanho-i][casa] == 0:
            TABULEIRO[tamanho-i][casa] = jogador.value
            return True
    print('Esta coluna está cheia!')
    return False

def verificarVitoria():
    """ Verifica se alguem ganhou """
    global CONTADOR
    for i in range(len(TABULEIRO)):
        for j in range(i):
            casa = TABULEIRO[i][j]
            if casa == 0:
                CONTADOR = CONTADOR + 1
                continue
            if j <= 3 and casa == TABULEIRO[i][j+1] == TABULEIRO[i][j+2] == TABULEIRO[i][j+3]:
                CONTADOR = CONTADOR + 1
                return True, casa
            if i <= 3 and casa == TABULEIRO[i+1][j] == TABULEIRO[i+2][j] == TABULEIRO[i+3][j]:
                CONTADOR = CONTADOR + 1
                return True, casa
            if i <= 3 and j <= 3 and casa == TABULEIRO[i+1][j+1] == TABULEIRO[i+2][j+2] == TABULEIRO[i+3][j+3]:
                CONTADOR = CONTADOR + 1
                return True, casa
            if i >= 3 and j < 7 and j <= 3 and casa == TABULEIRO[i-1][j+1] == TABULEIRO[i-2][j+2] == TABULEIRO[i-3][j+3]:
                CONTADOR = CONTADOR + 1
                return True, casa
    return False, ''

def main():
    for i in range(len(TABULEIRO)**2):
        mostrarTablueiro()
        vez = i % 2
        jogou = False 
        while not jogou:
            casa = input(f'Jogada do jogador {int(vez) + 1}: ')
            if casa is None or casa == '': continue
            jogou = jogada(JOGADORES[int(vez)], int(casa) - 1)
        acabou, vencedor = verificarVitoria()
        print(CONTADOR)
        if acabou:
            print(f'Jogador {vencedor} ganhou!')
            mostrarTablueiro()
            break
            
if __name__ == '__main__':    
    main()