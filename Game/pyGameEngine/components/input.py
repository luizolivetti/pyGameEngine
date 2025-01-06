import pygame

#
# Class input
#
class input:
    #
    # __init__
    #
    def __init__(self):
        self.keyBindings = {}  # Dicionário de mapeamento de teclas para ações
        self.continuous_keys = []  # Lista de teclas pressionadas de forma contínua
    #
    # bindKey
    #
    def bindKey(self, key, action):
        """Mapeia uma tecla a uma ação."""
        self.keyBindings[key] = action
    #
    # handleInput
    #
    def handleInput(self, continuous=False):
        """
        Lida com eventos de pressionar teclas (modo contínuo ou não contínuo).
        
        :param continuous: Se True, lida com teclas pressionadas continuamente.
        """
        if continuous:
            # Comportamento contínuo: Verifica constantemente as teclas pressionadas
            keys = pygame.key.get_pressed()  # Obtém o estado de todas as teclas
            for key, action in self.keyBindings.items():
                if keys[key]:
                    action()
        else:
            # Comportamento não contínuo: Trata eventos de pressionamento de tecla
            for event in pygame.event.get():  # Lê os eventos da fila
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    action = self.keyBindings.get(event.key)
                    if action:
                        action()
