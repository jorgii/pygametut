import pygame
import time
import random


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

img = pygame.image.load('snake_head.png')
block_size = 20
block_change = 10
FPS = 30
direction = 'right'

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)


def snake(block_size, snake_list):
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)
    game_display.blit(head, (snake_list[-1][0], snake_list[-1][1]))
    for block in snake_list[:-1]:
        pygame.draw.rect(
            game_display,
            black,
            [block[0], block[1], block_size, block_size])


def text_objects(text, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, y_displace=0):
    text_surface, text_rect = text_objects(msg, color)
    text_rect.center = (display_width/2), (display_height/2) + y_displace
    game_display.blit(text_surface, text_rect)


def game_loop():
    global direction
    game_exit = False
    game_over = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0
    snake_list = []
    snake_length = 1
    rand_apple_x = round(random.randrange(
        0,
        display_width - block_size)/block_size)*block_size
    rand_apple_y = round(random.randrange(
        0,
        display_height - block_size)/block_size)*block_size

    while not game_exit:
        while game_over is True:
            game_display.fill(white)
            message_to_screen("Game over", red, -50)
            message_to_screen("Press C to play again or Q to quit", black, 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_change
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_change
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_change
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_change
                    lead_x_change = 0

        if lead_x > (display_width - block_size) or \
                lead_x < 0 or \
                lead_y > (display_height - block_size) or \
                lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(white)
        apple_thickness = 30
        pygame.draw.rect(
            game_display,
            green,
            [rand_apple_x, rand_apple_y, apple_thickness, apple_thickness])
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True
        snake(block_size, snake_list)
        pygame.display.update()

        if lead_x > rand_apple_x and lead_x < rand_apple_x + apple_thickness \
                or lead_x + block_size > rand_apple_x and \
                lead_x + block_size < rand_apple_x + apple_thickness:
            if lead_y > rand_apple_y and \
                    lead_y < rand_apple_y + apple_thickness or \
                    lead_y + block_size > rand_apple_y and \
                    lead_y + block_size < rand_apple_y + apple_thickness:
                rand_apple_x = round(random.randrange(
                    0,
                    display_width - block_size)/block_size)*block_size
                rand_apple_y = round(random.randrange(
                    0,
                    display_height - block_size)/block_size)*block_size
                snake_length += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

game_loop()
