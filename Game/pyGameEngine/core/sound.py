#  ----------------------------------------------------------
#  sound
#  Classe CORE para sound 
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 20/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
#  fonte de sons 
#  https://pixabay.com/pt/music/search/genre/m%C3%BAsicas%20infantis%20assustadoras/
import pygame
#
# Class screen
#
import pygame

class sound:
    #
    # __init__
    #
    def __init__(self):
        """
        Inicializa o mixer de som do Pygame.
        """
        pygame.mixer.init()
        self.sounds = {}
    #
    # load
    #
    def load(self, name, file_path):
        """
        Carrega um arquivo de som e o associa a um nome.
        
        :param name: Nome associado ao som.
        :param file_path: Caminho para o arquivo de som.
        """
        try:
            self.sounds[name] = pygame.mixer.Sound(file_path)
            # print(f"Som '{name}' carregado com sucesso!")
        except pygame.error as e:
            print(f"Erro ao carregar o som '{file_path}': {e}")
    #
    # play
    #
    def play(self, name, loops=0):
        """
        Reproduz um som.
        
        :param name: Nome do som.
        :param loops: Número de repetições (-1 para repetição infinita).
        """
        if name in self.sounds:
            self.sounds[name].play(loops=loops)
        else:
            print(f"Som '{name}' não encontrado.")
    #
    # stop
    #
    def stop(self, name):
        """
        Para um som em execução.
        
        :param name: Nome do som.
        """
        if name in self.sounds:
            self.sounds[name].stop()
        else:
            print(f"Som '{name}' não encontrado.")
    #
    # volume
    #
    def volume(self, name, volume):
        """
        Define o volume de um som.
        
        :param name: Nome do som.
        :param volume: Volume (0.0 a 1.0).
        """
        if name in self.sounds:
            self.sounds[name].set_volume(volume)
        else:
            print(f"Som '{name}' não encontrado.")
    #
    # pause
    #
    def pause(self):
        """
        Pausa todos os canais de som.
        """
        pygame.mixer.pause()
    #
    # unpause
    #
    def unpause(self):
        """
        Retoma todos os canais de som pausados.
        """
        pygame.mixer.unpause()
    #
    # stop
    #
    def stop(self):
        """
        Para todos os canais de som.
        """
        pygame.mixer.stop()