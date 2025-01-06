#  ----------------------------------------------------------
#  physics
#  Classe COMPONENT para physics  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 03/01/2025
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# Class physics
#
class physics:
    #
    # __init__
    #
    def __init__(self, x, y, width, height, velocity=0):
        self.rect = pygame.Rect(x, y, width, height)  # Representa a posição e tamanho da entidade
        self.velocity_x = 0  # Velocidade no eixo X
        self.velocity_y = 0  # Velocidade no eixo Y
        self.gravity = 0.5   # Gravidade (ajustável)
        self.velocity = velocity  # Velocidade base
    #
    # apply_gravity
    #
    def apply_gravity(self):
        self.velocity_y += self.gravity
    #
    # move
    #
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    #
    # update
    #
    def update(self):
        self.apply_gravity()
        self.move(self.velocity_x, self.velocity_y)
    #
    # check_collision
    #
    def check_collision(self, other):
        """Verifica colisão com outra entidade."""
        return self.rect.colliderect(other.rect)
    #
    # set_position
    #
    def set_position(self, x, y):
        """Define uma nova posição para a entidade."""
        self.rect.topleft = (x, y)