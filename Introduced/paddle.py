import pygame

class Paddle():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speedy = 5

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def update(self, up, HEIGHT):
        if up:
            if self.y > 0:
                self.y -= self.speedy
        else:
            if self.y + self.height < HEIGHT:
                self.y += self.speedy







