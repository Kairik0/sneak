import pygame
import random


WSive = (720, 480)

screen = (pygame.display.set_mode(WSive))

TSide = 30
MSize = WSive[0] // 2, WSive[1] // TSide

start_pos = MSize[0] //2, MSize[1] //2
snake = [start_pos]
alive = True

direction = 0
directions =[(1, 0),(0, 1),(-1, 0), (0, -1)]

apple = random.randint(0, MSize[0]), random.randint(0, MSize[1])


FPS = 6
clock = pygame.time.Clock()


run = True
while run:
    clock.tick(FPS)
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                direction = 0
            if event.key == pygame.K_s:
                direction = 1
            if event.key == pygame.K_a:
                direction = 2
            if event.key == pygame.K_w:
                direction = 3


    [pygame.draw.rect(screen, "green", (x * TSide, y * TSide, TSide -1, TSide - 1)) for x, y in snake]
    [pygame.draw.rect(screen, "green", (apple[0] * TSide, apple[1] * TSide, TSide -1, TSide - 1)) for x, y in snake]

    if alive:
        new_pos = snake [0][0] + directions[direction][0], snake[0][1] + directions[direction][1]

        snake.insert(0, new_pos)
        snake.pop(-1)

    pygame.display.flip()
