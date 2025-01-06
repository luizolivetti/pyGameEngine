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
        super().__init__(x, y)
        self.renderer = image(x, y, image_path)
        self.renderer.resize(scale) 
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