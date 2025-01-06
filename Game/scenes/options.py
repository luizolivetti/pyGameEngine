#  ----------------------------------------------------------
#  MENU
#  First menu of the game
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
#
# settings
#
from settings import settings
#
# Engine
#
from pyGameEngine.core.game import game
#
# Extends
#
from pyGameEngine.core.extends.scene.menu import menu
from pyGameEngine.core.extends.entity.label import label
from pyGameEngine.core.extends.entity.layer import layer
from pyGameEngine.core.extends.entity.options import options
#
# mainMenu
#
optionsMenu = menu(game.BLACK)
# imagens
backgroundImage = layer(0,150,'Game/pyGameEngine/assets/images/backgrounds/opening.jpg',10)
optionsMenu.addEntity(backgroundImage)
# textos 
title = label(20, 0, 'Little Monsters', game.RED, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 80)
optionsMenu.addEntity(title)
subtitle = label(20, 100, 'beyond under the bed', game.WHITE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 30)
optionsMenu.addEntity(subtitle)
copyright = label(200, 550, 'Copyright(c)OER Tecnologia - Poweredge by PyGameEngine', game.WHITE, None, 20)
optionsMenu.addEntity(copyright)
# opcoes
configurations = options(320, 300) 
configurations.addItem("Volume do audio", None)
configurations.addItem("Volume dos efeitos", None)
configurations.addItem("Volume dos dialogos", None)
configurations.addItem("Configuração do teclado", None)
configurations.addItem("Voltar", None)
optionsMenu.addEntity(configurations)
# sons
optionsMenu.addSound('Doors', 'Game/pyGameEngine/assets/sounds/doors.mp3', -1, 0.8)