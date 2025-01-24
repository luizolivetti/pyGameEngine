#  ----------------------------------------------------------
#  MAIN
#  Main program
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor Luiz Olivetti     @data 06/01/2025
#  ----------------------------------------------------------
import time
#
# Engine
#
from pyGameEngine.core.engine import engine
#
# Custom scenes functions
#
from scenes.mainMenu import mountMainMenu
from scenes.optionsMenu import mountOptionsMenu
from scenes.stage1 import mountStage1
#
# Main program
#
Game = engine(engine.BLACK)
#
# Mounting scenes
#
mountMainMenu(Game)
mountOptionsMenu(Game)
mountStage1(Game)
#
# Starting first state 
#
Game.setScene('mainmenu')
#
# Executing game
#
Game.run()
