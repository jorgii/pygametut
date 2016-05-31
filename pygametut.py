import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Slither')

game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
pygame.quit()
quit()
