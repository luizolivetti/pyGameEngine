#  ----------------------------------------------------------
#  MENU
#  First menu of the Game
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor Luiz Olivetti     @data 06/01/2025
#  ----------------------------------------------------------
from pyGameEngine.core.engine import engine
from pyGameEngine.core.scene import scene
#
# extends
#
from pyGameEngine.core.extends.entity.label import label
from pyGameEngine.core.extends.entity.layer import layer
from pyGameEngine.core.extends.entity.options import options
#
# stage1
#
class optionsMenu(scene):
    #
    # init
    #
    def __init__(self, backgroundColor, inputContinuous=True, window=None, sceneSize=(0,0)):
        super().__init__(backgroundColor, inputContinuous, window, sceneSize)
        self.state = 'optionsmenu'
    #
    # stage1
    #
    def mount(self):
        super().mount()
        # imagens
        backgroundImage = layer(0,0,'Game/pyGameEngine/assets/images/backgrounds/opening.jpg',5)
        self.addEntity(backgroundImage)
        # textos 
        title = label(20, 0, 'Little Monsters', engine.ORANGE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 80)
        subtitle = label(20, 100, 'beyond under the bed', engine.WHITE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf', 40)
        copyright = label(20, 550, 'Copyright(c)OER Tecnologia - Poweredge by PyGameEngine', engine.WHITE, None, 20)
        self.addEntity(subtitle)
        self.addEntity(title)
        self.addEntity(copyright)
        # opcoes
        configurations = options(20, 300, engine.WHITE, engine.ORANGE, 'Game/pyGameEngine/assets/fonts/MountainsofChristmas-Regular.ttf')  
        configurations.addItem("Volume do audio", None)
        configurations.addItem("Volume dos efeitos", None)
        configurations.addItem("Volume dos dialogos", None)
        configurations.addItem("Configuração do teclado", None)
        configurations.addItem("Voltar", 'mainmenu')
        configurations.selected(0)
        self.addEntity(configurations)
        # controles
        self.input.keyboard.addHandler(self.input.keyboard.UP, configurations, 'up')
        self.input.keyboard.addHandler(self.input.keyboard.DOWN, configurations, 'down')
        self.input.keyboard.addHandler(self.input.keyboard.RETURN, configurations, 'do', self.execute)
        self.input.register(self.input.keyboard.getHandler())
        # sons
        self.media.addSound('Doors', 'Game/pyGameEngine/assets/sounds/doors.mp3', -1, 0.6)