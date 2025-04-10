
import pygame
import math
import random

class Coletaveis:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.raio = 5
        self.cor = (255, 255, 255)  # Cor branca (pode ajustar)
        self.consumido = False

    @staticmethod
    def criar_moedas_na_matriz(matriz, tamanho_tile):
        moedas = []
        for y in range(len(matriz)):
            for x in range(len(matriz[y])):
                if matriz[y][x] == 0:  # Verifica se é chão
                    # Calcula a posição central do tile
                    pos_x = x * tamanho_tile + tamanho_tile // 2
                    pos_y = y * tamanho_tile + tamanho_tile // 2
                    moedas.append(Coletaveis(pos_x, pos_y))
        return moedas


    def desenhar(self, tela):
        if not self.consumido:
            pygame.draw.circle(tela, self.cor, (self.x, self.y), self.raio)

    def verificar_colisao(self, player):
        if self.consumido:
            return False
            
        distancia = math.sqrt((self.x - player.x)**2 + (self.y - player.y)**2)
        if distancia < (self.raio + player.raio):
            self.consumido = True
            return True
        return False

    
