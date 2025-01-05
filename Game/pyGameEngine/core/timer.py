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
    # Getting
    #
    def get():
        timer.clock = pygame.time.Clock()