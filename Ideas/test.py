import pygame

SCALE = 1
WIDTH = 1280 * SCALE
HEIGHT = 720 * SCALE
color_dark = (100,100,100)
pressed = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((30, 30, 30))
mouse = pygame.mouse.get_pos()

while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            pressed = False
        if event.type == pygame.QUIT:
            pygame.quit()

        if pressed == True:
            pygame.draw.rect(screen,color_dark,[mouse[0],mouse[1],10,10])
    pygame.display.update()

    