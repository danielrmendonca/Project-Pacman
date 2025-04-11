from Coletaveis import Coletaveis
import pygame

class Buff_velocidade(Coletaveis):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.raio = 8
        self.cor = (0, 0, 255)
        self.sprite_size = (20, 20)
    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), self.raio)