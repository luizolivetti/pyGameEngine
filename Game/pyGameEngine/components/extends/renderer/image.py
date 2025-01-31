#  ----------------------------------------------------------
#  Renderer
#  Classe CORE para Renderer  
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
# Class image Extends renderer
#
class image(renderer):
    #
    # initialization
    #
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        # Original size
        self.imageWidth, self.imageHeight = self.image.get_size()      
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    #
    # resize
    #
    def resize(self, scale):
        if scale==0:
            scale=1
        # Resized image
        scaled_width, scaled_height = self.imageWidth // scale, self.imageHeight // scale
        self.image = pygame.transform.scale(self.image, (scaled_width, scaled_height))
        # New size
        self.imageWidth, self.imageHeight = self.image.get_size()   
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
    #
    # rendering
    #
    def render(self, screen):
        screen.blit(self.image, self.rect.topleft)