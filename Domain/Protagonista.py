import pygame
class Protagonista:
   
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.raio=9
        self.velocidade=6
        self.cor = (255, 255, 0) 

    def modelo_personagem(self,tela):
         pygame.draw.circle(tela, self.cor, (self.x, self.y), self.raio)

    def mover(self, teclas, paredes):
   
        novo_x = self.x
        novo_y = self.y
        
        if teclas[pygame.K_LEFT]: novo_x -= self.velocidade
        if teclas[pygame.K_RIGHT]: novo_x += self.velocidade
        if teclas[pygame.K_UP]: novo_y -= self.velocidade
        if teclas[pygame.K_DOWN]: novo_y += self.velocidade
        
  
        pode_mover_x = True
        pode_mover_y = True
        
       
        for parede in paredes:
            teste_x = pygame.Rect(
                novo_x - self.raio,
                self.y - self.raio,
                self.raio * 2,
                self.raio * 2
            )
            if teste_x.colliderect(parede):
                pode_mover_x = False 
        
      
        for parede in paredes:
            teste_y = pygame.Rect(
                self.x - self.raio,
                novo_y - self.raio,
                self.raio * 2,
                self.raio * 2
            )
            if teste_y.colliderect(parede):
                pode_mover_y = False
        
       
        if pode_mover_x:
            self.x = novo_x
        if pode_mover_y:
            self.y = novo_y
    def limitar_bordas(self, largura_tela, altura_tela):  
        self.x = max(self.raio, min(largura_tela - self.raio, self.x))
        self.y = max(self.raio, min(altura_tela - self.raio, self.y))

    def colidiu_com_parede(self, parede):
  
        ponto_x = max(parede.left, min(self.x, parede.right))
        ponto_y = max(parede.top, min(self.y, parede.bottom))
        
       
        distancia = ((self.x - ponto_x)**2 + (self.y - ponto_y)**2)**0.5
        return distancia <= self.raio 
        