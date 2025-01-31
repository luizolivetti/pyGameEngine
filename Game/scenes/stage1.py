#  ----------------------------------------------------------
#  STAGE 1
#  First stage of the Game
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
from pyGameEngine.core.extends.entity.layer import layer
from pyGameEngine.core.extends.entity.player import player
from pyGameEngine.core.extends.entity.land import land
from pyGameEngine.core.extends.entity.label import label
#
# stage1
#
def mountStage1(Game):
    # Scene object with the layer background size 1500x600
    Game.addScene('stage1', Game.BLACK, True, (1500, 600))
    stage1 = Game.getScene('stage1')
    # backgroundImage added like layer
    backgroundImage = layer(0,0,'Game/pyGameEngine/assets/images/backgrounds/kitchenp.jpg', 0)
    stage1.addLayer('background',backgroundImage)
    # floor and platforms
    land1 = land(0, 610, 1500, 25, "solid")
    land1.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0)
    stage1.addLand('floor', land1) # Chão
    land2 = land(20, 380, 480, 15, "solid")
    land2.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0)
    stage1.addLand('sink', land2) # Plataforma sólida
    land3 = land(515, 270, 150, 10, "solid")
    land3.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0) 
    stage1.addLand('shelf', land3) # Plataforma flutuante
    # add player 1 at the scene and mount commands for player 1
    player1 = player(0, 610, 0, 0)
    player1.setImage("Game/pyGameEngine/assets/images/player/1.png", 8)
    player1.setPhysics(0, 0, 0.5, (0, 1), 5, 10, 0.1, 0.9)
    stage1.addPlayer('player1', player1)
    stage1.input.keyboard.addHandler(stage1.input.keyboard.SPACE, player1, 'jump', param=-200)
    stage1.input.keyboard.addHandler(stage1.input.keyboard.DOWN,  player1, 'down')
    stage1.input.keyboard.addHandler(stage1.input.keyboard.LEFT,  player1, 'left')
    stage1.input.keyboard.addHandler(stage1.input.keyboard.RIGHT, player1, 'right')
    # registering controls on the scene
    stage1.input.register(stage1.input.keyboard.getHandler())
    # finally 
    return stage1    