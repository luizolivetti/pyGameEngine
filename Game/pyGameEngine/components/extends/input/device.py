#  ----------------------------------------------------------
#  Device
#  Classe abstrata/interface para controle dos devices  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 07/01/2025
#  @revisor                   @data 
#  ----------------------------------------------------------
from abc import ABC, abstractmethod
#
# device
#
class device(ABC):
    #
    # getHandler
    # Return dict defined to handler with device input
    #
    @abstractmethod
    def getHandler(self):
        pass
    #
    # device handler
    # Add dict defined to handler with device input
    #
    @abstractmethod
    def addHandler(self, key, entity, action):
        pass
    #
    # remHandler
    # Remove dict defined to handler with device input
    #
    @abstractmethod
    def remHandler(self, key):
        pass


