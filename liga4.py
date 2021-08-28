from enum import Enum
import pygame
import time


pygame.init()
font = pygame.font.SysFont('arial', 25)

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)


HEIGTH = 480
WIDTH = 640
DIMENSOES = (HEIGTH, WIDTH)

TAMANHO_TABULEIRO = 355
TAMANHO_PECA = 45
SPEED = 20

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



class Liga4:
    def __init__(self):
        self.h = TAMANHO_TABULEIRO
        self.w = TAMANHO_TABULEIRO
        
        self.display = pygame.display.set_mode((self.w, self.h))
        
        pygame.display.set_caption('Liga 4')

        self.clock = pygame.time.Clock()
        
        self.jogador_atual = Jogadores.JOGADOR1
    
    def play_step(self):
        return '',''
    
    def jogada(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        
        self.mostrarTablueiro()
        pygame.display.update()
        self.clock.tick(SPEED)

        acabou, vencedor = self.verificarVitoria()
        return acabou, vencedor

    def mostrarTablueiro(self):
        self.display.fill(PRETO)
        
        pygame.draw.rect(self.display, AMARELO, pygame.Rect(
                0,
                0,
                TAMANHO_TABULEIRO,
                TAMANHO_TABULEIRO))
        
        x_peca = 5
        for linha in TABULEIRO:
            y_peca = 5
            
            for casa in linha:
                if casa == 1:
                    cor = AZUL
                elif casa == 2:
                    cor = VERMELHO
                else: cor = PRETO
                
                pygame.draw.rect(self.display, cor, pygame.Rect(
                    y_peca,
                    x_peca,
                    TAMANHO_PECA,
                    TAMANHO_PECA))

                y_peca += TAMANHO_PECA + 5
            x_peca += TAMANHO_PECA + 5
            
    def verificarVitoria(self):
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
        
if __name__ == '__main__':
    game = Liga4()

    while True:
        game.jogada()
