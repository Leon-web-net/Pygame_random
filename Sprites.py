import pygame, sys, random

#sprite = A class that combines a surface, a rect and ,any additional
#features like animations or sound

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect= self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("Futuristic Sniper Rifle Single Shot.wav")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair,target_group,True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self,picture_path,x,y):
        super().__init__()
        self.image=pygame.image.load(picture_path)
        self.rect=self.image.get_rect()
        self.rect.center = [x,y]

#general Setup
pygame.init()
clock=pygame.time.Clock()

#Game Screen
screen_width =1000
screen_height =800
screen=pygame.display.set_mode((screen_width,screen_height))
background =pygame.image.load("../Photos/sunset1.png")
pygame.mouse.set_visible(False)

#Crosshair
crosshair=Crosshair("../Photos/aim.png")

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Target
target_group= pygame.sprite.Group()
for target in range(20):
    new_Target=Target("../Photos/new_bullet.png",
                      random.randrange(0,screen_width),
                      random.randrange(0,screen_height))
    target_group.add(new_Target)

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type== pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()


    pygame.display.flip()
    screen.blit(background,(0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)

