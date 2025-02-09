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
from scenes.mainMenu import mainMenu
from scenes.optionsMenu import optionsMenu
from scenes.stage1 import stage1
from scenes.stage2 import stage2
#
# Main program
#
Game = engine(engine.BLACK)
#
# add scenes
#
Game.addScene(mainMenu, engine.BLACK, False, (800, 600))
Game.addScene(optionsMenu, engine.BLACK, False, (800, 600))
Game.addScene(stage1, engine.BLACK, True, (1500, 600))
Game.addScene(stage2, engine.BLACK, True, (1500, 600))
#
# Starting first state 
#
Game.setScene('mainmenu')
#
# Executing game
#
Game.run()
