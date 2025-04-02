import pygame
import random
import time

pygame.init()
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка изображений
img_back = pygame.image.load('/Users/ermek/Desktop/AnimatedStreet.png')
img_player = pygame.image.load('/Users/ermek/Desktop/Player.png')
img_enemy = pygame.image.load('/Users/ermek/Desktop/Enemy.png')
img_coin = pygame.image.load('/Users/ermek/Desktop/coin.jpg')
img_newcoin = pygame.image.load("/Users/ermek/Desktop/new_coin.png")

# Масштабирование
img_coin = pygame.transform.scale(img_coin, (30, 30))
img_newcoin = pygame.transform.scale(img_newcoin, (30, 30))

# Шрифты и текст
font = pygame.font.SysFont("Verdana", 60)
image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Счётчики
n = 0
weigh_counter = 0

# Звук
pygame.mixer.music.load('/Users/ermek/Desktop/background.wav')
pygame.mixer.music.play(-1)
snd_crash = pygame.mixer.Sound('/Users/ermek/Desktop/crash.wav')

clock = pygame.time.Clock()
fps = 60

#класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = img_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
#класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = img_enemy
        self.rect = self.image.get_rect()
        self.speed = 10
        self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
#класс обычных монет
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = img_coin
        self.rect = self.image.get_rect()
        self.speed = 8
        self.random_rect()

    def random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.random_rect()
#класс монет с рандомным весом
class Coins_new(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = img_newcoin
        self.rect = self.image.get_rect()
        self.speed = 8
        self.generate()

    def generate(self):
        self.weigh = random.randint(1, 5)
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()

# Инициализация объектов
running = True
coin = Coins()
player = Player()
enemy = Enemy()
newcoin = Coins_new()
#создание спрайтов
all_sprites = pygame.sprite.Group(player, enemy, coin, newcoin)
enemy_sprites = pygame.sprite.Group(enemy)
coin_sprites = pygame.sprite.Group(coin)
new_coin_sprites = pygame.sprite.Group(newcoin)

# Главный игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()
    screen.blit(img_back, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    #проверки на коллизию
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        snd_crash.play()
        time.sleep(1)
        running = False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(1)

    if pygame.sprite.spritecollideany(player, coin_sprites):
        n += 1
        weigh_counter += 1
        coin.random_rect()

    if pygame.sprite.spritecollideany(player, new_coin_sprites):
        n += 1
        weigh_counter += newcoin.weigh
        newcoin.generate()

    # Перерисовка текста
    image_counter = font.render(f"{n}", True, "black")
    image_weigh = font.render(f"{weigh_counter}", True, "black")
    image_counter_rect = image_counter.get_rect(center=(370, 30))
    image_weigh_rect = image_weigh.get_rect(center=(320, 30))
    
    if n != 0 and n % 4 == 0:
        fps += 0.3
#вывод изображения
    screen.blit(image_counter, image_counter_rect)
    screen.blit(image_weigh, image_weigh_rect)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
