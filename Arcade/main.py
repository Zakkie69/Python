import pygame
pygame.init()

win = pygame.display.set_mode((500 , 500))   # scherm aanmaken
pygame.display.set_caption("Sudoko Solver")

x = 50
y = 50
width = 40
heigth = 60
vel = 5

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():    # programma loopt tot op kruisje wordt geduwt
        if event.type == pygame.QUIT:
            run = False


    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, heigth))
    pygame.display.update()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

pygame.quit()
