import pygame
from player import Player

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Multiplayer Test")

hostPlayer = Player(15, 15, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
    
    pygame.time.Clock().tick(60)

    screen.fill((0, 0, 0))

    hostPlayer.move_player()
    hostPlayer.draw_player()
    pygame.display.flip()