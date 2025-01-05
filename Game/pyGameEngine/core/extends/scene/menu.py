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
from pyGameEngine.core.extends.entity.option import option
#
# componentes
#
from pyGameEngine.components.input import input
#
# menu
#
class menu(scene):
    itemIndex = 0
    optionItems = []
    #
    # __init__
    #
    def __init__(self, color, unselectedfontColor, selectedFontColor):
        super().__init__(color)
        self.selectedFontColor = selectedFontColor
        self.unselectedfontColor = unselectedfontColor
        self.input = input()  # Inicializa o input
        self.registerInputs()  # Registra os inputs inicialmente
    #
    # limits
    #
    def limits(self, value, max, min):
        if value > max:
            self.itemIndex = min
            return min
        if value < min:
            self.itemIndex = max
            return max
        else:
            self.itemIndex = value
            return value
    #
    # registerInputs
    #
    def registerInputs(self):
        self.setupInput({
            pygame.K_UP: lambda: self.focus(self.limits(self.itemIndex-1, len(self.entities)-1, 0)),
            pygame.K_DOWN: lambda: self.focus(self.limits(self.itemIndex+1, len(self.entities)-1, 0)),
        })
    #
    # setupInput
    #
    def setupInput(self, key_mapping):
        for key, action in key_mapping.items():
            self.input.bindKey(key, action)
    #
    # focus
    #
    def focus(self, index):
        if index < len(self.optionItems):
            # Atualiza as cores das opções
            for key, entity in enumerate(self.optionItems):
                if isinstance(entity, option):
                    if key == index:
                        entity.select(self.selectedFontColor)  # Opção selecionada
                    else:
                        entity.select(self.unselectedfontColor)  # Opção não selecionada
    #
    # addEntity
    #
    def addEntity(self, entity):
        super().addEntity(entity)
        if isinstance(entity, option):
            self.optionItems.append(entity)
        self.focus(0)  # Foca na primeira opção inicialmente
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
