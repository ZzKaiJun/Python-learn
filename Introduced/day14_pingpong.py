#乒乓球遊戲
#用pygame製作一個小遊戲

import pygame
from ball import Ball
from paddle import Paddle

def paddle_move(keys, paddle1, paddle2):
    if keys[pygame.K_w]:
        paddle1.update(True, WIN_HEIGHT)
    if keys[pygame.K_s]:
        paddle1.update(False, WIN_HEIGHT)
    if keys[pygame.K_UP]:
        paddle2.update(True, WIN_HEIGHT)
    if keys[pygame.K_DOWN]:
        paddle2.update(False, WIN_HEIGHT)


pygame.init()       #初始化


WIN_WIDTH = 700
WIN_HEIGHT = 500
FPS = 60

#創建遊戲視窗大小
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#設置視窗標題
win_title = "乒乓球"
pygame.display.set_caption(win_title)

paddle_width = 15
paddle_height = 100

ball = Ball(WIN_WIDTH/2,WIN_HEIGHT/2,10,(255,0,0))
paddle1 = Paddle(10, WIN_HEIGHT/2 - paddle_height/2,15,100,(0,0,0))        #座標點是球拍左上角，必須要經過調整
paddle2 = Paddle(WIN_WIDTH-10-paddle_width, WIN_HEIGHT/2- paddle_height/2,15,100,(0,0,0))


run = True
Game_clock = pygame.time.Clock()   #時鐘物件，限制while迴圈執行的速度


while run:
    Game_clock.tick(FPS)   #每一秒鐘最多30次
    #-----取得輸入
    for event in pygame.event.get():      #所有事件  ex:滑鼠移動  鍵盤按下
        if event.type == pygame.QUIT:     #如果按下x
            run = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         paddle1.y -= 4
        #     if event.key == pygame.K_DOWN:
        #         paddle1.y += 4

    keys = pygame.key.get_pressed()
    paddle_move(keys, paddle1, paddle2)

    # if keys[pygame.K_w]:
    #     if paddle1.y > 0:
    #         paddle1.y -= 5
    # if keys[pygame.K_s]:
    #     if paddle1.y + paddle_height < WIN_HEIGHT:
    #         paddle1.y += 5
    #
    # if keys[pygame.K_UP]:
    #     if paddle2.y > 0:
    #         paddle2.y -= 5
    # if keys[pygame.K_DOWN]:
    #     if paddle2.y + paddle_height < WIN_HEIGHT:
    #         paddle2.y += 5


    #-----遊戲更新
    # 在窗口中绘制游戏内容
    ball.update(WIN_WIDTH,WIN_HEIGHT)

    #-----畫面顯示
    window.fill("#ffcad4")
    ball.draw(window)
    paddle1.draw(window)
    paddle2.draw(window)
    # pygame.draw.rect(window, (0,0,0), (5,100,10,100))   #在window這視窗畫一個矩形  rect( 視窗, 顏色, 座標矩形大小 )
    # pygame.draw.circle(window, (0, 0, 0), (x,400),10)

    pygame.display.update()

pygame.quit()       #離開
























