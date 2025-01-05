#  ----------------------------------------------------------
#  screen
#  Classe CORE para controle de screen  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
#
# from gui
#
from pyGameEngine.core.timer import timer
from pyGameEngine.core.window import window
from pyGameEngine.core.extends.scene.map import map
#
# Class screen
#
class screen :
    #
    # Properties
    # 
    window = None
    timer = None
    color = (0,0,0)
    #
    # __init__
    #
    def __init__(self, width, height):
        self.setResolution(width, height)
    #
    # Resolution
    #
    def setResolution(self, width, height):
        self.window = window(width, height)
    #
    # setWindowCaption
    #
    def setWindowCaption(self, caption):
        self.window.caption(caption)
    #
    # setWindowCaption
    #
    def setWindowBackground(self, color):
        self.color = color
        self.window.background(color)    
    #
    # getWindowHandler
    # 
    def getWindowHandler(self):
        return self.window.getHandler()    
    #
    # Timer | FPS
    #
    def setTimer(self):
        self.timer = timer.get()
    #
    # mapRender
    #
    def mapRender(self, windowHandler):
        map.render(windowHandler)