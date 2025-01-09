#  ----------------------------------------------------------
#  Scene
#  Classe CORE para Scene  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
#
# settings
#
from settings import settings
#
# core
#
from pyGameEngine.core.sound import sound
from pyGameEngine.core.screen import screen
#
# components
#
from pyGameEngine.components.input import input
#
# scene
#
class scene(screen, settings):
    #
    # __init__
    #
    def __init__(self, background, game, inputContinuous=True):
        self.game = game
        self.background = background
        self.snd = None
        self.ways = None
        self.backgroundImage =''
        self.sounds = []
        self.entities = []
        self.input = input()  
        self.inputContinuous = inputContinuous
    #
    # addEntity
    #
    def addEntity(self, entity):
        self.entities.append(entity)
    #
    # addSound
    #
    def addSound(self, name, file, loop, volume):
        self.sounds.append({'name': name, 'file': file, 'loop': loop, 'volume': volume})   
    #
    # startSound
    #
    def startSound(self):
        if self.snd is None:
            self.snd = sound()
    #
    # loadSound
    #
    def loadSounds(self):
        self.startSound()
        for sound in self.sounds:
            if sound['name'] not in self.snd.sounds:
                self.snd.load(sound['name'], sound['file'])           
    #
    # playSounds
    #
    def playSounds(self):
        # handleEvent de sons
        if len(self.sounds)>0:
            for sound in self.sounds:
                self.snd.play(sound['name'], sound['loop'])
                self.snd.volume(sound['name'], sound['volume']) 
    #
    # playSounds
    #
    def stopSounds(self):
        # handleEvent de sons
        if len(self.sounds)>0:
            for sound in self.sounds:
                if self.snd is not None:
                    self.snd.stop(sound['name'])                
                    self.snd.close()
    #
    # nextScene
    # 
    def nextScene(self, state):
        self.stopSounds()
        self.game.setScene(state)
    #
    # previousScene
    #
    def previousScene(self):
        self.stopSounds()
        self.game.setScene(self.game.previousState)   
    #
    # handle_event
    #
    def handleEvent(self, event):
        self.input.handleInput(self.inputContinuous)
        # inicia sons se não tiver iniciado
        self.startSound()
        # handleEvent de entidades
        for entity in self.entities:
            entity.handleEvent(event)
    #
    # handleEvents
    #
    def handleEvents(self, events):
        self.input.handleInput(self.inputContinuous)
        # inicia sons se não tiver iniciado
        self.startSound()
        # handleEvents de entidades
        for entity in self.entities:
            entity.handleEvents(events)   
    #
    # update
    #
    def update(self): 
        self.input.handleInput(self.inputContinuous)
        # update de entidades
        for entity in self.entities:
            entity.update()
    #
    # render
    #
    def render(self, screen):
        # carrega sons não carregados
        self.loadSounds()
        # inicia sons não iniciados
        self.playSounds()
        # render de entidades            
        for entity in self.entities:
            entity.render(screen) 