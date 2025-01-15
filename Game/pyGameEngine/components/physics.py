#  ----------------------------------------------------------
#  physics
#  Classe COMPONENT para physics  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 03/01/2025
#  @revisor                   @data 
#  ----------------------------------------------------------
import inspect
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
    instances =[]
    #
    # __init__
    #                         
    def __init__(self, rect, velocityX=0, velocityY=0, gravity=0.5, maxVelocityX = 5, maxVelocityY = 10, acceleration = 0.1, friction = 0.9):
        self.rect = rect # pygame.Rect(entityX, entityY, entityWidth, entityHeight)  # Representa a posição e tamanho da entidade
        self.velocityX = velocityX  # Velocidade no eixo X
        self.velocityY = velocityY  # Velocidade no eixo Y
        self.gravity = gravity   # Gravidade (ajustável)
        self.maxVelocityX = maxVelocityX  # Velocidade máxima no eixo X
        self.maxVelocityY = maxVelocityY  # Velocidade máxima no eixo Y
        self.acceleration = acceleration  # Aceleração para movimento no eixo X
        self.friction = friction  # Fricção para desacelerar a entidade
        self.instances.append(self.whois())
    #
    # whois
    #
    def whois(self):
        # Obtém a pilha de chamadas e captura o chamador da instância atual
        stack = inspect.stack()
        # O chamador é o segundo item na pilha (o primeiro é o próprio construtor __init__)
        if len(stack) > 2:
            caller = stack[2]
            caller_frame = caller.frame
            # Podemos obter o nome do arquivo e a linha, ou o próprio objeto
            caller_name = caller_frame.f_locals.get('self', None)
            return caller_name
        return None
    # 
    # Aplica a gravidade ao objeto, fazendo com que ele caia.
    # 
    def applyGravity(self):
        self.velocityY += self.gravity
        self.move(0, self.velocityY)
    # 
    # Move a entidade de acordo com a velocidade nos eixos X e Y.
    # 
    # :param dx: Deslocamento no eixo X.
    # :param dy: Deslocamento no eixo Y.
    # 
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    # 
    # Atualiza o estado da física da entidade, aplicando gravidade
    # e movimentando o objeto.
    # 
    def update(self):
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
    # Verifica colisão com outra entidade.
    # 
    # :param other: Outra instância de Physics para verificação de colisão.
    # :return: True se houver colisão, False caso contrário.
    # 
    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)
    
    # ????

    # 
    # Define uma nova posição para a entidade.
    # 
    # :param x: Nova posição no eixo X.
    # :param y: Nova posição no eixo Y.
    # 
    def setPosition(self, x, y):
        self.rect.topleft = (x, y)
    # 
    #  Controla o movimento horizontal (esquerda/direita) com aceleração.
    #  :param direction: 1 para direita, -1 para esquerda, 0 para parar.
    # 
    def moveHorizontally(self, direction):
        if direction != 0:
            self.velocityX += self.acceleration * direction
        else:
            # Aceleração negativa (desaceleração)
            if abs(self.velocityX) > self.acceleration:
                self.velocityX -= self.acceleration * (1 if self.velocityX > 0 else -1)
            else:
                self.velocityX = 0  # Para quando a desaceleração for suficiente

        # Aplicar fricção
        self.velocityX *= self.friction
    # 
    # check_if_on_ground
    # 
    def ifOnGround(self, ground_level):
        return self.rect.bottom >= ground_level        
    # 
    # Aplica um impulso de pulo ao objeto.
    # 
    # :param strength: Força do pulo.
    # 
    def jump(self, strength=10, ground_level=0):
        if self.ifOnGround(ground_level):  # Supondo que o chão esteja no fundo da tela
            self.velocityY = -strength  # Impulso para cima
