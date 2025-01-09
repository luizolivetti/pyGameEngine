#  ----------------------------------------------------------
#  Joystick
#  Classe compoennte para controle do Joystick  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 31/12/2024
#  @revisor Luiz Olivetti     @data 07/01/2025
#  ----------------------------------------------------------
import pygame
#
# interface
#
from pyGameEngine.components.extends.input.device import device
#
# Class input
#
class joystick(device):
    #
    # getHandler
    #
    def getHandler(self):
        pass
    #
    # device handler
    #
    def addHandler(self, key, entity, action):
        pass
    #
    # remHandler
    #
    def remHandler(self, key):
        pass 