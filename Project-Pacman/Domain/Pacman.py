import pygame
import sys
import random
import pytmx
import os
from Protagonista import Protagonista 
from Coletaveis import *
from Perseguidor import Perseguidor
from Labirinto import Labirinto
from Spawn import SpawnManager
from Botao import Botao
from Monitor import Monitor
from Buff_velocidade import Buff_velocidade

pygame.init()

labirinto = Labirinto()
TAMANHO_CELULA = labirinto.TAMANHO_TILE
LARGURA = labirinto.LARGURA_TELA
ALTURA = labirinto.ALTURA_TELA
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pac-Man")
labirinto.carregar_mapa()
maze = ''

PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

images_path = os.path.join(os.path.dirname(__file__), "..", "..", "imagens")
FUNDO_MENU = pygame.image.load(os.path.join(images_path, "fundo_menu.jpg"))
FUNDO_MENU = pygame.transform.scale(FUNDO_MENU, (LARGURA, ALTURA))

def carregar_fonte(tamanho):
    return pygame.font.Font(os.path.join(images_path, "PressStart2P-Regular.ttf"), tamanho)

def encontrar_posicao_inicial():
    """Retorna a posição central do mapa"""
    return (LARGURA // 2, ALTURA // 2)  # Centro do mapa: (648, 360)

def desenhar_contador_moedas(tela, quantidade):
    fonte = carregar_fonte(20)
    texto = fonte.render(f"Moedas: {quantidade}", True, BRANCO)
    tela.blit(texto, (LARGURA - texto.get_width() - 20, ALTURA - texto.get_height() - 20))

def jogo_principal():
    pos_x, pos_y = encontrar_posicao_inicial()
    jogador = Protagonista(pos_x, pos_y)
    vidas = 3
    total_moedas = 190

    inimigo = Perseguidor(170, 200)

    paredes = []
    for camada in labirinto.dados_tmx.layers:
        if isinstance(camada, pytmx.TiledTileLayer):
            print(f"Camada encontrada: {camada.name}")
            if "colisão" in camada.name.lower():
                print(f"Camada de colisão encontrada: {camada.name}, tiles: {sum(sum(row) for row in camada.data)}")
                for y in range(camada.height):
                    for x in range(camada.width):
                        if camada.data[y][x] != 0:
                            paredes.append(pygame.Rect(
                                x * TAMANHO_CELULA,
                                y * TAMANHO_CELULA,
                                TAMANHO_CELULA,
                                TAMANHO_CELULA
                            ))
    print(f"Total de paredes: {len(paredes)}")

    matriz = labirinto.get_matriz_labirinto()  # Matriz 2D com 0s e 1s
    print(matriz)

    moedas = []
    itens_especiais = []
    spawner = SpawnManager()
    powerups = []
    powerup_ativo = False

    for camada in labirinto.dados_tmx.layers:
        if isinstance(camada, pytmx.TiledTileLayer):
            if "moedas" in camada.name.lower():
                for y in range(camada.height):
                    for x in range(camada.width):
                        if camada.data[y][x] != 0:
                            pos_x = x * TAMANHO_CELULA + TAMANHO_CELULA // 2
                            pos_y = y * TAMANHO_CELULA + TAMANHO_CELULA // 2
                            moedas.append(Coletaveis(pos_x, pos_y))
                            spawner.adicionar_local_moeda(pos_x, pos_y)
            elif "itens" in camada.name.lower():
                for y in range(camada.height):
                    for x in range(camada.width):
                        if camada.data[y][x] != 0:
                            pos_x = x * TAMANHO_CELULA + TAMANHO_CELULA // 2
                            pos_y = y * TAMANHO_CELULA + TAMANHO_CELULA // 2
                            itens_especiais.append(Monitor(pos_x, pos_y))
                            spawner.adicionar_local_monitor(pos_x, pos_y)

    pontuacao = 0
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        if pontuacao >= total_moedas:
            rodando = False
            continue

        if inimigo.verificar_colisao(jogador):
            vidas -= 1
            if vidas <= 0:
                rodando = False
            else:
                jogador.x, jogador.y = encontrar_posicao_inicial()
                inimigo.x, inimigo.y = 170, 200

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        jogador.mover(teclas, paredes)
        jogador.limitar_bordas(LARGURA, ALTURA)
        inimigo.perseguir(jogador.x, jogador.y, paredes, LARGURA, ALTURA)

        for moeda in moedas[:]:
            if moeda.verificar_colisao(jogador):
                pontuacao += 1
                moedas.remove(moeda)

        for item in itens_especiais[:]:
            if item.verificar_colisao(jogador):
                itens_especiais.remove(item)

        if random.random() < 0.3 and not powerup_ativo:
            spawner.tentar_spawn_buff(moedas, itens_especiais, powerups, powerup_ativo, buff_aplicado= Buff_velocidade)

        tela.fill(PRETO)
        labirinto.desenhar(tela)

        # Removido o desenho das colisões
        # for parede in paredes:
        #     pygame.draw.rect(tela, VERMELHO, parede, 1)

        for moeda in moedas[:]:
            moeda.desenhar(tela)
        for item in itens_especiais:
            item.desenhar(tela)
        for powerup in powerups[:]:
            powerup.desenhar(tela)
            if powerup.verificar_colisao(jogador):
                powerups.remove(powerup)
                powerup_ativo = True

        jogador.modelo_personagem(tela)
        inimigo.desenhar(tela)
        desenhar_contador_moedas(tela, pontuacao)

        pygame.display.flip()
        relogio.tick(60)

def menu_principal():
    ativo = True
    while ativo:
        tela.blit(FUNDO_MENU, (0, 0))
        pos_mouse = pygame.mouse.get_pos()

        titulo = carregar_fonte(70).render("MAT-MAN", True, (182, 143, 64))
        subtitulo = carregar_fonte(24).render("O Labirinto Misterioso", True, (182, 143, 64))
        
        botao_jogar = Botao(
            pos=(LARGURA//2, 250),
            text_input="JOGAR",
            font=carregar_fonte(20),
            base_color=BRANCO,
            hovering_color=AZUL
        )
        
        botao_sair = Botao(
            pos=(LARGURA//2, 325),
            text_input="SAIR",
            font=carregar_fonte(20),
            base_color=BRANCO,
            hovering_color=AZUL
        )

        tela.blit(titulo, titulo.get_rect(center=(LARGURA//2 + 4, 110)))
        tela.blit(subtitulo, subtitulo.get_rect(center=(LARGURA//2 + 4, 160)))

        for botao in [botao_jogar, botao_sair]:
            botao.mudar_cor(pos_mouse)
            botao.update_tela(tela)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ativo = False
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.checar_clique(pos_mouse):
                    ativo = False
                    jogo_principal()
                elif botao_sair.checar_clique(pos_mouse):
                    ativo = False
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu_principal()
pygame.quit()
sys.exit()