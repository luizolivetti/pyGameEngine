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
# Class text Extends renderer
#
class text(renderer):
    #
    # properties
    #
    textObject=None
    textValue=0
    textColor=0
    textFont=0
    textSize=0
    textX=0
    textY=0
    position=0
    #
    # initialization
    #
    def __init__(self, x, y, textValue, textColor=(255,255,255), textFont=None, textSize=25):
        # Original size
        pygame.font.init()
        self.textValue=textValue
        self.textColor=textColor
        self.textFont=pygame.font.Font(textFont, textSize)
        self.textSize=textSize
        self.textX=x
        self.textY=y
        self.position = (x, y)
        self.textObject = self.textFont.render(self.textValue, True, self.textColor)
    #
    # getWidth
    #
    def getWidth(self):
        self.textObject.get_width()
    #
    # rendering
    #
    def render(self, screen):
        screen.blit(self.textObject, self.position)

        