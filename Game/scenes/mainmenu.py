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
from pyGameEngine.core.extends.entity.option import option
#
# mainMenu
#
mainMenu = menu(game.BLACK, game.WHITE, game.RED)

# imagens
backgroundImage = layer(0,150,'pyGameEngine/assets/images/backgrounds/opening.jpg',10)
mainMenu.addEntity(backgroundImage)

# textos 
title = label(20, 0, 'Little Monsters', game.RED, 'pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 80)
mainMenu.addEntity(title)
subtitle = label(20, 100, 'beyond under the bed', game.WHITE, 'pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 30)
mainMenu.addEntity(subtitle)
copyright = label(200, 550, 'Copyright(c)OER Tecnologia - Poweredge by PyGameEngine', game.WHITE, None, 20)
mainMenu.addEntity(copyright)

# opcoes
option1 = option(340, 300, "Start", game.WHITE)
mainMenu.addEntity(option1)
option2 = option(340, 325, "Options", game.WHITE)
mainMenu.addEntity(option2)

# sons 
mainMenu.addSound('Opening', 'pyGameEngine/assets/sounds/opening.mp3')
mainMenu.play('Opening',-1)
mainMenu.volume('Opening', 0.5)

mainMenu.addSound('Doors', 'pyGameEngine/assets/sounds/doors.mp3')
mainMenu.play('Doors',-1)
mainMenu.volume('Doors', 0.8)