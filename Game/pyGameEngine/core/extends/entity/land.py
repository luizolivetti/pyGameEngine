#  ----------------------------------------------------------
#  land
#  Classe CORE para controle de land  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 10/01/2025
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# core
#
from pyGameEngine.core.entity import entity
from pyGameEngine.components.extends.renderer.draw import draw
#
# land
#
class land(entity):
    #
    # __init__
    #
    def __init__(self, x, y, width, height, color = (0, 0, 255, 255)):
        super().__init__(x, y, width, height)
        self.color = color
        self.x = x
        self.y = y
    #
    # handle_event
    #    
    def handleEvent(self, event):
        pass       
    #
    # update
    #      
    def update(self):
        pass   
    #
    # render
    #    
    def render(self, screen):
        self.renderer.render(screen)  


  