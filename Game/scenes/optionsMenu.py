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
# optionsMenu
#
def optionsMenu(game):
    optionsMenu = scene(game.BLACK, game, False)
    # imagens
    backgroundImage = layer(0,0,'Game/pyGameEngine/assets/images/backgrounds/opening.jpg',5)
    optionsMenu.addEntity(backgroundImage)
    # textos 
    title = label(20, 0, 'Little Monsters', game.ORANGE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 80)
    subtitle = label(20, 100, 'beyond under the bed', game.WHITE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 40)
    copyright = label(20, 550, 'Copyright(c)OER Tecnologia - Poweredge by PyGameEngine', game.WHITE, None, 20)
    optionsMenu.addEntity(subtitle)
    optionsMenu.addEntity(title)
    optionsMenu.addEntity(copyright)
    # opcoes
    configurations = options(20, 300, game.WHITE, game.ORANGE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf')  
    configurations.addItem("Volume do audio", None)
    configurations.addItem("Volume dos efeitos", None)
    configurations.addItem("Volume dos dialogos", None)
    configurations.addItem("Configuração do teclado", None)
    configurations.addItem("Voltar", 'mainmenu')
    configurations.selected(0)
    optionsMenu.addEntity(configurations)
    # controles
    optionsMenu.input.keyboard.addHandler(optionsMenu.input.keyboard.UP, configurations, 'up')
    optionsMenu.input.keyboard.addHandler(optionsMenu.input.keyboard.DOWN, configurations, 'down')
    optionsMenu.input.keyboard.addHandler(optionsMenu.input.keyboard.RETURN, configurations, 'do', optionsMenu.nextScene)
    optionsMenu.input.register(optionsMenu.input.keyboard.getHandler())
    # sons
    optionsMenu.addSound('Doors', 'Game/pyGameEngine/assets/sounds/doors.mp3', -1, 0.6)
    # Retorno
    return optionsMenu