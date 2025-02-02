#  ----------------------------------------------------------
#  Draw
#  Classe CORE para Draw Elements
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# from
# 
from pyGameEngine.components.renderer import renderer
#
# draw
# 
class draw(renderer):
    #
    # __init__
    #
    def __init__(self, rect):
        self.x = rect.x
        self.y = rect.y
        self.rect = rect
        self.shape = None
    #
    # rectAlpha
    #
    def rectAlpha(self, color):
        if self.rect.width > 0 and self.rect.height > 0:
            self.shape = pygame.Surface(pygame.Rect(self.rect).size, pygame.SRCALPHA)
            pygame.draw.rect(self.shape, color, self.shape.get_rect())
            # surface.blit(self.shape, self.rect)
    #
    # circleAlpha
    #
    def circleAlpha(self, surface, color, center, radius):
        target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape_surf, color, (radius, radius), radius)
        surface.blit(shape_surf, target_rect)
    #
    # polygonAlpha
    #
    def polygonAlpha(self, surface, color, points):
        lx, ly = zip(*points)
        min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
        target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
        surface.blit(shape_surf, target_rect)
    #
    # render
    #
    def render(self, screen):
        screen.blit(self.shape, self.rect.topleft)