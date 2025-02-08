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
from pyGameEngine.components.extends.renderer.draw import draw
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
    # setImage
    #
    def setImage(self, imagePath, imageScale, color=None):
        self.renderer = image(self.x, self.y, imagePath)
        self.renderer.resize(imageScale)
        if color is not None:
            self.renderer.colorize(color)
        self.rect = self.renderer.rect
    #
    # drawLine
    #
    def drawLine(self):
        self.renderer = draw(self.rect)  
        self.renderer.rectAlpha(self.color)  
    #
    # addPhysics
    #
    def setPhysics(self, velocityX=0, velocityY=0, gravity=0.5, gravity_direction=(0, 1), maxVelocityX = 5, maxVelocityY = 10, acceleration = 0.1, friction = 0.9):
        self.physics = physics(self.rect, velocityX, velocityY, gravity, gravity_direction, maxVelocityX, maxVelocityY, acceleration, friction)
    #
    # do
    #
    def do(self, *function, **kwargs):
        result = {}
        for func in function:
            funcName = func.__name__
            try:
                result[funcName] = func(**kwargs)
            except TypeError:
                result[funcName] = func()
        return result  
    #
    # move
    # Atualiza o movimento com base na física
    # Move o entidade usando a física
    #
    def move(self, dx, dy):
        if self.physics:
           self.physics.move(dx, dy)      
    #
    # jump
    #
    def jump(self):
        if self.physics:
            self.physics.jump()
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
    # roll
    #
    def roll(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy         
    #  
    # update
    # Atualiza a física do jogador (movimento e gravidade)
    #      
    def update(self):
        if self.physics:
           self.physics.update()   
           self.x = self.physics.rect.x
           self.y = self.physics.rect.y      
    #  
    # render
    # Renderiza a imagem do jogador
    #      
    def render(self, screen):
        if self.renderer:
           self.renderer.render(screen)   
    #
    # handle_event
    #    
    def handleEvent(self, event):
        pass                 