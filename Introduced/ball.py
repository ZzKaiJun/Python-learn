import pygame
import random
class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speedx = 2
        self.speedy = 2

        # random_list = [-4,-3,-2,-1,1,2,3,4]
        # self.speedx = random.choice(random_list)   #隨機選列表中的其中一個選項
        # self.speedy = random.choice(random_list)

    #畫圖
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x , self.y) , self.radius)

    #遊戲更新
    def update(self, width, height):
        self.x += self.speedx
        self.y += self.speedy

        ball_top = self.y - self.radius
        ball_bottom = self.y + self.radius
        ball_right = self.x + self.radius
        ball_left = self.x - self.radius
        if ball_top < 0 or ball_bottom > height:
            self.speedy *= -1
        if ball_right > width or ball_left < 0:
            self.speedx *= -1





