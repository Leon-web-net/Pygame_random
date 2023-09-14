import pygame, sys, time, random

# C:\\Users\\letio\\OneDrive\\Desktop\\PycharmProjects\\12hr Part1\\Photos\\
pygame.init()
clock = pygame.time.Clock()

# screen
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Endless")
icon = pygame.image.load("Photos/moon.png")
pygame.display.set_icon(icon)

# text
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("Game", False, "Black")


# surface
ground_surface = pygame.image.load("Photos/ground.png").convert()
sky_surface = pygame.image.load("Photos/1.png").convert()
player_surf = pygame.image.load("Photos/Blue_SpriteMan_low.png").convert_alpha()
obstacle = pygame.image.load("Photos/poo.png").convert_alpha()


print(ground_surface.get_height())


platform = screen.get_height() - ground_surface.get_height() - player_surf.get_height()
C_platform = platform
x = 40

poosition = screen.get_height()-ground_surface.get_height()-obstacle.get_height()
obstacle_rect = obstacle.get_rect(topleft = (1000, poosition))

xMove = False
yMove = False
reach_top = 0
GoDown = 0
def ground_check():
    if C_platform>platform:
        return False
    else:
        return True

def key_check():
    pass



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ground_check():
                yMove = True
            elif event.key == pygame.K_RIGHT:
                xMove = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                xMove = False

    if yMove:
        platform -=  10
        if platform < C_platform-200:
            platform +=10
            reach_top = pygame.time.get_ticks()
            yMove = False

    GoDown = pygame.time.get_ticks()
    if xMove:
        x += 5

    if x > screen.get_width():
        x = 0
    if platform < C_platform and (GoDown - reach_top > 100):
        platform += 4
    elif platform > C_platform:
        platform = C_platform

    pygame.sprite.collide_rect(player_surf,obstacle)

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, screen.get_height()-ground_surface.get_height()))
    screen.blit(text_surface, (300, 50))
    screen.blit(obstacle,obstacle_rect)
    screen.blit(player_surf, (x, platform))

    time = test_font.render(f"Time {round(pygame.time.get_ticks() / 1000,2)}",
                            False, "Black")
    screen.blit(time,(0,0))
    player_rect = player_surf.get_rect(topleft=(x, platform))
    pygame.sprite.spritecollide(player_surf, obstacle)
    pygame.display.update()
    clock.tick(60)
