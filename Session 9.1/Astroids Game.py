import sys, pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
spaceship = pygame.image.load("spaceship.png")
spaceship = pygame.transform.scale(spaceship, (50, 50))
pos = [200,200]
incr = [0,0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                incr[0] = -1
            elif event.key == pygame.K_RIGHT:
                incr[0] = 1
            elif event.key == pygame.K_UP:
                incr[1] = -1
            elif event.key == pygame.K_DOWN:
                incr[1] = 1
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                incr[0] = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                incr[1] = 0

    pos[0] = pos[0] + incr[0]
    pos[1] = pos[1] + incr[1]

    if pos[0] < 0:
        pos[0] = 500 - 50
    elif pos[0] > 500 - 50:
        pos[0] = 0

    if pos[1] < 0:
        pos[1] = 500 - 50
    elif pos[1] > 500 - 50:
        pos[1] = 0

    screen.fill((0,0,0))
    screen.blit(spaceship,pos)
    pygame.display.update()
