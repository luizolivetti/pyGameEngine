#  ----------------------------------------------------------
#  STAGES
#  Stages class
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor Luiz Olivetti     @data 06/01/2025
#  ----------------------------------------------------------
#
# https://www.freepik.com/free-photos-vectors/cartoon-kitchen
# https://pngtree.com/freepng/monster-Game-assets-ui-kit_3712767.html <-- personagens
# https://pngtree.com/so/monster-Game-assets-ui-kit
from pyGameEngine.core.scene import scene
#
# Extends
#
from pyGameEngine.core.extends.entity.label import label
from pyGameEngine.core.extends.entity.layer import layer
from pyGameEngine.core.extends.entity.player import player
from pyGameEngine.core.extends.entity.land import land
#
# stage1
#
class stage1(scene):
    #
    # init
    #
    def __init__(self, backgroundColor, inputContinuous=True, window=None, sceneSize=(0,0)):
        super().__init__(backgroundColor, inputContinuous, window, sceneSize)
        self.state = 'stage1'
        self.player1 = None
    #
    # stage1
    #
    def mount(self):
        super().mount()
        # backgroundImage added like layer
        backgroundImage = layer(0,0,'Game/pyGameEngine/assets/images/backgrounds/kitchenp.jpg', 0)
        self.addLayer('background',backgroundImage)
        # floor and platforms
        land1 = land(0, 580, 1500, 25, (250, 183, 217, 0.8))
        land1.drawLine()
        land1.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0)
        self.addLand('floor', land1) # Chão
        land2 = land(20, 380, 480, 15, (250, 183, 217, 0.8))
        land2.drawLine()
        land2.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0)
        self.addLand('sink', land2) # Plataforma sólida
        land3 = land(515, 270, 150, 10, (250, 183, 217, 0.8))
        land3.drawLine()
        land3.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0) 
        self.addLand('shelf', land3) # Plataforma flutuante
        land4 = land(680, 370, 400, 10, (250, 183, 217, 0.8))
        land4.drawLine()
        land4.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0)
        self.addLand('sink2', land4) # Plataforma sólida
        # add player 1 at the scene and mount commands for player 1
        self.player1 = player(10, 600, 0, 0)
        self.player1.setImage("Game/pyGameEngine/assets/images/player/1.png", 8, (250, 183, 217, 0.8))
        self.player1.setPhysics(0, 0, 0.8, (0, 1), 5, 35, 0.1, 0.9)
        self.addPlayer('player1', self.player1)
        self.input.keyboard.addHandler(self.input.keyboard.SPACE, self.player1, 'jump')
        self.input.keyboard.addHandler(self.input.keyboard.UP,    self, 'action')
        self.input.keyboard.addHandler(self.input.keyboard.DOWN,  self.player1, 'down')
        self.input.keyboard.addHandler(self.input.keyboard.LEFT,  self.player1, 'left')
        self.input.keyboard.addHandler(self.input.keyboard.RIGHT, self.player1, 'right')
        # registering controls on the scene
        self.input.register(self.input.keyboard.getHandler())        
    #
    # execute
    #
    def update(self):
        super().update()
    #
    # action
    #
    def action(self):
        if self.player1 is not None:
            if self.player1.x >= 738:
                self.execute('stage2')

