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
# sound
#
class sound():
    #
    # __init__
    # Inicializa o mixer de som do Pygame.
    #
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
    #
    # load
    # Carrega um arquivo de som e o associa a um nome.
    # 
    # :param name: Nome associado ao som.
    # :param file_path: Caminho para o arquivo de som.
    #
    def load(self, name, file_path):
        try:
            self.sounds[name] = pygame.mixer.Sound(file_path)
            # print(f"Som '{name}' carregado com sucesso!")
        except pygame.error as e:
            print(f"Erro ao carregar o som '{file_path}': {e}")
    #
    # play
    # Reproduz um som.
    # 
    # :param name: Nome do som.
    # :param loops: Número de repetições (-1 para repetição infinita).    
    #
    def play(self, name, loops=0):
        if name in self.sounds:
            self.sounds[name].play(loops=loops)
        else:
            print(f"Som '{name}' não encontrado.")
    #
    # stop
    # Para um som em execução.
    # 
    # :param name: Nome do som.    
    #
    def stop(self, name):
        if name in self.sounds:
            self.sounds[name].stop()
        else:
            print(f"Som '{name}' não encontrado.")
    #
    # volume
    # Define o volume de um som.
    # 
    # :param name: Nome do som.
    # :param volume: Volume (0.0 a 1.0).
    #
    def volume(self, name, volume):
        if name in self.sounds:
            self.sounds[name].set_volume(volume)
        else:
            print(f"Som '{name}' não encontrado.")
    #
    # pause
    # Pausa todos os canais de som.
    #
    def pause(self):
        pygame.mixer.pause()
    #
    # unpause
    # Retoma todos os canais de som pausados.
    #
    def unpause(self):
        pygame.mixer.unpause()
    #
    # close
    # Para todos os canais de som.
    #
    def close(self):
        pygame.mixer.stop()