import pygame, sys

from pygame.locals import  *

pygame.init()

clock =pygame.time.Clock()
pygame.display.set_caption("My Pygame Window")
window_size = (600, 400)

screen =pygame.display.set_mode(window_size,0,32)
display = pygame.Surface((300, 200))

player_image = pygame.image.load("Photos/player.png")
player_image.set_colorkey((255,255,255))
grass_image = pygame.image.load("Photos/grass.png")
TILE_SIZE = grass_image.get_width()
dirt_image = pygame.image.load("Photos/dirt.png")
game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {"top":False, "bottom":False, "right":False, "left":False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] >0:
            rect.right = tile.left
            collision_types["right"] =True
        elif movement[0]<0:
            rect.left = tile.right
            collision_types["left"]= True
    rect.y += movement[1]
    hit_list =collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types["top"] = True
    return rect, collision_types


moving_right = False
moving_left = False
player_y_momentum = 0
air_timer = 0

#player_location = [50,50]

player_rect = pygame.Rect(50,50,player_image.get_width(),player_image.get_height())
test_rect = pygame.Rect(100,100,100,50)

while True:
    display.fill((146,244,255))
    tile_rect = []
    y=0
    for row in game_map:
        x=0
        for tile in row:
            if tile == "1":
                display.blit(dirt_image, (x*TILE_SIZE, y*TILE_SIZE))
            if tile == "2":
                display.blit(grass_image, (x*TILE_SIZE, y*TILE_SIZE))
            if tile != "0":
                tile_rect.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1





    player_movement = [0,0]
    if moving_right:
        player_movement[0]+=2
    if moving_left:
        player_movement[0]-=2
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    if player_y_momentum > 3:
        player_y_momentum =3

    player_rect,collisions = move(player_rect,player_movement, tile_rect)
    if collisions["bottom"]:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer+=1

    display.blit(player_image, (player_rect.x,player_rect.y))


    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                if air_timer<6:
                    player_y_momentum=-5
        if event.type == KEYUP:

            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False



    surf = pygame.transform.scale(display, window_size)
    screen.blit(surf, (0,0))
    #screen.blit(player_image,(50,50))
    pygame.display.update()
    clock.tick(60)