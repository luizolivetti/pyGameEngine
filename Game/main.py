# 
# Main File
# 
# Created by: Luiz Olivetti
# Created at: 2024-12-20
# 
# Examples | References
# --------------------------------------------------------------------------------------------------------
# Get isometric tile mouse selection in Pygame
# https://stackoverflow.com/questions/71336864/get-isometric-tile-mouse-selection-python/73996398#73996398
# 
# Draw a staggered isometric map with python
# https://stackoverflow.com/questions/66568267/draw-a-staggered-isometric-map-with-python/66569330#66569330
#
# GitHub - PyGameExamplesAndAnswers - Isometric
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_isometric.md
# https://replit.com/@Rabbid76/Pygame-IsometircMap#main.py
#
# ASCII Art
# https://www.asciiart.eu/space/aliens
# ---------------------------------------------------------------------------------------------------------
# https://pngtree.com/freepng/monster-game-assets-ui-kit_3712767.html <-- personagens
#
# Engine
#
from pyGameEngine.core.game import game
#
# Custom scenes
#
from scenes.stage1 import stage1
from scenes.mainmenu import mainMenu
from scenes.options import optionsMenu
#
# Main program
#
Game = game(game.BLACK)
# adicionando estados e suas cenas
Game.addScene('mainmenu', mainMenu)
Game.addScene('optionsmenu', optionsMenu)
Game.addScene('stage1', stage1)
# inicializando o estado inicial
Game.setScene('stage1')
# TO-DO : 
#     1. Ao addScene não executar todo seu contexto
#     2. Melhorar a concepção de menu. Atualmente option é uma entity na scene
#        e as seleção dos itens e os eventos de escolha não estão adequados
#     3. Criar modo de navegação nos "states" de modo a mudar a cena de acordo 
#        com o estado necessário
#     4. Melhorar adesão de layers para que sejam ajustadas as telas
#     5. Melhorar enquadramento para que a tela possa "correr" para os lados 
#        quando background for maior que o enquadramento
# executando
Game.run()
