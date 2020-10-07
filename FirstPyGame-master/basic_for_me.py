import pygame
pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First GAme")

walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'),
             pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'),
             pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'),
            pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'),
            pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

clock = pygame.time.Clock()

#punkty startowe postaci
x = 50
y = 400
#wymiary postaci
width = 64
height = 64
vel = 5

left = False
right = False
walk_count = 0

is_jump = False
jump_count = 10

def redrawGameWindow():
    global  walk_count

    #CZysci ekran
    #win.fill((0,0,0))

    #tlo
    win.blit(bg, (0,0))

    #implementacja postaci
    #pygame.draw.rect(win,(255,0,0), (x,y,width,height))


    if walk_count +1 >= 27:
        walk_count = 0

    if left:
        win.blit(walkLeft[walk_count//3], (x,y))
        walk_count += 1
    elif right:
        win.blit(walkRight[walk_count//3], (x,y))
        walk_count += 1
    else:
        win.blit(char, (x,y))

    pygame.display.update()

#mainloop
run = True
while run:
    #szybkosc gry
    #pygame.time.delay(30)
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        left =  False
        right = True
    else:
        right = False
        left = False
        walk_count = 0
    if not(is_jump):
        #ruszanie do gory i do dolu
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < 500 - height - vel:
        #     y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_count = 0
    else:
        if jump_count >= - 10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    redrawGameWindow()

pygame.quit()


