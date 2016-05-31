import pygame

pygame.init()

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Slither')
pygame.display.update()

game_exit = False

while not game_exit:
    for event in pygame.event.get():
        print(event)

pygam.quit()
quit()
