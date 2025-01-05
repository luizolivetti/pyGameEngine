#  ----------------------------------------------------------
#  Window
#  Classe CORE para controle de janelas  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# Class window
#
class window :
    #
    # properties
    # 
    handler = None
    #
    # Setting
    #
    def __init__(self, width, height) :
        self.handler = pygame.display.set_mode((width, height))
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