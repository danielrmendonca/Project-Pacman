import pygame
import sys
from Protagonista import Protagonista 
from Coletaveis import Coletaveis
from Perseguidor import Perseguidor
from Labirinto import LABIRINTO

pygame.init()


LARGURA_CELULA = 30  
LARGURA = len(LABIRINTO[0]) * LARGURA_CELULA
ALTURA = len(LABIRINTO) * LARGURA_CELULA
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pac-Man")


PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)


def encontrar_posicao_inicial():
    for y in range(len(LABIRINTO)):
        for x in range(len(LABIRINTO[y])):
            if LABIRINTO[y][x] == 2:
                return x * LARGURA_CELULA + LARGURA_CELULA // 2, y * LARGURA_CELULA + LARGURA_CELULA // 2
    return LARGURA // 2, ALTURA // 2  

player_x, player_y = encontrar_posicao_inicial()
player = Protagonista(player_x, player_y)


perseguidores = [
    Perseguidor(150, 200),
    Perseguidor(600, 300)
]


paredes = []
for y in range(len(LABIRINTO)):
    for x in range(len(LABIRINTO[y])):
        if LABIRINTO[y][x] == 1:  
            paredes.append(pygame.Rect(
                x * LARGURA_CELULA,
                y * LARGURA_CELULA,
                LARGURA_CELULA,
                LARGURA_CELULA
            ))


moedas = []
for y in range(len(LABIRINTO)):
    for x in range(len(LABIRINTO[y])):
        if LABIRINTO[y][x] == 2:
            moedas.append(Coletaveis(
                x * LARGURA_CELULA + LARGURA_CELULA // 2,
                y * LARGURA_CELULA + LARGURA_CELULA // 2
            ))

pontos = 0
relogio = pygame.time.Clock()
cacada = True

while cacada:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            cacada = False


    teclas = pygame.key.get_pressed()
    player.mover(teclas, paredes)
    player.limitar_bordas(LARGURA, ALTURA)

  
    for perseguidor in perseguidores:
        perseguidor.mover(player.x, player.y, paredes)

  
    for moeda in moedas[:]:  
        if moeda.verificar_colisao(player):
            pontos += 10
            moedas.remove(moeda)

    
    tela.fill(PRETO)

    
    for parede in paredes:
        pygame.draw.rect(tela, AZUL, parede)

    
    for moeda in moedas:
        moeda.desenhar(tela)

    
    player.modelo_personagem(tela)
    for perseguidor in perseguidores:
        perseguidor.desenhar(tela)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()