#  ----------------------------------------------------------
#  Window
#  Classe CORE para controle de janelas  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
#
#
from pyGameEngine.core.timer import timer
#
# Class window 
#
class window :
    #
    # properties
    # 
    handler = None
    timer = None
    color = (0,0,0)
    #
    # Setting
    #
    def __init__(self, width, height, title, color):
        self.handler = pygame.display.set_mode((width, height))
        self.background(color)
        self.caption(title)
        self.timer = timer()
    #
    # caption
    #
    def caption(self, text):
        pygame.display.set_caption(text)
    #
    # background
    # 
    def background(self, color) :
        if self.handler is None:
            raise ValueError("The window has not been initialized. Call 'init' first.")
        self.handler.fill(color)
    #
    # getHandler
    #
    def getHandler(self) :
        return self.handler 