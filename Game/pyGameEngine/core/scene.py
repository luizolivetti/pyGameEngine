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
class scene(screen, sound, settings):
    #
    # 
    #
    background = (0,0,0)
    backgroundImage =''
    #
    # __init__
    #
    def __init__(self, background):
        sound.__init__(self)
        self.entities = []
        self.background = background
    #
    # addEntity
    #
    def addEntity(self, entity):
        self.entities.append(entity)
    #
    # handle_event
    #
    def handleEvent(self, event):
        for entity in self.entities:
            entity.handleEvent(event)
    #
    # handleEvents
    #
    def handleEvents(self, events):
        for entity in self.entities:
            entity.handleEvents(events)            
    #
    # update
    #
    def update(self):
        for entity in self.entities:
            entity.update()
    #
    # render
    #
    def render(self, screen):
        for entity in self.entities:
            entity.render(screen)
    #
    # addSound
    #
    def addSound(self, name, file):
        self.load(name, file)    