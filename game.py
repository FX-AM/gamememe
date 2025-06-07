import pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ракетка і цегла")

# Завантаження фону
background = pygame.image.load("realistic-polygonal-background_23-2148922432.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Клас базового спрайта
class GameSprite:
    def __init__(self, x, y, width, height, step, image_sprite):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.step = step
        self.image = pygame.image.load(image_sprite)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self):
        window.blit(self.image, (self.x, self.y))

# Клас гравця (ракетка)
class Player(GameSprite):
    def update(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.y > 0:
            self.y -= self.step
        if keys[down_key] and self.y + self.height < HEIGHT:
            self.y += self.step
        self.rect.topleft = (self.x, self.y)

# Клас м'яча
class Brick(GameSprite):
    def __init__(self, x, y, width, height, step, image_sprite, speed_x, speed_y):
        super().__init__(x, y, width, height, step, image_sprite)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Відскок від верхньої і нижньої стіни
        if self.y <= 0 or self.y + self.height >= HEIGHT:
            self.speed_y *= -1
        # Відскок від правої стіни
        if self.x + self.width >= WIDTH:
            self.speed_x *= -1


        self.rect.topleft = (self.x, self.y)

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            self.speed_x *= -1

# Ініціалізація гравця і м'яча
player = Player(50, HEIGHT//2 - 100, 85, 100, 7, "pngwing.com.png")
brick = Brick(WIDTH//2, HEIGHT//2, 50, 50, 0, "brick.png", speed_x=5, speed_y=5)

# Шрифти
font = pygame.font.SysFont('Arial', 36)
big_font = pygame.font.SysFont('Arial', 60)

hearts = 3
remaining_time = 60
# Початковий час у мілісекундах
start_ticks = pygame.time.get_ticks()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # Оновлення положення гравця
    player.update(pygame.K_w, pygame.K_s)
    brick.move()

    # Перевірка зіткнення м'яча і ракетки
    brick.check_collision(player)


    # Якщо м'яч пройшов за ліву межу - очко AI (у нас немає AI, просто рахунок)
    if brick.x <= 0:
        hearts -= 1
        brick.x, brick.y = WIDTH//2, HEIGHT//2
        brick.speed_x *= -1

    # Малюємо все
    window.blit(background, (0, 0))
    player.draw()
    brick.draw()

    # Відображення рахунку
    heartss = font.render(f"Життя: {hearts} ", True, (255, 255, 255))
    window.blit(heartss, (WIDTH//2 - heartss.get_width()//2, 20))
    # Відображення часу
    time_text = font.render(f"Час: {remaining_time}", True, (255, 255, 255))
    window.blit(time_text, (10, 10))

    # Зменшуємо час
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    remaining_time = max(0, 60 - int(seconds_passed))

    if remaining_time == 0:
        win = big_font.render("Ти виграв!", True, (0, 255, 0))
        window.blit(win, (WIDTH//2 - win.get_width()//2, HEIGHT//2 - win.get_height()//2))
        
    # Якщо життя закінчилися, показуємо текст
    if hearts <= 0:
        game_over_text = big_font.render("Гра закінчена!", True, (255, 0, 0))
        window.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - game_over_text.get_height()//2))
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()