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
    # __init__
    #     
    def __init__(self, x, y, textOption, textColor=(255,255,255), textFont=None, textSize=25):
        super().__init__(x, y, 0, 0)
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
    def handleEvent(self, event):
        pass       
    #
    # update
    #      
    def update(self):
        super().update()   
    #
    # render
    #    
    def render(self, screen):
        self.renderer.render(screen)