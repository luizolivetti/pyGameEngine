#  ----------------------------------------------------------
#  MAIN
#  Main program
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor Luiz Olivetti     @data 06/01/2025
# 
#  Themes https://www.youtube.com/watch?v=rxBiV3OaEjA
# 
#  ----------------------------------------------------------
#
# Engine
#
from pyGameEngine.core.engine import engine
#
# Custom scenes functions
#
from scenes.stage1 import stage1
from scenes.stage2 import stage2
#
# Main program
#
Game = engine(engine.BLACK)
#
# Mounting scenes
#
Game.addScene(stage1, Game.BLACK, True, (1500, 600))
Game.addScene(stage2, Game.BLACK, True, (1500, 600))
#
# Starting first state 
#
Game.setScene('stage1')
#
# Executing game
#
Game.run()
