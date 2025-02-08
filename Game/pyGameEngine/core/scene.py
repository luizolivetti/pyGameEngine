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
from pyGameEngine.components.physics import physics
#
# cores
#
from pyGameEngine.core.extends.entity.layer import layer
from pyGameEngine.core.extends.entity.player import player
from pyGameEngine.core.extends.entity.land import land
#
# scene
#
class scene():
    #
    # __init__
    #
    def __init__(self, backgroundColor, inputContinuous=True, window=None, sceneSize=(0,0)):
        # scene properties
        self.background = backgroundColor
        self.window = window
        self.media = media() 
        self.input = input() 
        self.entities = []
        self.players = {} 
        self.lands = {}   
        self.layerImage = {}        
        self.layerImageWidth = {}
        self.layerImageHeight = {}  
        self.cameraX = 0
        self.cameraY = 0
        self.position = (0,0)
        self.callFor = None
        # scene size
        if sceneSize==(0,0) and window is not None:
            self.sceneSize = (window.handler.get_width(), window.handler.get_height())  
        else:
            self.sceneSize = sceneSize    
        self.window.background(backgroundColor)
        # input controls on the scene
        self.inputContinuous = inputContinuous  
    #
    # execute
    #
    def execute(self, sceneState):
        self.callFor = sceneState          
    #
    # mount
    # 
    def mount(self):
        physics.instances.clear()  
    #
    # addLayer
    # Layers to compose the scene
    # Layers are type of entity, a image with position and size
    #
    def addLayer(self, name, layer):
        self.layerImage[name] = layer        
        self.layerImageWidth[name] = layer.width
        self.layerImageHeight[name] = layer.height  
        self.addEntity(layer)
    #
    # addLand
    #
    def addLand(self, name, land):
        self.lands[name] = land        
        self.addEntity(land)          
    #
    # addPlayer
    #
    def addPlayer(self, name, player):
        self.players[name] = player          
        self.addEntity(player)   
    #
    # addEntity
    # Entites to players, enemies, platforms, etc
    #
    def addEntity(self, entity):
        # Set limits of the scene
        if isinstance(entity.physics, physics):
            entity.physics.screenWidth = self.window.handler.get_width()
            entity.physics.screenHeight = self.window.handler.get_height()
        # Add entity to the scene
        self.entities.append(entity)        
    #
    # rollScene
    #
    def rollScene(self, player):
        # proporsional divisor
        divisor = self.sceneSize[0] * 0.1
        if divisor <= 0:
            divisor=1
        # calculating X axis for camera 
        self.cameraX = max(0, min(self.cameraX, self.sceneSize[0] - self.window.handler.get_width()))
        self.cameraX += (player.x - self.cameraX - self.window.handler.get_width() / divisor) * 0.1
        # moving elements layer
        for name, layerImage in self.layerImage.items():
            if hasattr(layerImage, "renderer") and hasattr(layerImage.renderer, "rect"):
                layerImage.renderer.rect.topleft = (layerImage.x-self.cameraX, layerImage.renderer.rect.y)    
        # moving elements land
        for name, land in self.lands.items():
            if hasattr(land, "renderer") and hasattr(land.renderer, "rect"):
                land.renderer.rect.topleft = (land.x-self.cameraX, land.renderer.rect.y)    
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
            if isinstance(entity, player):
                 self.rollScene(entity)  
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