#  ----------------------------------------------------------
#  item
#  Classe CORE para Player  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
from pyGameEngine.core.entity import entity
from pyGameEngine.components.extends.renderer.text import text
#
# Player
#
class item(entity):
    #
    # properties
    #
    x = 0
    y = 0
    textItem = ''
    textColor = (255,255,255)
    textFont = None
    textSize = 25
    #
    # __init__
    #     
    def __init__(self, x, y, textItem, action, textColor=(255,255,255), textFont=None, textSize=25):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.textItem = textItem
        self.textColor = textColor
        self.textFont = textFont
        self.textSize = textSize
        self.action = action
        self.renderer = text(x, y, textItem, textColor, textFont, textSize)
    #
    # handle_event
    #    
    def handle_event(self, event):
        pass                    
    #
    # update
    #      
    def update(self):
        self.renderer = text(self.x, self.y, self.textItem, self.textColor, self.textFont, self.textSize) 
    #
    # render
    #    
    def render(self, screen):
        self.renderer.render(screen)