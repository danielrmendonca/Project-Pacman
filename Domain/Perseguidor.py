import pygame
import math

class Perseguidor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.raio = 9
        self.velocidade = 6
        self.cor = (255, 0, 0)  
    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, (self.x, self.y), self.raio)

    def mover(self, jogador_x, jogador_y, paredes):
        
        dx = jogador_x - self.x
        dy = jogador_y - self.y
        distancia = max(1, math.hypot(dx, dy))  
        dx, dy = dx/distancia, dy/distancia  

        novo_x = self.x + dx * self.velocidade
        novo_y = self.y + dy * self.velocidade

       
        pode_mover_x = True
        pode_mover_y = True

        for parede in paredes:
            
            area_teste_x = pygame.Rect(
                novo_x - self.raio,
                self.y - self.raio,
                self.raio * 2,
                self.raio * 2
            )
            if area_teste_x.colliderect(parede):
                pode_mover_x = False

          
            area_teste_y = pygame.Rect(
                self.x - self.raio,
                novo_y - self.raio,
                self.raio * 2,
                self.raio * 2
            )
            if area_teste_y.colliderect(parede):
                pode_mover_y = False

        if pode_mover_x:
            self.x = novo_x
        if pode_mover_y:
            self.y = novo_y