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
# Options
#
class options(entity):
    #
    # __init__
    #     
    def __init__(self, x, y, colorMenu=(255,255,255), selectedItem=(255,0,0), textFont=None, textSize=25):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.colorMenu = colorMenu
        self.selectedItem = selectedItem  
        self.textFont = textFont
        self.textSize=textSize   
        self.currentItem = 0
        self.items = []   
    #
    # addItem 
    #
    def addItem(self, textItem, action):
        self.items.append(item(self.x, (self.y+(20*len(self.items))), textItem, action, self.colorMenu, self.textFont, self.textSize))
    #
    # selected
    #
    def selected(self, itemIndex):
        self.items[self.currentItem].textColor = self.colorMenu
        self.items[itemIndex].textColor = self.selectedItem
        self.currentItem = itemIndex
        self.update()
    #
    # do
    #
    def do(self, func):
        return func(self.items[self.currentItem].action)
    #
    # focus Up
    #
    def up(self):
        self.selected((self.currentItem - 1) % len(self.items))
    #
    # focus Down
    #
    def down(self):
        self.selected((self.currentItem + 1) % len(self.items))   
    #
    # focus Left
    #
    def left(self):
        self.up()   
    #
    # focus Right
    #
    def right(self):
        self.down()              
    #
    # handle_event
    #    
    def handleEvent(self, event):
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