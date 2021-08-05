import pygame
import random
import math

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
enemy_x_change = []
enemy_y_change = []
num_of_enemy = 4
enemy_x = []
enemy_y = []

for i in range(num_of_enemy):
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(0.4)
    enemy_y_change.append(45)

# Bullet
bullet_img = pygame.image.load("bullet.png")
bullet_x = player_x
bullet_y = 480
bullet_y_change = 0.7
bullet_state = "ready"

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 30)

score_x = 10
score_y = 10


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def bullet(x, y):
    screen.blit(bullet_img, (x, y))


def isCollision(bullet_x, bullet_y, enemy_x, enemy_y):
    distance = math.sqrt(math.pow(bullet_x - enemy_x, 2) +
                         math.pow(bullet_y - enemy_y, 2))
    return distance < 32


def show_score():
    score_text = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (score_x, score_y))


# game loop
run = True
while run:
    screen.fill((0, 0, 0))
    # background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                bullet_state = "fire"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_x_change = 0

    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    for i in range(num_of_enemy):

        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] <= 0:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]

        if isCollision(bullet_x, bullet_y, enemy_x[i], enemy_y[i]):
            bullet_state = "ready"
            bullet_y = 480
            score += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i])

    if bullet_state == "fire":
        bullet(bullet_x + 15, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= -35:
        bullet_state = "ready"
        bullet_y = 480
        bullet_x = player_x

    player(player_x, player_y)
    show_score()
    pygame.display.update()

pygame.quit()
