
import pygame
import math

class Coletaveis:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.raio = 5
        self.cor = (255, 255, 255) 
        self.consumido = False

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


