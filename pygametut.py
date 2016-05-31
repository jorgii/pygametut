import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Slither')

game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    game_display.fill(white)
    pygame.draw.rect(game_display, black, [400, 300, 10, 100])
    pygame.draw.rect(game_display, red, [400, 300, 10, 10])

    game_display.fill(red, rect=[200, 200, 50, 50])
    pygame.display.update()
pygame.quit()
quit()
