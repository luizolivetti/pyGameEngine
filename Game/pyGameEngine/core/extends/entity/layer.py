#  ----------------------------------------------------------
#  layer
#  Classe CORE para layer  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
from pyGameEngine.core.entity import entity
from pyGameEngine.components.extends.renderer.image import image
#
# layer
#
class layer(entity):
    #
    # __init__
    #     
    def __init__(self, x, y, image_path, scale):
        super().__init__(x, y, 0, 0)
        self.setImage(image_path, scale)
        self.width = self.renderer.imageWidth
        self.height = self.renderer.imageHeight
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