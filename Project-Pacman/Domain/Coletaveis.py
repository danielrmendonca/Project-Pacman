
import pygame
import math
import random

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


class Monitor(Coletaveis):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.raio = 8
        self.cor = (128, 0, 128)


class Buff_velocidade(Coletaveis):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.raio = 8
        self.cor = (0, 0, 255)

    
