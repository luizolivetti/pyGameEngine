#  ----------------------------------------------------------
#  Map
#  Classe CORE para controle de mapa da cena  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# Class log
#
class map :
    #
    # properties
    # 
    gameSurface = None
    scene = None
    matrix = None
    vector = None
    #
    columns = 0
    rows = 0
    origin = 0
    pointToGrid = 0
    #
    # render
    #
    def render(windowHandler):
        colors = {'g': (40, 128, 40), 'd': (90, 60, 40)}
        tilemap = [
            'gdddg',
            'dgddd',
            'ggddg',
            'ggddg',
            'ddddg',
            'dgggd'
        ]
        columns, rows = len(tilemap[0]), len(tilemap)

        isometric_tiles = {}
        for key, color in colors.items():
            tile_surf = pygame.Surface((50, 50), pygame.SRCALPHA)
            tile_surf.fill(color)
            tile_surf = pygame.transform.rotate(tile_surf, 45)
            isometric_size = tile_surf.get_width()
            tile_surf = pygame.transform.scale(tile_surf, (isometric_size, isometric_size//2))
            isometric_tiles[key] = tile_surf
        tile_size = (isometric_size, isometric_size//2)

        gameSurface = pygame.Surface(((columns+rows) * isometric_size // 2, (columns+rows) * isometric_size // 4), pygame.SRCALPHA)
        for column in range(columns):
            for row in range(rows):
                tile_surf = isometric_tiles[tilemap[row][column]]
                tile_rect = map.tileRect(column, row, tile_size)
                gameSurface.blit(tile_surf, tile_rect)

        map_rect = gameSurface.get_rect(center = windowHandler.get_rect().center)
        map_outline = [
            pygame.math.Vector2(0, columns * isometric_size / 4), 
            pygame.math.Vector2(columns * isometric_size / 2, 0),
            pygame.math.Vector2((columns+rows) * isometric_size // 2, rows * isometric_size / 4),
            pygame.math.Vector2(rows * isometric_size / 2, (columns+rows) * isometric_size // 4)
        ]
        for pt in map_outline:
            pt += map_rect.topleft 

        map.origin = map_outline[0]
        x_axis = (map_outline[1] - map_outline[0]) / columns
        y_axis = (map_outline[3] - map_outline[0]) / rows

        map.point_to_grid = map.inverseMat2x2((x_axis, y_axis))


        # marcador de x e y    
        # font = pygame.font.SysFont(None, 30)
        # textO = font.render("O", True, (255, 255, 255))
        # textX = font.render("X", True, (255, 0, 0))
        # textY = font.render("Y", True, (0, 255, 0))
    #
    # inverseMat2x2
    #        
    def inverseMat2x2(m):
        a, b, c, d = m[0].x, m[0].y, m[1].x, m[1].y
        det = 1 / (a*d - b*c)
        return [(d*det, -b*det), (-c*det, a*det)]
    #
    # transform
    #    
    def transform(p, mat2x2):
        x = p[0] * mat2x2[0][0] + p[1] * mat2x2[1][0]
        y = p[0] * mat2x2[0][1] + p[1] * mat2x2[1][1]
        return pygame.math.Vector2(x, y)
    #
    # tileRect
    #        
    def tileRect(column, row, tile_size):
        x = (column + row) * tile_size[0] // 2
        y = ((columns - column - 1) + row) * tile_size[1] // 2 
        return pygame.Rect(x, y, *tile_size)