#  ----------------------------------------------------------
#  Player
#  Classe CORE para Player  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
from pyGameEngine.core.entity import entity
from pyGameEngine.components.physics import physics
from pyGameEngine.components.extends.renderer.image import image
#
# Player
#
class player(entity):
    #
    # __init__
    #     
    def __init__(self, x, y, image_path, scale):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.renderer = image(x, y, image_path)
        self.renderer.resize(scale)
        self.physics = physics(x, y, self.renderer.imageWidth, self.renderer.imageHeight)
    #
    # move
    # Move o jogador pela mudança dx e dy.
    #      
    def move(self, dx, dy):
        self.renderer.rect.x += dx
        self.renderer.rect.y += dy   
    #
    # do
    #
    def do(self):
        pass
    #
    # focus Up
    #
    def up(self):
        self.move(0,-5)
    #
    # focus Down
    #
    def down(self):
        self.move(0,5)  
    #
    # focus Left
    #
    def left(self):
        self.move(-5,0)   
    #
    # focus Right
    #
    def right(self):
        self.move(5,0)               
    #
    # handle_event
    #    
    def handle_event(self, event):
        pass       
    #
    # update
    #      
    def update(self):
        self.physics.update()    
    #
    # render
    #    
    def render(self, screen):
        self.renderer.render(screen)