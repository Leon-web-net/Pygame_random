import pygame, sys, random
from pygame.locals import *
from pygame import mixer

def colour_checker(health):

    print(bullet_colour)
    if bullet_colour == "black":
        health =1
    elif bullet_colour == "red":
        health-=20
    elif bullet_colour == "orange":
        health-=10
    elif bullet_colour == "yellow":
        health-=5
    elif bullet_colour == "blue":
        health+=5
    elif bullet_colour == "green":
        health+=50
        if health>100:
            health = 100
    print(health)
    return health

def move(rect,player_movement):
    rect.x+= player_movement[0]
    rect.y += player_movement[1]

class Player(pygame.sprite.Sprite):
    #def __init__(self):
        #super().__init__()
        #self.image = pygame.Surface((100, 100))
        #self.image.fill("#3690e3")
        #self.rect = self.image.get_rect(
            #center=(screen_width/2, screen_height/2))



    #def update(self):
        #self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(0, random.randrange(0,screen_height))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10,5))
        self.colour = colour[random.randrange(0,len(colour)-1)]
        self.image.fill(self.colour)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        global hit, bullet_colour
        self.rect.x += 5
        #collide = pygame.Rect.colliderect(self.rect,player.rect)
        collide_soldier = pygame.Rect.colliderect(self.rect,player_rect)
        if collide_soldier:
            self.kill()
            hit =True
            bullet_colour = self.colour
            return self.colour


        if self.rect.x >screen_width or self.rect.x<0:
            self.kill()

def reset():
    global player_rect, health, health_bar
    print("reset")
    health = 100
    #player_rect = (20,screen_height-player_image.get_height())
    health_bar =pygame.transform.scale(health_bar,(50, 4))
    health_bar.fill("#02f771")

pygame.init()
timer = 0
health = 100
clock=pygame.time.Clock()
screen_width, screen_height =800, 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.mouse.set_visible(False)

player_image = pygame.image.load("Photos/player_soldier.png").convert_alpha()
player_image.set_colorkey((255,255,255))
health_bar = pygame.Surface((50,4))
health_bar.fill("#02f771")


player = Player()
#player_group = pygame.sprite.Group()
#player_group.add(player)

colour =["orange","yellow","blue","red"]
while len(colour)<10:
    colour.append(colour[random.randrange(0,len(colour)-1)])
colour.append("black")
colour.append("green")


bullet_group = pygame.sprite.Group()

hit =False
moving_right = False
moving_left = False
moving_up = False
moving_down = False

player_rect = pygame.Rect(20, screen_height-player_image.get_height(), player_image.get_width(), player_image.get_height())
health_bar_rect = pygame.Rect(player_rect.x,player_rect.y+5,health_bar.get_width(),health_bar.get_height())


while True:

    player_movement = [0,0]
    if moving_right:
        player_movement[0]+=5
    if moving_left:
        player_movement[0]-=5
    if moving_up:
        player_movement[1]-=5
    if moving_down:
        player_movement[1]+=5


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == pygame.MOUSEBUTTONDOWN:
            #bullet_group.add(player.create_bullet())

        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                moving_up = True
            if event.key == K_DOWN:
                moving_down = True

        if event.type == KEYUP:

            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_UP:
                moving_up = False
            if event.key == K_DOWN:
                moving_down = False

    if pygame.time.get_ticks() - timer > 2000:
        bullet_group.add(player.create_bullet())
        timer = pygame.time.get_ticks()


    move(player_rect,player_movement)

    if hit:
        health=colour_checker(health)
        #health = c
        hit = False
        if health <= 0:
            print("low")
            reset()
            print(health)
        health_bar = pygame.transform.scale(health_bar,(health/2, 4))

    #draw
    screen.fill((30,30,30))
    #player_group.update()
    b=bullet_group.update()
    bullet_group.draw(screen)
    #player_group.draw(screen)
    screen.blit(health_bar,(player_rect.x,player_rect.midtop[1]-5))
    screen.blit(player_image, (player_rect.x, player_rect.y))
    pygame.display.flip()
    clock.tick(30)