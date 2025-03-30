import pygame
import sys
from Protagonista import Protagonista 
from Coletaveis import Coletaveis
from Perseguidor import Perseguidor
from Labirinto import LABIRINTO

pygame.init()

# Configurações
LARGURA_CELULA = 30  
LARGURA = len(LABIRINTO[0]) * LARGURA_CELULA
ALTURA = len(LABIRINTO) * LARGURA_CELULA
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pac-Man")

# Cores
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)

# Inicialização do jogador
def encontrar_posicao_inicial():
    for y in range(len(LABIRINTO)):
        for x in range(len(LABIRINTO[y])):
            if LABIRINTO[y][x] == 2:
                return x * LARGURA_CELULA + LARGURA_CELULA // 2, y * LARGURA_CELULA + LARGURA_CELULA // 2
    return LARGURA // 2, ALTURA // 2  

player_x, player_y = encontrar_posicao_inicial()
player = Protagonista(player_x, player_y)

# Inicialização do perseguidor
perseguidor = Perseguidor(170, 200)  # Agora é um único objeto, não uma lista

# Criação das paredes
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

# Criação das moedas
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

jogador_direcao = (0, 0)  

while cacada:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            cacada = False

  
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador_direcao = (-1, 0)
    elif teclas[pygame.K_RIGHT]:
        jogador_direcao = (1, 0)
    elif teclas[pygame.K_UP]:
        jogador_direcao = (0, -1)
    elif teclas[pygame.K_DOWN]:
        jogador_direcao = (0, 1)

    player.mover(teclas, paredes)
    player.limitar_bordas(LARGURA, ALTURA)

    perseguidor.perseguir(player.x, player.y, paredes,LARGURA,ALTURA)

 
    for moeda in moedas[:]:  
        if moeda.verificar_colisao(player):
            pontos += 10
            moedas.remove(moeda)

    # Renderização
    tela.fill(PRETO)

    # Desenhar paredes
    for parede in paredes:
        pygame.draw.rect(tela, AZUL, parede)

    # Desenhar moedas
    for moeda in moedas:
        moeda.desenhar(tela)

    # Desenhar jogador
    player.modelo_personagem(tela)

    # Desenhar perseguidor (corrigido o nome do método)
    perseguidor.desenhar(tela)  # Era "desennhar" no seu código original

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()