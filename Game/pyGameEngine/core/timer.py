#  ----------------------------------------------------------
#  Window
#  Classe CORE para controle de tempo  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# Class timer
#
class timer :
    #
    # properties
    # 
    clock = None
    #
    # __init__
    # 
    def __init__(self):
        self.setClock()  
    #
    # setClock
    #
    def setClock(self):
        self.clock = pygame.time.Clock() 
    #
    # tick
    #
    def tick(self, ms):
        self.clock.tick(ms)        
    #
    # getClock
    #
    def getClock(self):
        return self.clock     