import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Slither')

game_exit = False

lead_x = 300
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock()

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -2
            if event.key == pygame.K_RIGHT:
                lead_x_change = 2
    lead_x += lead_x_change

    game_display.fill(white)
    pygame.draw.rect(game_display, black, [lead_x, lead_y, 10, 10])

    pygame.display.update()

    clock.tick(100)
pygame.quit()
quit()
