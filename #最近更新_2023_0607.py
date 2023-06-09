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
    #初始化設定
    def __init__(self, image, position) :
        self.image = image
        self.position = position
    #移動設定
    def playermove(self, bg, jump, speed, right,  position, screen, keylist):
        speedtest = 2
        if len(keylist) == 2:
            if (keylist[0]=='right' and keylist[1]=='up') or \
                (keylist[1]=='right' and keylist[0]=='up'):
                speed[0] += speedtest 
                speed[1] -= speedtest+13
                screen.blit(bg, position, position)                      
                right[0] = 1
                jump[0] = 1                
            if(keylist[0]=='left' and keylist[1]=='up') or \
                (keylist[1]=='left' and keylist[0]=='up'):
                speed[0] -= speedtest
                speed[1] -= speedtest+13
                screen.blit(bg, position, position)
                right[0] = 0
                jump[0] = 1 
        if len(keylist) == 1:
            if keylist[0] == 'left':
                speed[0] -= speedtest
                screen.blit(bg, position, position)
                right[0] = 0 
                jump[0] = 0
            if keylist[0] == 'right':
                speed[0] += speedtest
                screen.blit(bg, position, position)
                right[0] = 1 
                jump[0] = 0
            if keylist[0] == 'up':
                speed[1] -= speedtest+13
                screen.blit(bg, position, position)
                jump[0] = 1      
    #重力
    def gravity(self, bg, gra, jump, position, screen):
        self.bg = bg
        self.gra = gra
        self.jump = jump
        self.position = position
        self.screen = screen
        screen.blit(bg, position, position)
        if jump[0] == 1:
            gra[1] = 0
        elif position[1] >= 500:
            gra[1] = 0
            position[1] = 500
        else:
            gra[1] += 1
        
#圖片下載
imm1 = pg.image.load\
    ('player1.png').convert_alpha()
imm2 = pg.image.load\
    ('player2.png').convert_alpha()
imm3 = pg.image.load\
    ('player3.png').convert_alpha()
imm4 = pg.image.load\
    ('player4.png').convert_alpha()
imm5 = pg.image.load\
    ('player1.png').convert()
imm6 = pg.image.load\
    ('player2.png').convert()
imm7 = pg.image.load\
    ('player3.png').convert()
imm8 = pg.image.load\
    ('player4.png').convert()
imm9 = pg.image.load\
    ('player6.png').convert()
imm10 = pg.image.load\
    ('player6.png').convert_alpha()
mybg = pg.image.load\
    ('google interland smart.png').convert()

#主角設定
immlist = [imm1, imm2, imm3, imm4, imm5, imm6, imm7, imm8, imm9, imm10]
immselect = 0 
immpos = immlist[immselect].get_rect()
immpos[1] = 500
imm = Player
imm.__init__(imm, immlist[immselect], immpos)
immright = [0]
immkeylist = []

#初始顯示設定
myscreen.blit(mybg, (0, 0))
myscreen.blit(immlist[immselect], immpos)

#forever loop
running = True
while running:
    #重力
    mygra = [0, 0]
    immjump = [0]
    imm.gravity(imm, mybg, mygra, immjump, immpos, myscreen)
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
            if event.key == pg.K_UP and not('up' in immkeylist):
                immkeylist.append('up')
            if event.key == pg.K_RIGHT and not('right' in immkeylist):
                immkeylist.append('right')
            if event.key == pg.K_LEFT and not('left' in immkeylist):
                immkeylist.append('left')
        #按鍵鬆開或串列過長
        if event.type == pg.KEYUP or len(immkeylist)>=3:
            if event.key == pg.K_UP and 'up' in immkeylist:
                immkeylist.remove('up')
            if event.key == pg.K_RIGHT and 'right' in immkeylist:
                immkeylist.remove('right')
            if event.key == pg.K_LEFT and 'left' in immkeylist:
                immkeylist.remove('left')
        #行走
        if event.type != pg.QUIT:
            print(immkeylist)
            immspeed = [0, 0]
            imm.playermove(imm, mybg, immjump, immspeed, immright, immpos, myscreen, immkeylist)
            immpos = immpos.move(immspeed)            
            immselect = int(immpos[0]/20) % 4
            if immjump[0] == 1:
                immselect = 8
            elif immright[0] == 0:
                immselect += 4
            if len(immkeylist) == 0:
                immselect = 9
            myscreen.blit(immlist[immselect], immpos)
    #更新視窗內容
    pg.display.flip()
    #重複偵測
    pg.key.set_repeat(10)