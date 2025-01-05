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
optionsMenu = menu(game.BLACK, game.WHITE, game.RED)

# imagens
backgroundImage = layer(0,150,'pyGameEngine/assets/images/backgrounds/opening.jpg',10)
optionsMenu.addEntity(backgroundImage)

# textos 
title = label(20, 0, 'Little Monsters', game.RED, 'pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 80)
optionsMenu.addEntity(title)
subtitle = label(20, 100, 'beyond under the bed', game.WHITE, 'pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 30)
optionsMenu.addEntity(subtitle)
copyright = label(200, 550, 'Copyright(c)OER Tecnologia - Poweredge by PyGameEngine', game.WHITE, None, 20)
optionsMenu.addEntity(copyright)

# opcoes
option1 = option(320, 300, "Volume do audio", game.WHITE)
optionsMenu.addEntity(option1)
option2 = option(320, 325, "Volume dos efeitos", game.WHITE)
optionsMenu.addEntity(option2)
option3 = option(320, 350, "Volume dos dialogos", game.WHITE)
optionsMenu.addEntity(option3)
option4 = option(320, 375, "Configuração do teclado", game.WHITE)
optionsMenu.addEntity(option4)
option5 = option(320, 400, "Voltar", game.WHITE)
optionsMenu.addEntity(option5)

# sons
optionsMenu.addSound('Doors', 'pyGameEngine/assets/sounds/doors.mp3')
optionsMenu.play('Doors',-1)
optionsMenu.volume('Doors', 0.8)