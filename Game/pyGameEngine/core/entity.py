#  ----------------------------------------------------------
#  Entity
#  Classe CORE para controle de Entity
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# components
#
from pyGameEngine.components.physics import physics
from pyGameEngine.components.extends.renderer.image import image
#
# entity
#
class entity:
    #
    # __init__
    #
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.physics = None
        self.renderer = None
    #
    # addPhysics
    #
    def setImage(self, imagePath, imageScale):
        self.renderer = image(self.x, self.y, imagePath)
        self.renderer.resize(imageScale)
        self.rect = self.renderer.rect
    #
    # addPhysics
    #
    def togglePhysics(self, velocityX=0, velocityY=0, gravity=0.5, maxVelocityX = 5, maxVelocityY = 10, acceleration = 0.1, friction = 0.9):
        if self.physics:
           self.physics = None
        else:       
           self.physics = physics(self.rect, velocityX, velocityY, gravity, maxVelocityX, maxVelocityY, acceleration, friction)
    #
    # move
    # Atualiza o movimento com base na física
    # Move o entidade usando a física
    #
    def move(self, dx, dy):
        if self.physics:
           self.physics.move(dx, dy)       
    #
    # up (pular)
    #
    def up(self):
        self.move(0, -5)
    #
    # down (descer)
    #
    def down(self):
        self.move(0, 5)  # Movimento de descida, você pode querer algo mais realista aqui
    #
    # left
    #
    def left(self):
        self.move(-5, 0)
    #
    # right
    #
    def right(self):
        self.move(5, 0)
    #
    # jump
    #
    def jump(self, dy):
        if self.physics:
           self.physics.jump()  
    #  
    # update
    # Atualiza a física do jogador (movimento e gravidade)
    #      
    def update(self):
        if self.physics:
           self.physics.update()              
    #  
    # render
    # Renderiza a imagem do jogador
    #      
    def render(self, screen):
        if self.physics and self.renderer:
            self.renderer.rect.topleft = self.physics.rect.topleft
        if self.renderer:
            self.renderer.render(screen)   
    #
    # handle_event
    #    
    def handleEvent(self, event):
        pass                 