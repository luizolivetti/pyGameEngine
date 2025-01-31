#  ----------------------------------------------------------
#  Input
#  Classe COMPONENTE para Input  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor Luiz Olivetti     @data 07/01/2025
#  ----------------------------------------------------------
import pygame
import time
#
# Extends
#
from pyGameEngine.components.extends.input.mouse import mouse
from pyGameEngine.components.extends.input.joystick import joystick
from pyGameEngine.components.extends.input.keyboard import keyboard
#
# Class input
#
class input():
    #
    # __init__
    #
    def __init__(self):
        self.last_input_time = 0  # Inicializa o tempo do último input
        self.input_delay = 0.2  # Delay de 200ms entre entradas contínuas
        self.keyBindings = {}  # Key mapping dictionary 
        self.keyboard = keyboard()
        self.joystick = joystick()
        self.mouse = mouse()
    #
    # register
    # Attention! The dictionaryHandler sets the entity responsible
    #            to make a moviment or selections in the scene
    #   
    def register(self, dictionaryHandler):
        self.setup(dictionaryHandler)           
    #
    # setup
    #
    def setup(self, keyMapping):
        for key, action in keyMapping.items():
            self.bindKey(key, action)            
    #
    # bindKey
    #
    def bindKey(self, key, action):
        self.keyBindings[key] = action
    #
    # handleInput
    #
    def handleInput(self, continuous=False):
        current_time = time.time()  # Obtém o tempo atual
        if continuous:
            # Comportamento contínuo: Verifica constantemente as teclas pressionadas
            keys = pygame.key.get_pressed()  # Obtém o estado de todas as teclas
            for key, action in self.keyBindings.items():
                if keys[key]:
                    action()
        else:
            # Comportamento contínuo: Verifica constantemente as teclas pressionadas
            keys = pygame.key.get_pressed()  # Obtém o estado de todas as teclas
            if current_time - self.last_input_time >= self.input_delay:
                # Apenas executa se o tempo de espera for maior que o delay
                for key, action in self.keyBindings.items():
                    if keys[key]:
                        action()
                self.last_input_time = current_time  # Atualiza o tempo do último input
