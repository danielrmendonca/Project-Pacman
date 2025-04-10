import pygame
import pytmx
import os

class Labirinto:
    def __init__(self):
        # Configurações
        self.TAMANHO_TILE = 24  # Tamanho de cada célula/tile
        self.LARGURA_TELA = 54 * self.TAMANHO_TILE  # Largura total da tela
        self.ALTURA_TELA = 30 * self.TAMANHO_TILE   # Altura total da tela
        
        # Cores
        self.BLACK = (0, 0, 0)
        self.COLISION_COLOR = (255, 0, 0, 128)  # Vermelho semitransparente
        
        # Caminho do mapa (ainda não carregado)
        self.assets_path = os.path.join(os.path.dirname(__file__), "assets")
        self.map_filename = "mapa_final.tmx"
        self.map_path = os.path.join(self.assets_path, self.map_filename)
        self.dados_tmx = None  # O mapa será carregado posteriormente
    
    def load_tmx_map(self, filename):
        """Carrega o mapa TMX"""
        return pytmx.load_pygame(filename)
    
    def carregar_mapa(self):
        """Método para carregar o mapa após a inicialização da tela"""
        self.dados_tmx = self.load_tmx_map(self.map_path)
    
    def desenhar(self, tela):
        """Desenha o labirinto na tela fornecida pelo Pacman.py"""
        if self.dados_tmx is None:
            return  # Não desenha nada se o mapa ainda não foi carregado
        # Renderiza todas as camadas, exceto a de colisão
        for i, layer in enumerate(self.dados_tmx.layers):
            if isinstance(layer, pytmx.TiledTileLayer):
                if "colisão" not in layer.name.lower():  # Evita desenhar a camada de colisão
                    for y in range(layer.height):
                        for x in range(layer.width):
                            tile = self.dados_tmx.get_tile_image(x, y, i)
                            if tile:
                                tela.blit(tile, (x * self.TAMANHO_TILE, y * self.TAMANHO_TILE))
    def get_matriz_labirinto(self):
        """Retorna uma matriz onde 0 = vazio e 1 = parede"""
        matriz = []
        for y in range(self.dados_tmx.height):
            linha = []
            for x in range(self.dados_tmx.width):
                # Verifica se há tile de colisão na posição (x, y)
                tem_parede = False
                for camada in self.dados_tmx.layers:
                    if isinstance(camada, pytmx.TiledTileLayer) and "colisão" in camada.name.lower():
                        if camada.data[y][x] != 0:
                            tem_parede = True
                            break
                linha.append(1 if tem_parede else 0)
            matriz.append(linha)
        return matriz

if __name__ == "__main__":
    pygame.init()
    labirinto = Labirinto()
    tela = pygame.display.set_mode((labirinto.LARGURA_TELA, labirinto.ALTURA_TELA))
    labirinto.carregar_mapa()  # Carrega o mapa após a tela estar pronta
    pygame.display.set_caption("Teste do Labirinto")
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        tela.fill((0, 0, 0))  # Preenche com preto
        labirinto.desenhar(tela)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()