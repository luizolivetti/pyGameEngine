#  ----------------------------------------------------------
#  STAGE 1
#  First stage of the game
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
#
# https://www.freepik.com/free-photos-vectors/cartoon-kitchen
#
# Engine
#
from pyGameEngine.core.game import game
#
# Extends
#
from pyGameEngine.core.extends.scene.stage import stage
from pyGameEngine.core.extends.entity.layer import layer
from pyGameEngine.core.extends.entity.player import player

# Scene object
stage1 = stage(game.BLACK)

# backgroundImage
backgroundImage = layer(0,0,'pyGameEngine/assets/images/backgrounds/kitchen.jpg', 4.5)
stage1.addEntity(backgroundImage)

# creating player 1
player1 = player(0, 100, "pyGameEngine/assets/images/player/1.png", 8)
# add player 1 at the scene
stage1.addEntity(player1)
# mount commands for player 1
left = stage1.keyboard.a # left 
down = stage1.keyboard.s # down
right = stage1.keyboard.d # right
up = stage1.keyboard.w # up
# regiter commands for player 1
stage1.registerInputs(player1, left, right, up, down)

# creating player 2
player2 = player(0, 200, "pyGameEngine/assets/images/player/2.png", 8)
# add player 1 at the scene
stage1.addEntity(player2)
# mount commands for player 1
left = stage1.keyboard.LEFT # left 
down = stage1.keyboard.DOWN # down
right = stage1.keyboard.RIGHT # right
up = stage1.keyboard.UP # up
# regiter commands for player 1
stage1.registerInputs(player2, left, right, up, down)

# creating player 3
player3 = player(0, 300, "pyGameEngine/assets/images/player/3.png", 8)
# add player 1 at the scene
stage1.addEntity(player3)
# mount commands for player 1
left = stage1.keyboard.h # left 
down = stage1.keyboard.j # down
right = stage1.keyboard.k # right
up = stage1.keyboard.u # up
# regiter commands for player 1
stage1.registerInputs(player3, left, right, up, down)

# creating player 4
player4 = player(0, 400, "pyGameEngine/assets/images/player/4.png", 8)
# add player 1 at the scene
stage1.addEntity(player4)
# mount commands for player 1
left = stage1.keyboard.c # left 
down = stage1.keyboard.v # down
right = stage1.keyboard.b # right
up = stage1.keyboard.f # up
# regiter commands for player 1
stage1.registerInputs(player4, left, right, up, down)