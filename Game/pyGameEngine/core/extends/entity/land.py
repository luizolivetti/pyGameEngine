#  ----------------------------------------------------------
#  land
#  Classe CORE para controle de land  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 10/01/2025
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# core
#
from pyGameEngine.core.entity import entity
#
# land
#
class land(entity):
    #
    # __init__
    #
    def __init__(self, x, y, width, height, platform_type="solid"):
        super().__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.type = platform_type  # Pode ser "solid", "hole", "floating", etc.
    #
    # interact
    # Interage com o jogador dependendo do tipo de plataforma
    #
    def interact(self, player):
        if self.type == "hole":
            if self.rect.colliderect(player.rect):
                player.die()  # Método para "matar" o jogador caso ele caia em um buraco
        # Pode adicionar outras interações para diferentes tipos de plataforma
    #
    # update
    #      
    def update(self):
        super().update()
    #
    # render
    # Renderiza a plataforma no cenário
    #
    def render(self, screen):
        if self.type == "solid":
            pygame.draw.rect(screen, (0, 255, 0), self.rect)  # Cor verde para plataforma sólida
        elif self.type == "hole":
            pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Cor vermelha para buracos
        elif self.type == "floating":
            pygame.draw.rect(screen, (0, 0, 255), self.rect)  # Cor azul para plataformas flutuantes        
    #
    # handleEvent
    #
    def handleEvent(self, event):
        pass
    #
    # handleEvent
    #
    def handleEvents(self, events):
        pass

