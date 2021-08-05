import pygame
import random
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# set title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background.jpg")

# Player
player_img = pygame.image.load("space-invaders.png")
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
enemy_x_change = 0.4
enemy_y_change = 45


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# game loop
run = True
while run:
    screen.fill((0, 0, 0))
    #background
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_x_change = 0

    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    enemy_x += enemy_x_change

    if enemy_x <= 0:
        enemy_x_change *= -1
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change *= -1
        enemy_y += enemy_y_change

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    pygame.display.update()
pygame.quit()
