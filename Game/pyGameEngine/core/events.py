#  ----------------------------------------------------------
#  Events
#  Classe CORE para controle de eventos  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# from 
#

#
# Class events
#
class events :
    #
    # __init__
    #
    def __init__(self):
        self.events = []
        self.keys = pygame.key.get_pressed()
    #
    # handleEvents
    #
    def handleEvents(self):
        self.events = pygame.event.get()  # Pega todos os eventos
        self.keys = pygame.key.get_pressed()  # Atualiza o estado das teclas pressionadas
    #
    # getEvents
    #
    def getEvents(self):
        return self.events
    #
    # isKeyPressed
    #
    def isKeyPressed(self, key):
        return self.keys[key]
    #
    # isKeyJustPressed
    #
    def isKeyJustPressed(self, key):
        for event in self.events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
    #
    # isQuitEvent
    #
    def isQuitEvent(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                return True
        return False