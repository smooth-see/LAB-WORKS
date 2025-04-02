import pygame
import random
import time

pygame.init()

WIDTH=400                                       #ширина окна
HEIGHT=600
screen=pygame.display.set_mode((WIDTH, HEIGHT))

img_back=pygame.image.load('/Users/ermek/Desktop/AnimatedStreet.png') #загружаю картинки
img_player=pygame.image.load('/Users/ermek/Desktop/Player.png')
img_enemy=pygame.image.load("/Users/ermek/Desktop/Enemy.png")
img_coin=pygame.image.load("/Users/ermek/Desktop/new_coin.png")
img_coin=pygame.transform.scale(img_coin, (30, 30))

font = pygame.font.SysFont("Verdana", 60)          #создаю изображение для гейм овер и счетчика монет
image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))

n=0                                              #счетчик монет
image_counter=font.render(f"{n}", True, "black")   #рисует счетчик н                
image_counter_rect = image_counter.get_rect(center = (10, 570))

pygame.mixer.music.load('/Users/ermek/Desktop/background.wav')  #загружаю музыку
pygame.mixer.music.play(-1) #-1 бесконечный луп музыки 
snd_crash=pygame.mixer.Sound("/Users/ermek/Desktop/crash.wav")
clock=pygame.time.Clock()
fps=60

class Player(pygame.sprite.Sprite):      #создаю и помещаю игрока
    def __init__(self):
        super().__init__()
        self.image=img_player   #создаю плеера и помещаю его
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH//2               
        self.rect.bottom=HEIGHT
        self.speed = 5

    def move(self):                 
        keys=pygame.key.get_pressed()           #плеер реагирует на нажатие клавиш
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH

class Enemy(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()      #создаю и помещаю врага
        self.image=img_enemy
        self.rect=self.image.get_rect()
        self.speed=10
    def generate_random_rect(self):
        self.rect.left=random.randint(0, WIDTH-self.rect.w)
        self.rect.bottom=0                                         #рандомные координаты
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top>HEIGHT:
            self.generate_random_rect()

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=img_coin                #работает почти также как и класс враг
        self.rect=self.image.get_rect()
        self.speed=8
    def random_rect(self):
        self.rect.left=random.randint(0, WIDTH-self.rect.w)
        self.rect.bottom=0
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top>HEIGHT:
            self.random_rect()

running=True
coin=Coins()
player=Player()
enemy=Enemy()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy, coin)
coin_sprites=pygame.sprite.Group()
coin_sprites.add(coin)
enemy_sprites.add(enemy)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    player.move()
    screen.blit(img_back, (0,0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        snd_crash.play()
        time.sleep(1)                                              #столкновение с врагом
        running=False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()

        time.sleep(3)
    if pygame.sprite.spritecollideany(player, coin_sprites):
        n += 1
        image_counter = font.render(f"{n}", True, "black")                    #столкновение с монетой
        image_counter_rect = image_counter.get_rect(center = (10, 570))
        coin.random_rect()
    screen.blit(image_counter, image_counter_rect)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()