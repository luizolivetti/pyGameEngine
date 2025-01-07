#  ----------------------------------------------------------
#  MENU
#  First menu of the game
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor Luiz Olivetti     @data 06/01/2025
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
mainMenu = menu(game.BLACK)
# imagens
backgroundImage = layer(0,150,'Game/pyGameEngine/assets/images/backgrounds/opening.jpg',10)
mainMenu.addEntity(backgroundImage)
# textos 
title = label(20, 0, 'Little Monsters', game.RED, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 80)
mainMenu.addEntity(title)
subtitle = label(20, 100, 'beyond under the bed', game.WHITE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 40)
mainMenu.addEntity(subtitle)
copyright = label(200, 550, 'Copyright(c)OER Tecnologia - Poweredge by PyGameEngine', game.WHITE, None, 20)
mainMenu.addEntity(copyright)
# opcoes
mainOptions = options(320,300) 
mainOptions.addItem("Start", 'stage1')
mainOptions.addItem("Options", None)
mainMenu.addEntity(mainOptions)
# sons 
mainMenu.addSound('Opening', 'Game/pyGameEngine/assets/sounds/opening.mp3', -1, 0.2)
mainMenu.addSound('Doors', 'Game/pyGameEngine/assets/sounds/doors.mp3', -1, 0.2)
