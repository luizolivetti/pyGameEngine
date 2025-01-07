#  ----------------------------------------------------------
#  stage
#  Classe COMPONENT para stage  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 03/01/2025
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# cores
#
from pyGameEngine.core.scene import scene
#
# componentes
#
from pyGameEngine.components.input import input
#
# menu
#
class menu(scene):
    #
    # __init__
    #
    def __init__(self, color):
        super().__init__(color)
        self.itemIndex = 0
        # Inicializa o input
        self.input = input()  
        # Registra os inputs inicialmente
        self.registerInputs()  
    #
    # registerInputs
    #
    def registerInputs(self):
        self.setupInput({
            pygame.K_UP: lambda: self.focusUp(),
            pygame.K_DOWN: lambda: self.focusDown(),
        })
    #
    # setupInput
    #
    def setupInput(self, key_mapping):
        for key, action in key_mapping.items():
            self.input.bindKey(key, action)  
    #
    # addEntity
    #
    def addEntity(self, entity):
        super().addEntity(entity)
    #
    # handleEvent
    #
    def handleEvent(self, event):
        super().handleEvent(event)
        self.input.handleInput(False)
    #
    # update
    #
    def update(self):
        super().update()
        self.input.handleInput(False)