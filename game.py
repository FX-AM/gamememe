import pygame
pygame.init()
window = pygame.display.set_mode((800, 500))
background = pygame.image.load("realistic-polygonal-background_23-2148922432.jpg")
#window.fill((0, 0, 0))
clock = pygame.time.Clock()
#pygame.mixer.musik.load("")
#pygame.mixer.music.play(-1)
class GameSprite():
    def __init__(self, x=0, y=0, width=10, height=10, step=0, image_sprite=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x=x
        self.y=y
        self.image =pygame.image.load(image_sprite)
        self.image =pygame.transform.scale(self.image, (self.width, self.height))
        self.step = step
    def draw(self, x, y,):
        window.blit(self.image, (self.x, self.y))  
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.step
        if keys[pygame.K_s]:
            self.y += self.step
        if keys[pygame.K_a]:
            self.x -= self.step
        if keys[pygame.K_d]:
            self.x += self.step
class Player2(GameSprite):
    def draw(self, x, y,):
        window.blit(self.image, (self.x, self.y))  
    def __init__(self, x=0, y=0, width=10, height=10, step=0, image_sprite=""):
        super().__init__(x, y, width, height, step, image_sprite)
        self.image = pygame.image.load(image_sprite)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def updute(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.step
        if keys[pygame.K_DOWN]:
            self.y += self.step
        if keys[pygame.K_LEFT]:
            self.x -= self.step
        if keys[pygame.K_RIGHT]:
            self.x += self.step
class Player1(GameSprite):
    def __init__(self, x=0, y=0, width=10, height=10, step=0, image_sprite=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x=x
        self.y=y
        self.image =pygame.image.load(image_sprite)
        self.image =pygame.transform.scale(self.image, (self.width, self.height))
        self.step = step
    def draw(self, x, y,):
        window.blit(self.image, (self.x, self.y))  
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.step
        if keys[pygame.K_s]:
            self.y += self.step
        if keys[pygame.K_a]:
            self.x -= self.step
        if keys[pygame.K_d]:
            self.x += self.step
#class ball(GameSprite):
#    def __init__(self, x=0, y=0, width=10, height=10, step=0, image_sprite=""):
#        self.x = x
#        self.y = y
#        self.width = width
#        self.height = height
#        self.x=x
#        self.y=y
#        self.image =pygame.image.load(image_sprite)
#        self.image =pygame.transform.scale(self.image, (self.width, self.height))
#        self.step = step
#    def draw(self, x, y,):
#        window.blit(self.image, (self.x, self.y))  
#def move(self):
#    self.x += self.speed_x
#    self.y += self.speed_y
#
#    if self.x < self.radius or self.x >= window - self.radius:
#        self.speed_x *= -1
#    if self.y < self.radius:
#        self.speed_y *= -1
player2 = GameSprite(100, 100, 100, 100, 10, "pngwing.com (7).png")
player1 = GameSprite(100, 100, 100, 100, 10, "pngwing.com1.png")
#ball = GameSprite(100, 100, 100, 100, 10, "")
player1.draw(100, 100)
player2.draw(101, 100)

game=True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(background, (0, 0))

#def collide(self, other):
#    if self.rect.colliderect(self.x, self.y):
#        self.kill()
#    player1.update()
#    player2.update()

pygame.display.update()
clock.tick(40)
pygame.quit()