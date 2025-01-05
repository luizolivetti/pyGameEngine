#  ----------------------------------------------------------
#  Text
#  Classe Extend para Entity Text  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
from pyGameEngine.core.entity import entity
from pyGameEngine.components.extends.renderer.text import text
#
# Player
#
class label(entity):
    #
    # properties
    #
    x = 0
    y = 0
    textOption = ''
    textColor = (255,255,255)
    textFont = None
    textSize = 25
    #
    # __init__
    #     
    def __init__(self, x, y, textOption, textColor=(255,255,255), textFont=None, textSize=25):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.textOption = textOption
        self.textColor = textColor
        self.textFont = textFont
        self.textSize = textSize
        self.renderer = text(x, y, textOption, textColor, textFont, textSize)   
    #
    # handle_event
    #    
    def handle_event(self, event):
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