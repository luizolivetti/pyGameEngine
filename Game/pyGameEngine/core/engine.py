#  ----------------------------------------------------------
#  pyEngine
#  Classe CORE para Engine  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
# import gc
import pygame
#
# configurations
#
from settings import settings
from pyGameEngine.core.scene import scene
from pyGameEngine.core.window import window
#
# Class game
#
class engine(settings):
    #
    # properties
    #
    window = None
    scene = None
    scenes = {}
    running = True
    firstState = None
    currentState = None
    previousState = None
    runningState = None
    countScenes = 0   
    #
    # Initialization
    #
    def __init__(self, color):
        # Initializing pyGame
        pygame.init()    
        # Initializing variables 
        self.window = window(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT, settings.TITLE, color)
    #
    # addScene
    #
    def addScene(self, sceneObject, background, inputContinuous=True, sceneSize=(0,0)):
        so = sceneObject(background, inputContinuous, self.window, sceneSize)
        self.scenes[so.state] = so  
        self.countScenes = len(self.scenes)           
    #
    # getScene
    #
    def getScene(self, state):
        return self.scenes[state]  
    #
    # nextScene
    # 
    def nextScene(self, state):
        self.currentState.media.stopSounds()
        self.setScene(state)  
    #
    # previousScene
    #         
    def previousScene(self):
        self.currentState.media.stopSounds()
        self.setScene(self.previousState)           
    #
    # setScene
    #
    def setScene(self, state):
        if state in self.scenes:
            if self.previousState is None:
               self.previousState = self.scenes[state]
            else:
               self.previousState = self.currentState
            self.currentState = self.scenes[state]
        else:
            print(f"Cena não encontrada para o estado '{state}'.")
    #
    # executeScene
    # 
    def executeScene(self):  
        if self.currentState is not None:
            if self.runningState != self.currentState:
                self.currentState.mount()
                self.runningState = self.currentState
            self.currentState.update()
            self.currentState.render(self.window.getHandler())                  
    #
    # Loop
    #
    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if self.currentState:
                    self.currentState.handleEvent(event)
            # call for
            if self.currentState.callFor is not None:
                self.setScene(self.currentState.callFor)
            # executeScene
            self.executeScene()
            # update
            pygame.display.flip()
            self.window.timer.tick(settings.FPS)

        pygame.quit()
    #
    # update
    #
    def update(self):
        pygame.display.update() 
        if self.currentState is not None:
           self.currentState.update()
    #
    # quit
    #
    def quit(self):
        pygame.quit() 
    #
    # handle_events
    #
    def handleEvents(self, events):
        if self.currentState is not None:
           self.currentState.handleEvents(events)
    #
    # render
    #
    def render(self, window):
        if self.currentState is not None:
           self.currentState.render(window)        