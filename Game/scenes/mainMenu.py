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
# core
#
from pyGameEngine.core.scene import scene
#
# extends
#
from pyGameEngine.core.extends.entity.label import label
from pyGameEngine.core.extends.entity.layer import layer
from pyGameEngine.core.extends.entity.options import options
#
# mainMenu
#
def mainMenu(game):
    mainMenu = scene(game.BLACK, game, False)
    # imagens
    backgroundImage = layer(0,0,'Game/pyGameEngine/assets/images/backgrounds/opening.jpg', 5)
    mainMenu.addEntity(backgroundImage)
    # textos 
    title     = label(20, 0, 'Little Monsters', game.ORANGE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 80)
    subtitle  = label(20, 100, 'beyond under the bed', game.WHITE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 40)
    copyright = label(20, 550, 'Copyright(c)OER Tecnologia - Poweredge by PyGameEngine', game.WHITE, None, 20)
    mainMenu.addEntity(title)
    mainMenu.addEntity(subtitle)
    mainMenu.addEntity(copyright)
    # opcoes              
    mainOptions = options(20, 300, game.WHITE, game.ORANGE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf') 
    mainOptions.addItem("Start", "stage1")
    mainOptions.addItem("Options", "optionsmenu")
    mainOptions.selected(0)
    mainMenu.addEntity(mainOptions)
    # controles
    mainMenu.input.keyboard.addHandler(mainMenu.input.keyboard.UP, mainOptions, 'up')
    mainMenu.input.keyboard.addHandler(mainMenu.input.keyboard.DOWN, mainOptions, 'down')
    mainMenu.input.keyboard.addHandler(mainMenu.input.keyboard.RETURN, mainOptions, 'do', mainMenu.nextScene)
    mainMenu.input.register(mainMenu.input.keyboard.getHandler())
    # sons 
    mainMenu.addSound('Opening', 'Game/pyGameEngine/assets/sounds/opening.mp3', -1, 0.2)
    mainMenu.addSound('Doors', 'Game/pyGameEngine/assets/sounds/doors.mp3', -1, 0.5)
    # Retorno
    return mainMenu

