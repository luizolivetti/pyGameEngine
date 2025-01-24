#  ----------------------------------------------------------
#  physics
#  Classe COMPONENT para physics  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 03/01/2025
#  @revisor                   @data 
#  ----------------------------------------------------------
import inspect
import time
#
# Inicializa a classe de física para um objeto.
#
# :param x: Posição inicial no eixo X.
# :param y: Posição inicial no eixo Y.
# :param width: Largura do objeto.
# :param height: Altura do objeto.
# :param velocityX: Velocidade inicial no eixo X.
# :param velocityY: Velocidade inicial no eixo Y.
#
class physics:
    #
    # instances
    #
    instances = []
    #
    # __init__
    #
    def __init__(self, rect, velocityX=0, velocityY=0, gravity=0.5, gravity_direction=(0, 1), maxVelocityX=5, maxVelocityY=10, acceleration=0.1, friction=0.9, screenWidth=0, screenHeight=0):
        self.rect = rect  # pygame.Rect(entityX, entityY, entityWidth, entityHeight)  # Representa a posição e tamanho da entidade
        self.velocityX = velocityX  # Velocidade no eixo X
        self.velocityY = velocityY  # Velocidade no eixo Y
        self.gravity = gravity  # Gravidade (ajustável)
        self.gravity_direction = gravity_direction  # Direção da gravidade
        self.maxVelocityX = maxVelocityX  # Velocidade máxima no eixo X
        self.maxVelocityY = maxVelocityY  # Velocidade máxima no eixo Y
        self.acceleration = acceleration  # Aceleração para movimento no eixo X
        self.friction = friction  # Fricção para desacelerar a entidade
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.instances.append(self.whois())
        self.currentCaller = None
        self.inGround = False # to-do : monitorar se está no chão
    #
    # whois
    #
    def whois(self):
        # Obtém a pilha de chamadas e captura o chamador da instância atual
        stack = inspect.stack()
        if len(stack) > 2:
            caller = stack[2]
            caller_frame = caller.frame
            caller_name = caller_frame.f_locals.get('self', None)
            return caller_name
        return None    
    #
    # Aplica a gravidade ao objeto, fazendo com que ele caia.
    #
    # :param reverse: inverte o sentido da gravidade, fazendo com que o objeto suba.
    #
    def applyGravity(self):
        # Calcula a aceleração da gravidade com base na direção
        self.velocityX += self.gravity * self.gravity_direction[0]
        self.velocityY += self.gravity * self.gravity_direction[1]
        self.handleCollision(self.velocityX, self.velocityY)     
    #
    # Move a entidade de acordo com a velocidade nos eixos X e Y.
    #
    # :param dx: Deslocamento no eixo X.
    # :param dy: Deslocamento no eixo Y.
    #        
    def jump(self, dx, dy):
        # Quem me chamou?
        self.currentCaller = self.whois()
        # Verifica se está no chão antes de aplicar o pulo
        if self.inGround:
           self.velocityY -= self.maxVelocityY # Aplica uma velocidade negativa para impulsionar a entidade para cima
           self.handleCollision(dx, dy)
           self.update()
           self.inGround = False  # Marca que não está mais no chão    
    #
    # Move a entidade de acordo com a velocidade nos eixos X e Y.
    #
    # :param dx: Deslocamento no eixo X.
    # :param dy: Deslocamento no eixo Y.
    #
    def move(self, dx, dy):
        # Quem me chamou?
        self.currentCaller = self.whois()
        self.handleCollision(dx, dy)
        self.update()
    #
    # Atualiza o estado da física da entidade, aplicando gravidade
    # e movimentando o objeto.
    #
    def update(self):
        # Quem me chamou?
        if(self.currentCaller == None):
            self.currentCaller = self.whois()
        # Aplica a gravidade
        self.applyGravity()
        # Limita a velocidade
        if abs(self.velocityX) > self.maxVelocityX:
            self.velocityX = self.maxVelocityX if self.velocityX > 0 else -self.maxVelocityX
        if abs(self.velocityY) > self.maxVelocityY:
            self.velocityY = self.maxVelocityY if self.velocityY > 0 else -self.maxVelocityY
        # Desacelera com a fricção
        self.velocityX *= self.friction
        self.velocityY *= self.friction    
        # 
        self.screenLimits()
    #
    # Verifica colisão com outra entidade.
    #
    # :param other: Outra instância de Physics para verificação de colisão.
    # :return: True se houver colisão, False caso contrário.
    #
    def checkCollision(self, other):
        return self.rect.colliderect(other)
    #
    # screenLimits
    #
    def screenLimits(self):
        # Limitar o personagem no eixo X
        if self.rect.left < 0:  # Verifica se ultrapassou o limite esquerdo
            self.rect.left = 0
        elif self.rect.right > self.screenWidth:  # Verifica se ultrapassou o limite direito
            self.rect.right = self.screenWidth
        # Limitar o personagem no eixo Y (no topo e fundo da tela)
        if self.rect.top < 0:  # Verifica se ultrapassou o limite superior
            self.rect.top = 0
            self.velocityY = 0  # Impede que a velocidade Y continue afetando
        elif self.rect.bottom > self.screenHeight:  # Verifica se ultrapassou o limite inferior
            self.rect.bottom = self.screenHeight
            self.velocityY = 0  # Para a queda ao atingir o fundo  
    #
    # handleCollision
    # Verifica colisão com outra entidade.
    # Verifica colisões durante o movimento e ajusta a posição
    #
    def handleCollision(self, dx, dy):
        # Tentativa de mover o objeto
        self.rect.x += dx
        self.rect.y += dy
        self.inGround = False  # Assume que não está no chão inicialmente
        # Verifica colisões com outros objetos
        for obstacle in self.instances:
            if obstacle != self.currentCaller and self.checkCollision(obstacle.rect):
                # Ajustar movimento dependendo da direção da colisão
                if dx > 0:  # Colisão com a direita
                    self.rect.right = obstacle.rect.left
                elif dx < 0:  # Colisão com a esquerda
                    self.rect.left = obstacle.rect.right
                # Ajustar movimento vertical
                if dy > 0:  # Colisão com o fundo
                    self.rect.bottom = obstacle.rect.top
                    self.velocityY = 0  # Parar movimento vertical
                    self.inGround = True  # O personagem está no chão
                elif dy < 0:  # Colisão com o topo
                    self.rect.top = obstacle.rect.bottom
                    self.velocityY = 0  # Parar movimento vertical
                # Redefine a posição após colisão para não ultrapassar obstáculos
                break          