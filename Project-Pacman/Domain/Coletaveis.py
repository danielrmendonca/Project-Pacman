import pygame
import math
import random
import os
from Spawn import SpawnManager


class Coletaveis:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.raio = 5  # Mantido para colisão
        self.consumido = False

        # Configurações do sprite
        # Tamanho do sprite na tela (ajuste conforme necessário)
        self.sprite_size = (20, 20)

        # Carregar o sprite 'branca.png' com caminho relativo
        sprite_path = os.path.join(os.path.dirname(
            __file__), "..", "sprites", "branca.png")
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(
            self.sprite, self.sprite_size)  # Redimensiona o sprite

    @staticmethod
    def criar_moedas_na_matriz(matriz, tamanho_tile, spawn):
        moedas = []
        for y in range(len(matriz)):
            for x in range(len(matriz[y])):
                if matriz[y][x] == 0:  # Verifica se é chão
                    if random.random() < 0.3:
                        # Calcula a posição central do tile
                        pos_x = x * tamanho_tile + tamanho_tile // 2
                        pos_y = y * tamanho_tile + tamanho_tile // 2
                        moedas.append(Coletaveis(pos_x, pos_y))
                        spawn.adicionar_local_moeda(pos_x, pos_y)
        print(f"Total de moedas criadas: {len(moedas)}")  # Depuração
        return moedas

    def desenhar(self, tela):
        if not self.consumido:
            # Desenha o sprite centralizado em (self.x, self.y)
            tela.blit(
                self.sprite,
                (int(self.x - self.sprite_size[0] // 2),
                 int(self.y - self.sprite_size[1] // 2))
            )

    def verificar_colisao(self, player):
        if self.consumido:
            return False

        distancia = math.sqrt((self.x - player.x)**2 + (self.y - player.y)**2)
        if distancia < (self.raio + player.raio):
            self.consumido = True
            return True
        return False
