import pygame
import random

a=random.randint(50,750)
class Enemy(pygame.sprite.Sprite):

    def __init__(self, w, h):
        super().__init__()
        self.h, self.w = h, w
        self.image = pygame.image.load(f'image/star.png')
        self.image = pygame.transform.rotozoom(self.image, 1, 0.1)
        self.rect = self.image.get_rect()
        a = random.randint(50, 750)
        self.rect.centerx = w - a
        self.rect.centery = h - 700
        self.speed = 3

    def update(self):
        self.move()
        if self.rect.bottom > self.h:
            self.kill()
    def move(self):
        self.rect.y += self.speed
