import pygame
import os
from Coletaveis import Coletaveis

class Buff_velocidade(Coletaveis):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.raio = 8
        self.cor = (0, 0, 255)  # Cor de fallback (azul)
        self.sprite_size = (24, 24)  # Tamanho do sprite na tela
        
        # Carrega o sprite
        self.sprite = self.carregar_sprite()
        
    def carregar_sprite(self):
        # Define o caminho relativo para o arquivo livro.png
        sprite_path = os.path.join(os.path.dirname(__file__), "..", "..", "sprites", "livro.png")
        
        try:
            sprite = pygame.image.load(sprite_path).convert_alpha()
            return pygame.transform.scale(sprite, self.sprite_size)
        except Exception as e:
            print(f"Erro ao carregar sprite: {sprite_path} - {e}")
            return None
    
    def desenhar(self, tela):
        if self.sprite:
            # Desenha o sprite centralizado na posição do buff
            tela.blit(
                self.sprite,
                (int(self.x - self.sprite_size[0] // 2),
                 int(self.y - self.sprite_size[1] // 2))
            )
        else:
            # Fallback: desenha círculo azul se o sprite não carregou
            pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), self.raio)