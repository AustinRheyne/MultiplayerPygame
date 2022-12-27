import pygame
import random
class Player:
    WIDTH = 50
    HEIGHT = 50
    SPEED = 2
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.screen = screen

    def move_player(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= Player.SPEED
        if keys[pygame.K_RIGHT]:
            self.x += Player.SPEED
        if keys[pygame.K_DOWN]:
            self.y += Player.SPEED
        if keys[pygame.K_UP]:
            self.y -= Player.SPEED

    def draw_player(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, Player.WIDTH, Player.HEIGHT))
        