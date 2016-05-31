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

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x += 10
    game_display.fill(white)
    pygame.draw.rect(game_display, black, [lead_x, lead_y, 10, 100])

    pygame.display.update()
pygame.quit()
quit()
