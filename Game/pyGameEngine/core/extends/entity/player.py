# ----------------------------------------------------------
# Player
# Classe CORE para Player  
# ----------------------------------------------------------
# @author  Luiz Olivetti     @data 20/12/2024
# @revisor                   @data 
# ----------------------------------------------------------
#
# core
#
from pyGameEngine.core.entity import entity
#
# player extends entity
#
class player(entity):
    #
    # __init__
    #
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
    #
    # update
    #      
    def update(self):
        super().update()
    #
    # render
    #    
    def render(self, screen):
        super().render(screen)         