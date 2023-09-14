import pygame, sys
from pygame.locals import *
import random, math
import numpy as np
from Vector_method import d_collision

class Player(pygame.sprite.Sprite):
    def __init__(self,colour,radius):
        super().__init__()
        self.image = pygame.Surface([radius,radius])
        self.colour = colour
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, self.colour,(radius/2,radius/2), radius=radius/2)
        self.rect = self.image.get_rect()
        self.vel_x = p_velx
        self.vel_y = p_vely


    def update(self):


        # if pygame.sprite.spritecollide(player,ball_group, False):    # for rectangles
        #     ball_group.ball_player_collision()
        ball_group.update(self.rect.centerx,self.rect.centery)
        if self.rect.x < 0 or self.rect.x + self.image.get_width() > screen_width:
            self.vel_x*=-1
            if self.rect.x <0:
                self.rect.x =0
            else:
                self.rect.x -=1
        if self.rect.y < 0 or self.rect.y + self.image.get_height() > screen_height:
            self.vel_y*=-1
            if self.rect.y < 0:
                self.rect.y = 0
            else:
                self.rect.y -= 1

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y



class Ball(pygame.sprite.Sprite):
    def __init__(self,radius, colour):
        super().__init__()
        self.image = pygame.Surface([radius,radius])
        self.colour = colour
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, self.colour, (radius / 2, radius / 2), radius=radius / 2)
        self.X_vel = ball_x_vel
        self.Y_vel = ball_y_vel
        self.rect = self.image.get_rect(center =(random.randrange(radius,screen_width-radius),random.randrange(radius,screen_height-radius)))


    def update(self,*args):
        self.rect.x += self.X_vel
        self.rect.y += self.Y_vel



        p_center_x = args[0]
        p_center_y = args[1]
        x_dist = self.rect.centerx - p_center_x
        y_dist = self.rect.centery - p_center_y
        distance = pow((pow(x_dist,2)+pow(y_dist,2)),0.5)
        if distance<shortest_distance:
            print("\n distance:", distance)
            #ball_group.ball_player_collision(p_center_x,p_center_y, self.rect.centerx, self.rect.centery)
            player.vel_x,player.vel_y, self.X_vel, self.Y_vel = d_collision(p_center_x, p_center_y, self.rect.centerx, self.rect.centery, player.vel_x,player.vel_y, self.X_vel,
                                                self.Y_vel)


        if self.rect.x < 0 or self.rect.x + self.image.get_width() > screen_width:
            self.X_vel *= -1
        if self.rect.y <= 0 or self.rect.y + self.image.get_height() > screen_height:
            self.Y_vel *= -1


    # def ball_player_collision(self,p_center_x,p_center_y, B_center_x, B_center_y):
    #     e,w,self.X_vel,self.Y_vel = d_collision(p_center_x,p_center_y,B_center_x,B_center_y,0,0,self.X_vel,self.Y_vel)

    def seperate(self, distance,x_dist, y_dist, p_center_x,p_center_y):
        push_f = 60 - distance
        push_x = x_dist/(distance) * push_f
        push_y = y_dist/(distance) * push_f
        return p_center_x+push_x, p_center_y+push_y



pygame.init()
screen=pygame.display.set_mode((800,800))
clock=pygame.time.Clock()
screen_width = screen.get_width()
screen_height = screen.get_height()

current_time = 0
button_press_time = 0

#Player
p_velx = 2
p_vely = 2
p_radius = 60
player = Player(radius=p_radius, colour="red")
player_group = pygame.sprite.Group()
player_group.add(player)


#Ball
B_radius = 60
ball_x_vel = 2
ball_y_vel = 2
ball = Ball(radius=B_radius, colour="green", )
ball_group = pygame.sprite.Group()
ball_group.add(ball)

shortest_distance = (B_radius+p_radius)/2
for i in range(10):
    ball = Ball(radius=B_radius, colour="blue")
    ball_group.add(ball)

while True:

    screen.fill("#29CCDC")
    # ball_group.update()

    player_group.update()
    ball_group.draw(screen)
    player_group.draw(screen)



    # if pygame.time.get_ticks() - current_time >2000:
    #     current_time = pygame.time.get_ticks()
    #     ball = Ball(radius=B_radius, colour="blue")
    #     ball_group.add(ball)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.type == pygame.KEYDOWN:
        pass


    #print(f"current time: {current_time}Button Press Time: {button_press_time}")
    pygame.display.flip()
    clock.tick(80)