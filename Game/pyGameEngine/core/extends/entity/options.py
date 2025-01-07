#  ----------------------------------------------------------
#  Options
#  Classe CORE para Options  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
from pyGameEngine.core.entity import entity
from pyGameEngine.core.extends.entity.item import item
#
# Player
#
class options(entity):
    #
    # __init__
    #     
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.currentItem = 0
        self.items = []        
    #
    # addItem 
    #
    def addItem(self, textItem, action, textColor=(255, 255,255), textFont=None, textSize=25):
        self.items.append(item(self.x, (self.y+(20*len(self.items))), textItem, action, textColor, textFont, textSize))
    #
    # selected
    #
    def selected(self, itemIndex):
        self.currentItem = itemIndex
    #
    # focusUp
    #
    def focusUp(self):
        #self.options[self.itemIndex].selected = False
        self.itemIndex = (self.itemIndex + 1) % len(self.options)
        #self.options[self.itemIndex].selected = True
    #
    # focusDown
    #
    def focusDown(self):
        #self.options[self.itemIndex].selected = False
        self.itemIndex = (self.itemIndex - 1) % len(self.options)
        #self.options[self.itemIndex].selected = True         
    #
    # handle_event
    #    
    def handle_event(self, event):
        pass       
    #
    # update
    #      
    def update(self):
        for item in self.items:
            item.update()
    #
    # render
    #    
    def render(self, screen):
        for item in self.items:
            item.render(screen)   