#  ----------------------------------------------------------
#  Renderer
#  Classe CORE para Renderer  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# Class Renderer
#
class renderer:
    #
    # properties
    #
    x=0
    y=0
    #
    # initialization
    #
    def __init__(self, x, y):
        self.x = x
        self.y = y