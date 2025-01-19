#  ----------------------------------------------------------
#  STAGE 1
#  First stage of the game
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor Luiz Olivetti     @data 06/01/2025
#  ----------------------------------------------------------
#
# https://www.freepik.com/free-photos-vectors/cartoon-kitchen
# https://pngtree.com/freepng/monster-game-assets-ui-kit_3712767.html <-- personagens
# https://pngtree.com/so/monster-game-assets-ui-kit
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
def stage1(game):
    # Scene object
    stage1 = scene(game.BLACK, game)
    # backgroundImage
    backgroundImage = layer(0,0,'Game/pyGameEngine/assets/images/backgrounds/kitchen.jpg', 5)
    stage1.addEntity(backgroundImage)
    # floor and platforms
    land1 = land(0, 550, 800, 50, "solid")
    land1.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0)
    stage1.addEntity(land1) # Chão
    land2 = land(200, 400, 200, 20, "solid")
    land2.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0)
    stage1.addEntity(land2) # Plataforma sólida
    land3 = land(500, 300, 150, 20, "floating")
    land3.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0)  
    stage1.addEntity(land3) # Plataforma flutuante
    land4 = land(350, 150, 100, 20, "hole")  
    land4.setPhysics(0, 0, 0, (0,0), 0, 0, 0, 0)  
    stage1.addEntity(land4) # Buraco
    # creating player 1
    # add player 1 at the scene
    # mount commands for player 1
    player1 = player(0, 100, 0, 0)
    player1.setImage("Game/pyGameEngine/assets/images/player/1.png", 8)
    player1.setPhysics(0, 0, 0.5, (0, 1), 5, 10, 0.1, 0.9)
    stage1.addEntity(player1)
    stage1.input.keyboard.addHandler(stage1.input.keyboard.UP,    player1, 'jump', param=-15)
    stage1.input.keyboard.addHandler(stage1.input.keyboard.DOWN,  player1, 'down')
    stage1.input.keyboard.addHandler(stage1.input.keyboard.LEFT,  player1, 'left')
    stage1.input.keyboard.addHandler(stage1.input.keyboard.RIGHT, player1, 'right')
    # to-do: how to get the velocity of the player
    x = label(20, 0, "x: " + str(player1.physics.velocityX), game.WHITE)
    y = label(20, 15, "y: " + str(player1.physics.velocityY), game.WHITE)
    stage1.addEntity(x)
    stage1.addEntity(y)
    # creating player 2
    # add player 2 at the scene
    # mount commands for player 2
    # player2 = player(0, 200, "Game/pyGameEngine/assets/images/player/2.png", 8)
    # stage1.addEntity(player2)
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.w, player2, 'up')
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.s, player2, 'down')
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.a, player2, 'left')
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.d, player2, 'right')
    # creating player 3
    # add player 3 at the scene
    # mount commands for player 3    
    # player3 = player(0, 300, "Game/pyGameEngine/assets/images/player/3.png", 8)
    # stage1.addEntity(player3)
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.t, player3, 'up')
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.g, player3, 'down')
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.f, player3, 'left')
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.h, player3, 'right')
    # creating player 4
    # add player 4 at the scene
    # mount commands for player 4
    # player4 = player(0, 400, "Game/pyGameEngine/assets/images/player/4.png", 8)
    # stage1.addEntity(player4)
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.i, player4, 'up')
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.k, player4, 'down')
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.j, player4, 'left')
    # stage1.input.keyboard.addHandler(stage1.input.keyboard.l, player4, 'right')
    # registering controls
    stage1.input.register(stage1.input.keyboard.getHandler())
    # finally 
    return stage1    