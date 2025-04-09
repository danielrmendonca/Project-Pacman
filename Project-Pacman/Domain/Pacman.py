import pygame, sys, random
from Protagonista import Protagonista 
from Coletaveis import *
from Perseguidor import Perseguidor
from Labirinto import LABIRINTO
from Spawn import SpawnManager
from Botao import Botao

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

# Definições menu
FUNDO_MENU = pygame.image.load("ativos/fundo_menu.png")
FUNDO_MENU = pygame.transform.scale(FUNDO_MENU, (LARGURA, ALTURA))
def fonte(tamanho):
    return pygame.font.Font("ativos/PressStart2P-Regular.ttf", tamanho)

# Inicialização do jogador
def encontrar_posicao_inicial():
    for y in range(len(LABIRINTO)):
        for x in range(len(LABIRINTO[y])):
            if LABIRINTO[y][x] == 2:
                return x * LARGURA_CELULA + LARGURA_CELULA // 2, y * LARGURA_CELULA + LARGURA_CELULA // 2
    return LARGURA // 2, ALTURA // 2  

def jogar():
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
    monitores = []
    spawn_manager = SpawnManager()
    buff_velocidade = []
    buffonmap = False

    for y in range(len(LABIRINTO)):
        for x in range(len(LABIRINTO[y])):
            pos_x = x * LARGURA_CELULA + LARGURA_CELULA // 2
            pos_y = y * LARGURA_CELULA + LARGURA_CELULA // 2
            
            if LABIRINTO[y][x] == 2:
                moedas.append(Coletaveis(pos_x, pos_y))
                spawn_manager.adicionar_local_moeda(pos_x, pos_y)  # x,y correto
            elif LABIRINTO[y][x] == 3:
                monitores.append(Monitor(pos_x, pos_y))
                spawn_manager.adicionar_local_monitor(pos_x, pos_y)  # x,y correto
                
    pontos = 0
    relogio = pygame.time.Clock()
    jogador_direcao = (0, 0)  

    # ------------------------------- LOOP DO JOGO -------------------------------
    cacada = True
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

        for monitor in monitores[:]:
            if monitor.verificar_colisao(player):
                monitores.remove(monitor)
        
        chance = random.random()
        if chance < 0.3 and not buffonmap:  # 30% de chance
            spawn_manager.tentar_spawn_buff(moedas, monitores, buff_velocidade, buffonmap)


        # Renderização
        tela.fill(PRETO)

        # Desenhar paredes
        for parede in paredes:
            pygame.draw.rect(tela, AZUL, parede)

        # Desenhar moedas
        for moeda in moedas:
            moeda.desenhar(tela)

        if len(buff_velocidade) == 1:
            for buff in buff_velocidade[:]:
                buff.desenhar(tela)
                buffonmap = True

        for buff in buff_velocidade[:]:
            if buff.verificar_colisao(player):
                buff_velocidade.remove(buff)
                buffonmap = False


        for monitor in monitores:
            monitor.desenhar(tela)

        
        # Desenhar jogador
        player.modelo_personagem(tela)

        # Desenhar perseguidor (corrigido o nome do método)
        perseguidor.desenhar(tela)  # Era "desennhar" no seu código original

        pygame.display.flip()
        relogio.tick(60)

def menu():
    menu_ativo = True
    while menu_ativo:
        tela.blit(FUNDO_MENU, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXTO = fonte(75).render("MAT-MAN", True, "#b68f40")
        MENU_POS = MENU_TEXTO.get_rect(center=(LARGURA/2, 100))

        BOTAO_JOGAR = Botao (pos=(LARGURA/2, 250), text_input="JOGAR", font=fonte(45), base_color="#d7fcd4", hovering_color="White")
        BOTAO_SAIR = Botao (pos=(LARGURA/2, 450), text_input="SAIR", font=fonte(45), base_color="#d7fcd4", hovering_color="White")

        tela.blit(MENU_TEXTO, MENU_POS)

        for botao in [BOTAO_JOGAR, BOTAO_SAIR]:
            botao.mudar_cor(MOUSE_POS)
            botao.update_tela(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #clicar no x
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTAO_JOGAR.checar_clique(MOUSE_POS):
                    menu_ativo = False
                    jogar()
                if BOTAO_SAIR.checar_clique(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu()

pygame.quit()
sys.exit()