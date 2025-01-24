#  ----------------------------------------------------------
#  media
#  Classe COMPONENTE para media player  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 23/01/2025
#  @revisor                   @data 
#  ----------------------------------------------------------
import pygame
#
# components
#
from pyGameEngine.components.sound import sound
#
# media
#
class media():
    #
    # __init__
    #
    def __init__(self):
        self.snd = None
        self.sounds = []
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