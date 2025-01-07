#  ----------------------------------------------------------
#  MAIN
#  Main program
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor Luiz Olivetti     @data 06/01/2025
#  ----------------------------------------------------------
#
# Engine
#
from pyGameEngine.core.game import game
#
# Custom scenes
#
from scenes.stage1 import stage1
from scenes.mainMenu import mainMenu
from scenes.optionsMenu import optionsMenu
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
#     1. Ao addScene não executar todo seu contexto - OK
#     2. Melhorar a concepção de menu. Atualmente option é uma entity na scene
#        e as seleção dos itens e os eventos de escolha não estão adequados
#     3. Criar modo de navegação nos "states" de modo a mudar a cena de acordo 
#        com o estado necessário
#     4. Melhorar adesão de layers para que sejam ajustadas as telas
#     5. Melhorar enquadramento para que a tela possa "correr" para os lados 
#        quando background for maior que o enquadramento
#
# executando
Game.run()
