import pygame

pygame.init()

#create screen
screen = pygame.display.set_mode((800, 600))

#game loop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
