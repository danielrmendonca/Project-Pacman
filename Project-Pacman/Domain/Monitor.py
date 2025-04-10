from Coletaveis import Coletaveis

class Monitor(Coletaveis):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.raio = 8
        self.cor = (128, 0, 128)

    @staticmethod
    def criar_monitores_na_matriz(matriz, tamanho_tile):
        monitores = []
        for y in range(len(matriz)):
            for x in range(len(matriz[y])):
                if matriz[y][x] == 2:  # Verifica se é chão
                    # Calcula a posição central do tile
                    pos_x = x * tamanho_tile + tamanho_tile // 2
                    pos_y = y * tamanho_tile + tamanho_tile // 2
                    monitores.append(Monitor(pos_x, pos_y))
        return monitores