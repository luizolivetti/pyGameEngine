#  ----------------------------------------------------------
#  stage
#  Classe COMPONENT para stage  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 03/01/2025
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
# cores 
from pyGameEngine.core.scene import scene
# components
from pyGameEngine.components.input import input
# extends
from pyGameEngine.components.extends.input.keyboard import keyboard
#
# stage extends scene
# 
class stage(scene):
    #
    # __init__
    #     
    def __init__(self, color):
        super().__init__(color)
        self.input = input()
        self.keyboard = keyboard()
    #
    # registerInputs
    # Vincula os inputs aos jogadores ou outras entidades da cena.
    #   
    def registerInputs(self, entity, left, right, up, down):
        self.setupPlayerInput(entity, {
            left: lambda: entity.move(-5, 0),
            right: lambda: entity.move(5, 0),
            up: lambda: entity.move(0, -5),
            down: lambda: entity.move(0, 5),
        })        
    #
    # setupPlayerInput
    # Configura o input para uma entidade com base em um dicionário de teclas e ações.
    # :param player: Entidade que terá o input configurado.
    # :param key_mapping: Dicionário de mapeamento {tecla: ação}.
    #  
    def setupPlayerInput(self, player, key_mapping):
        for key, action in key_mapping.items():
            self.input.bindKey(key, action)
    #
    # handle_event
    #  
    def handle_event(self, event):
        super().handle_event(event)
        # Trata eventos únicos
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.input.handleInput(True)
    #
    # update
    #  
    def update(self):
        super().update()
        self.input.handleInput(True)