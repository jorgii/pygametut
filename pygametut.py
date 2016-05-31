import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

game_exit = False

lead_x = display_width/2
lead_y = display_height/2
lead_x_change = 0
lead_y_change = 0

block_size = 10
block_change = 2
FPS = 100

clock = pygame.time.Clock()

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_change
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_change
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_change
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_change
                lead_x_change = 0

    if lead_x > (display_width - block_size) or \
            lead_x < 0 or \
            lead_y > (display_height - block_size) or \
            lead_y < 0:
        game_exit = True

    lead_x += lead_x_change
    lead_y += lead_y_change

    game_display.fill(white)
    pygame.draw.rect(
        game_display,
        black,
        [lead_x, lead_y, block_size, block_size])

    pygame.display.update()

    clock.tick(FPS)
pygame.quit()
quit()
