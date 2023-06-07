#最近更新
import pygame as pg

#pygame初始化
pg.init()

#設定視窗的寬&高
width, height = 1000, 800
screen = pg.display.set_mode((width, height))

#設定視窗標題
pg.display.set_caption("Emily's_test")
#image.load('圖片路徑')
imm = pg.image.load('player1.png')
#視窗變數.blit(圖像, 繪製位置)
screen.blit(imm, (0, 0))

running = True
while running:
    for event in pg.event.get():
        #若點按關閉按鈕
        if event.type == pg.QUIT:
            #停止使用pygame
            pg.quit()
    #更新視窗內容
    pg.display.flip()