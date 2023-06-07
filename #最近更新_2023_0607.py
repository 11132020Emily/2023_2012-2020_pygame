#import與pygame初始化
import pygame as pg
import sys
pg.init()

#視窗設定
width, height = 1200, 600
myscreen = pg.display.set_mode((width, height))
pg.display.set_caption("Emily's_test")

#主角的class
class Player :
    def __init__(self, image, position) :
        self.image = image
        self.position = position

    def playermove(self, key, bg, isjump, speed, right, position, screen):
        self.key = key
        self.bg = bg
        self.isjump = isjump
        self.right = right
        self.position = position
        self.screen = screen
        self.speed = speed
        speedtest = 3
        if key == pg.K_UP : 
            speed[1] -= speedtest+13                     
            screen.blit(bg, position, position)
            isjump[0] = 1
        if not(key == pg.K_UP):
            isjump[0] = 0
        if key == pg.K_LEFT:
            speed[0] -= speedtest
            screen.blit(bg, position, position)
            right[0] = 0
            isjump[0] = 0
        if key == pg.K_RIGHT:
            speed[0] += speedtest                       
            screen.blit(bg, position, position)
            right[0] = 1
            isjump[0] = 0
            
    def gravity(self, bg, gra, isjump, position, screen):
        self.bg = bg
        self.gra = gra
        self.isjump = isjump
        self.position = position
        self.screen = screen
        screen.blit(bg, position, position)
        if isjump[0] == 1:
            gra[1] = 0
        elif position[1] >= 500:
            gra[1] += 1
            position[1] = 500
        else:
            gra[1] += 1
        
#圖片下載
imm1 = pg.image.load\
    ('C:\ASUS UX31E Driver\Emily\自主學習\player1.png').convert_alpha()
imm2 = pg.image.load\
    ('C:\ASUS UX31E Driver\Emily\自主學習\player2.png').convert_alpha()
imm3 = pg.image.load\
    ('C:\ASUS UX31E Driver\Emily\自主學習\player3.png').convert_alpha()
imm4 = pg.image.load\
    ('C:\ASUS UX31E Driver\Emily\自主學習\player4.png').convert_alpha()
imm5 = pg.image.load\
    ('C:\ASUS UX31E Driver\Emily\自主學習\player1.png').convert()
imm6 = pg.image.load\
    ('C:\ASUS UX31E Driver\Emily\自主學習\player2.png').convert()
imm7 = pg.image.load\
    ('C:\ASUS UX31E Driver\Emily\自主學習\player3.png').convert()
imm8 = pg.image.load\
    ('C:\ASUS UX31E Driver\Emily\自主學習\player4.png').convert()
imm9 = pg.image.load\
    ('C:\ASUS UX31E Driver\Emily\自主學習\player6.png').convert_alpha()
mybg = pg.image.load\
    ('C:\ASUS UX31E Driver\Emily\資訊\google interland kind.png').convert()

#主角設定
immlist = [imm1, imm2, imm3, imm4, imm5, imm6, imm7, imm8, imm9]
immselect = 0 
immpos = immlist[immselect].get_rect()
immpos[1] = 500
imm = Player
imm.__init__(imm, immlist[immselect], immpos)
immright = [0]

#初始顯示設定
myscreen.blit(mybg, (0, 0))
myscreen.blit(immlist[immselect], immpos)

#forever loop
running = True
while running:
    #重力
    mygra = [0, 0]
    immisjump = [0]
    imm.gravity(imm, mybg, mygra, immisjump, immpos, myscreen)
    immpos = immpos.move(mygra)
    myscreen.blit(immlist[immselect], immpos)
    for event in pg.event.get():
        #點按關閉按鈕
        if event.type == pg.QUIT:
            #停止使用pygame
            pg.quit()
            sys.exit()
        #偵測到有按鍵按下
        if event.type == pg.KEYDOWN:
            immspeed = [0, 0]
            imm.playermove(imm, event.key, mybg, immisjump, immspeed, immright, immpos, myscreen)
            immpos = immpos.move(immspeed)
            immselect = int(immpos[0]/30) % 4
            if immright[0] == 0:
                immselect += 4
            if immisjump[0] == 1:
                immselect = 8
            myscreen.blit(immlist[immselect], immpos)
            
    #更新視窗內容
    pg.display.flip()
    #重複偵測
    pg.key.set_repeat(10)