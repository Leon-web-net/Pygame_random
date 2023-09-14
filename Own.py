import pygame, random, sys, time
from pygame.locals import *
from pygame import mixer
from tkinter import *
from tkinter import messagebox

def poison(health, shield, coins):
    if player_rect.centery > (display.get_height()*(2/3)):
        health -= 1
        coins+=20
        print(health)
    elif player_rect.centery > (display.get_height()/3):
        coins+=10
        if shield<=0:
            health -= 1
        else:
            shield-=1
        print(health)
    return health, shield, coins

def colour_checker(health, shield):

    for i in colour_dict:
        if i == bullet_colour:
            print(i)
            if shield <= 0:
                if i == "blue":
                    shield += colour_dict[i]
                else:
                    health += colour_dict[i]
                    if health > 100:
                        shield += health - 100
                        health = 100
            else:
                shield += colour_dict[i]
                if shield < 0:
                    health += shield
                    shield = 0

    if bullet_colour == "black":
        print(bullet_colour)
        health = 1
    elif bullet_colour == "green":
        print(bullet_colour)
        health += 50
        if health > 100:
            health = 100
    print(f"Health: {health}  Shield: {shield}")
    return health, shield

def click():
    if messagebox.askyesno(title="Please Stop",
                           message="Wanna LEAVE LOOOSER?"):
        pygame.quit()
        sys.exit()
    else:
        messagebox.showwarning(title="WARNING!",
                               message="Big Skill Issue!")

class Player(pygame.sprite.Sprite):
    def create_bullet(self):
        return Bullet(0, random.randrange(0, display.get_height()))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.colour = colour[random.randrange(0, len(colour))]
        self.image.fill(self.colour)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, tiles):
        global hit, bullet_colour
        self.rect.x += 2
        #collide = pygame.Rect.colliderect(self.rect,player.rect)
        collide_soldier = pygame.Rect.colliderect(self.rect, player_rect)
        if collide_soldier:
            self.kill()
            hit = True
            bullet_colour = self.colour
            return self.colour
        if self.rect.x > display.get_width()/4:
            for tile in tiles:
                if self.rect.colliderect(tile):
                    self.kill()
                    return
        if self.rect.x > display.get_width() or self.rect.x < -10:
            self.kill()



def load_map(path):
    f = open(path,"r")
    data = f.read()
    f.close()
    data = data.split("\n")
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {"top": False, "bottom": False, "right": False, "left": False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types["right"] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types["left"] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types["top"] = True
    return rect, collision_types

pygame.init()

timer = 0
mode = 1000
health = 100
shield = 0
mode_timer = 0
coins = 0

clock = pygame.time.Clock()
pygame.display.set_caption(("First Game :)"))
window_size = (1000, 800)

mixer.init()
mixer.music.load("Photos/Explanation.wav")
mixer.music.play(-1)

screen = pygame.display.set_mode(window_size, 0, 32)
display = pygame.Surface((600, 450))
font = pygame.font.Font(None, 20)
death_font = pygame.font.Font(None, 50)


health_bar = pygame.Surface((100, 10))
health_bar.fill("#02f771")
shield_bar = pygame.Surface((0, 10))
shield_bar.fill("#345eeb")



player_image = pygame.image.load("Photos/player.png").convert()
player_image.set_colorkey((255,255,255))
grass_image = pygame.image.load("Photos/grass.png")
TILE_SIZE = grass_image.get_width()
dirt_image = pygame.image.load("Photos/dirt.png")

game_map = load_map("PYGAME/First_Map.txt")

player = Player()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

colour =["orange", "yellow", "blue", "red"]
while len(colour) < 10:
    colour.append(colour[random.randrange(0, len(colour)-1)])
colour.append("black")
colour.append("green")
colour_dict = {"yellow": -5, "orange": -10, "red": -20, "blue": 5}
hit = False
moving_right = False
moving_left = False
player_y_momentum = 0
air_timer = 0
true_scroll = [0,0]

player_rect = pygame.Rect(20, 450-player_image.get_height(), player_image.get_width(), player_image.get_height())

#test_rect = pygame.Rect(100, 100, 100, 50)


while True:
    display.fill((146, 244, 255))

    if pygame.time.get_ticks() - timer > mode:
        bullet_group.add(player.create_bullet())
        timer = pygame.time.get_ticks()
        health, shield, coins = poison(health, shield, coins)
        health_bar = pygame.transform.scale(health_bar, (health, 10))
        shield_bar = pygame.transform.scale(shield_bar, (shield, 10))

        if (pygame.time.get_ticks()/1000)-mode_timer > 15:
            mode_timer += 15
            mode -= 25
            if mode < 100:
                mode = 100


    tile_rect = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == "1":
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE ))
            if tile == "2":
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile != "0":
                tile_rect.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    bullet_group.update(tile_rect)
    bullet_group.draw(display)

    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    if player_y_momentum > 3:
        player_y_momentum = 3

    player_rect, collisions = move(player_rect, player_movement, tile_rect)
    if collisions["bottom"]:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer += 1

    if collisions["top"]:
        player_y_momentum = 0
        air_timer = 0

    display.blit(player_image, (player_rect.x , player_rect.y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                if air_timer < 6:
                    player_y_momentum = -5
        if event.type == KEYUP:

            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False


    if hit:
        health, shield = colour_checker(health, shield)
        hit = False
        if health <= 0:
            window = Tk()

            button = Button(window,
                            command=click,
                            text="resume")
            button.pack()
            window.mainloop()
            while True:
                clock.tick(30)
                display.fill((0, 0, 0))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
        health_bar = pygame.transform.scale(health_bar, (health, 10))
        shield_bar = pygame.transform.scale(shield_bar, (shield, 10))
        if health <= 25:
            health_bar.fill("red")
        elif health <= 40:
            health_bar.fill("orange")
        else:
            health_bar.fill("#02f771")

        # if event.type == KEYDOWN:
        # if event.key == K_SPACE:
        # s_lock = True

    # if s_lock:
    # screen_lock()
    Shield_text = font.render(f"SHIELD:", False, "Black")
    Health_text = font.render(f"HEALTH:", False, "Black")
    Coin_text = font.render(f"COINS: {coins}",False,"yellow")
    display.blit(Health_text, (0, 0))
    display.blit(health_bar, (60, 2))
    display.blit(Shield_text, (0, 20))
    display.blit(shield_bar, (60, 20))
    display.blit(Coin_text, (200,0))
    surf = pygame.transform.scale(display, window_size)
    screen.blit(surf, (0, 0))
    # screen.blit(player_image,(50,50))
    pygame.display.update()
    #pygame.display.flip()
    clock.tick(80)