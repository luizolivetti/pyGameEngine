#  ----------------------------------------------------------
#  Scene
#  Classe CORE para Scene  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
#
# configurations
#
from settings import settings
#
# core
#
from pyGameEngine.core.sound import sound
from pyGameEngine.core.screen import screen
#
# scene
#
class scene(screen, settings):
    #
    # __init__
    #
    def __init__(self, background):
        self.background = background
        self.snd = None
        self.ways = None
        self.backgroundImage =''
        self.sounds = []
        self.entities = []
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
    # handle_event
    #
    def handleEvent(self, event):
        # inicia sons se não tiver iniciado
        self.startSound()
        # handleEvent de entidades
        for entity in self.entities:
            entity.handleEvent(event)
    #
    # handleEvents
    #
    def handleEvents(self, events):
        # inicia sons se não tiver iniciado
        self.startSound()
        # handleEvents de entidades
        for entity in self.entities:
            entity.handleEvents(events)   
    #
    # update
    #
    def update(self): 
        # update de entidades
        for entity in self.entities:
            entity.update()
    #
    # render
    #
    def render(self, screen):
        # carrega sons não carregados
        # inicia sons não iniciados
        self.loadSounds()
        self.playSounds()
        # render de entidades            
        for entity in self.entities:
            entity.render(screen) 