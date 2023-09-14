import pygame, sys,time

xVelocity=1
yVelocity=1
pygame.init()
clock =pygame.time.Clock()
#Display surface

screen=pygame.display.set_mode((800,800))#main display
second_surface=pygame.Surface([100,200]) #height and width
second_surface.fill((0,255,255))

image =pygame.image.load("../Photos/Bleach_2.png")
image_rect=image.get_rect(topleft=[100,200])
print(image_rect.height,image_rect.width)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill((60, 99, 207))
    screen.blit(second_surface,(0,50))# placement (x,y)
    screen.blit(image,image_rect)
    if (screen.get_width()<=image_rect.right) or (0>=image_rect.left):
        xVelocity*=-1
        print("change_x")
    image_rect.right+=(xVelocity*5)
    if (screen.get_height()<=image_rect.centery+(image_rect.height/2)) or (0>=image_rect.centery-(image_rect.height/2)):
        yVelocity*=-1
        print("change_y")
    image_rect.centery+=(yVelocity*5)
    #print(image_rect.right,image_rect.left)
    pygame.display.flip() #updates window
    clock.tick(60) #fps
