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
from scenes.stage1 import stage1
from scenes.mainMenu import mainMenu
from scenes.optionsMenu import optionsMenu
#
# Main program
#
Game = engine(engine.BLACK)
#
# Relation of Scene and States
#
Game.addScene('mainmenu', mainMenu(Game))
Game.addScene('optionsmenu', optionsMenu(Game))
Game.addScene('stage1', stage1(Game))
#
# Starting first state 
#
Game.setScene('mainmenu')
# TO-DO : 
#     1. Ao addScene não executar todo seu contexto - OK
#     2. Melhorar a concepção de menu. Atualmente option é uma entity na scene
#        e as seleção dos itens e os eventos de escolha não estão adequados - OK
#     3. Criar modo de navegação nos "states" de modo a mudar a cena de acordo 
#        com o estado necessário - OK
# 
#     4. Melhorar adesão de layers para que sejam ajustadas as telas
#     5. Melhorar enquadramento para que a tela possa "correr" para os lados 
#        quando background for maior que o enquadramento
# https://www.gamedevmarket.net/category/2d/characters?page=160
# executing game
Game.run()
