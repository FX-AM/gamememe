import pygame
pygame.init()
window = pygame.display.set_mode((800, 500))
background = pygame.image.load("realistic-polygonal-background_23-2148922432.jpg")
#window.fill((0, 0, 0))
clock = pygame.time.Clock()

class GameSprite():
    def __init__(self, x=0, y=0, width=10, height=10, step=0, image_sorite=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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
player = GameSprite(100, 100, 100, 100, 10, "pngwing.com.png")
game=True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
    player.draw(100, 100)
    window.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(40)
