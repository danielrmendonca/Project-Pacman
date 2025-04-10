import pygame

class Protagonista:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.raio = 9
        self.velocidade = 3
        self.cor = (255, 255, 0)

    def modelo_personagem(self, tela):
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), self.raio)

    def mover(self, teclas, paredes):
        dx = 0
        dy = 0
        
        # Calcula o deslocamento com base nas teclas
        if teclas[pygame.K_LEFT]:
            dx = -self.velocidade
        if teclas[pygame.K_RIGHT]:
            dx = self.velocidade
        if teclas[pygame.K_UP]:
            dy = -self.velocidade
        if teclas[pygame.K_DOWN]:
            dy = self.velocidade

        # Cria a hitbox atual do jogador
        hitbox = pygame.Rect(
            self.x - self.raio,
            self.y - self.raio,
            self.raio * 2,
            self.raio * 2
        )

        # Testa movimento horizontal
        hitbox.x += dx
        for parede in paredes:
            if hitbox.colliderect(parede):
                if dx > 0:  # Movendo para a direita
                    hitbox.right = parede.left
                elif dx < 0:  # Movendo para a esquerda
                    hitbox.left = parede.right
                dx = 0  # Bloqueia o movimento no eixo X

        # Testa movimento vertical
        hitbox.y += dy
        for parede in paredes:
            if hitbox.colliderect(parede):
                if dy > 0:  # Movendo para baixo
                    hitbox.bottom = parede.top
                elif dy < 0:  # Movendo para cima
                    hitbox.top = parede.bottom
                dy = 0  # Bloqueia o movimento no eixo Y

        # Atualiza a posição do jogador para o centro da hitbox
        self.x = hitbox.centerx
        self.y = hitbox.centery

    def limitar_bordas(self, largura_tela, altura_tela):
        self.x = max(self.raio, min(largura_tela - self.raio, self.x))
        self.y = max(self.raio, min(altura_tela - self.raio, self.y))

    def colidiu_com_parede(self, parede):
        ponto_x = max(parede.left, min(self.x, parede.right))
        ponto_y = max(parede.top, min(self.y, parede.bottom))
        distancia = ((self.x - ponto_x)**2 + (self.y - ponto_y)**2)**0.5
        return distancia <= self.raio