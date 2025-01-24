#  ----------------------------------------------------------
#  Scene
#  Classe CORE para Scene  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
#
# components
#
from pyGameEngine.components.input import input
from pyGameEngine.components.media import media
#
# scene
#
class scene():
    #
    # __init__
    #
    def __init__(self, background, inputContinuous=True, window=None):
        # 
        self.background = background
        self.window = window
        self.media = media() 
        self.input = input() 
        self.entities = []
        # scene background can overwrite window background
        self.window.background(background)
        # input controls on the scene
        self.inputContinuous = inputContinuous
    #
    # addBackground
    #
    def addLayerBackground(self, layer):
        self.backgroundImage = layer        
        self.backgroundImageWidth = layer.width
        self.backgroundImageHeight = layer.height    
        self.addEntity(layer)
    #
    # addEntity
    #
    def addEntity(self, entity):
        self.entities.append(entity)        
    #
    # moveScene
    # 
    def moveScene(self, dx, dy):
        pass 
    #
    # handle_event
    #
    def handleEvent(self, event):
        self.input.handleInput(self.inputContinuous)
        # inicia sons se não tiver iniciado
        self.media.startSound()      
        # handleEvent de entidades
        for entity in self.entities:
            entity.handleEvent(event)
        # 
        self.update()
    #
    # handleEvents
    #
    def handleEvents(self, events):
        self.input.handleInput(self.inputContinuous)
        # inicia sons se não tiver iniciado
        self.media.startSound()             
        # handleEvents de entidades
        for entity in self.entities:
            entity.handleEvents(events)   
        # 
        self.update()            
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
        # inicia e carrega sons não carregados
        self.media.loadSounds()
        self.media.playSounds()    
        # render de entidades            
        for entity in self.entities:
            entity.render(screen) 