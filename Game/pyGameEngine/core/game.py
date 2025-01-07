#  ----------------------------------------------------------
#  pyEngine
#  Classe CORE para Engine  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# configurations
#
from settings import settings
from pyGameEngine.core.screen import screen
#
# Class game
#
class game(settings):
    #
    # Properties
    #
    running = True
    screen = None
    scene = None
    scenes = {}
    currentState = None
    firstState = None
    countScenes = 0
    #
    # Initialization
    #
    def __init__(self, color):
        # Initializing pyGame
        pygame.init()    
        # Define Window
        self.screen = screen(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        self.screen.setWindowCaption(settings.TITLE)
        self.screen.setWindowBackground(color)
        self.screen.setTimer()
        # to-do it better
        self.clock = pygame.time.Clock()
    #
    # addScene
    #
    def addScene(self, state, scene):
        self.scenes[state] = scene  
        self.countScenes = len(self.scenes)            
    #
    # getScene
    #
    def getScene(self, state):
            self.scenes[state]    
    #
    # setScene
    #
    def setScene(self, state):
        if state in self.scenes:
            self.currentState = self.scenes[state]
        else:
            print(f"Cena não encontrada para o estado '{state}'.")
    #
    # executeScene
    # 
    def executeScene(self):  
        if self.currentState is not None:
            self.screen.setWindowBackground(self.currentState.background)
            self.currentState.update()
            self.currentState.render(self.screen.getWindowHandler())                  
    #
    # Loop
    #
    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if self.scene:
                    self.scene.handleEvent(event)

            self.executeScene()

            pygame.display.flip()
            self.clock.tick(60)

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
    def render(self, screen):
        if self.currentState is not None:
           self.currentState.render(screen)        