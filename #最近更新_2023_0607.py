#import與pygame初始化
import pygame as pg
import random
import sys
import time
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
    def playermove(self, bg, jump, speed, right, jumplimit, position, screen, keylist, jr):
        #跳板 = [上y, 下y, 下反射範圍, 左x, 右x]
        B = [370, 440, 480, 600, 700]
        CL = [290, 375, 410, -100, 605] 
        CR = [290, 375, 410, 750, 1200]
        C = [132, 200, 240, 220, 880]
        TL = [10, 90, 130, 100, 230]
        TR = [10, 90, 130, 890, 1020]
        speedtest = 2
        if len(keylist) == 2:
            if (keylist[0]=='right' and keylist[1]=='up') or \
                (keylist[1]=='right' and keylist[0]=='up'):
                speed[0] += speedtest 
                speed[1] -= speedtest+13
                screen.blit(bg, position, position)                      
                right[0] = 1
                jump[0] = 1  
                jumplimit[0] -= 15         
            if(keylist[0]=='left' and keylist[1]=='up') or \
                (keylist[1]=='left' and keylist[0]=='up'):
                speed[0] -= speedtest
                speed[1] -= speedtest+13
                screen.blit(bg, position, position)
                right[0] = 0
                jump[0] = 1
                jumplimit[0] -= 15
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
                jumplimit[0] -= 15
        #跳板們 
        if position[1]>=B[0] and position[1]<=B[0]+13 and position[0]>=B[3] and position[0]<=B[4]:
            jump[0] = 0 
        if position[1]>B[0]+13 and position[1]<B[1] and position[0]>=B[3] and position[0]<=B[4]:
            speed[0] = 0
            jump[0] = 0
        if position[1]>=B[1] and position[1]<=B[2] and position[0]>=B[3] and position[0]<=B[4]:
            if speed[1] < 0:
                speed[1] *= -1
            jump[0] = 0 

        if position[1]>=CL[0] and position[1]<=CL[0]+13 and position[0]>=CL[3] and position[0]<=CL[4]:
            jump[0] = 0 
        if position[1]>CL[0]+13 and position[1]<CL[1] and position[0]>=CL[3] and position[0]<=CL[4]:
            speed[0] = 0
            jump[0] = 0
        if position[1]>=CL[1] and position[1]<=CL[2] and position[0]>=CL[3] and position[0]<=CL[4]:
            if speed[1] < 0:
                speed[1] *= -1
            jump[0] = 0 

        if position[1]>=CR[0] and position[1]<=CR[0]+13 and position[0]>=CR[3] and position[0]<=CR[4]:
            jump[0] = 0 
        if position[1]>CR[0]+13 and position[1]<CR[1] and position[0]>=CR[3] and position[0]<=CR[4]:
            speed[0] = 0
            jump[0] = 0
        if position[1]>=CR[1] and position[1]<=CR[2] and position[0]>=CR[3] and position[0]<=CR[4]:
            if speed[1] < 0:
                speed[1] *= -1
            jump[0] = 0 
        
        if position[1]>=C[0] and position[1]<=C[0]+13 and position[0]>=C[3] and position[0]<=C[4]:
            jump[0] = 0 
        if position[1]>C[0]+13 and position[1]<C[1] and position[0]>=C[3] and position[0]<=C[4]:
            speed[0] = 0
            jump[0] = 0
        if position[1]>=C[1] and position[1]<=C[2] and position[0]>=C[3] and position[0]<=C[4]:
            if speed[1] < 0:
                speed[1] *= -1
            jump[0] = 0 

        if position[1]>=TL[0] and position[1]<=TL[0]+13 and position[0]>=TL[3] and position[0]<=TL[4]:
            jump[0] = 0 
        if position[1]>TL[0]+13 and position[1]<TL[1] and position[0]>=TL[3] and position[0]<=TL[4]:
            speed[0] = 0
            jump[0] = 0
        if position[1]>=TL[1] and position[1]<=TL[2] and position[0]>=TL[3] and position[0]<=TL[4]:
            if speed[1] < 0:
                speed[1] *= -1
            jump[0] = 0 

        if position[1]>=TR[0] and position[1]<=TR[0]+13 and position[0]>=TR[3] and position[0]<=TR[4]:
            jump[0] = 0 
        if position[1]>TR[0]+13 and position[1]<TR[1] and position[0]>=TR[3] and position[0]<=TR[4]:
            speed[0] = 0
            jump[0] = 0
        if position[1]>=TR[1] and position[1]<=TR[2] and position[0]>=TR[3] and position[0]<=TR[4]:
            if speed[1] < 0:
                speed[1] *= -1
            jump[0] = 0 

        #垂直邊界
        if position[0]<=CL[4] and position[1]>=CL[2]-30 and not('right' in keylist):
            speed[0] = 0
        #水平上界
        if position[1]<=0:
            jump[0] = 0
            speed[1] = 0
        #被看到
        if position[1]>=CL[2]-10 and policeLBright == [1] and speed!=[0, 0]:
            jr[0] = 2
    #重力
    def gravity(self, bg, gra, jump, position, screen):
        B = [370, 440, 480, 600, 700]
        CL = [290, 375, 410, -100, 605] 
        CR = [290, 375, 410, 750, 1200]
        C = [132, 200, 240, 220, 880]
        TL = [10, 90, 130, 100, 230]
        TR = [10, 90, 130, 890, 1020]
        screen.blit(bg, position, position)
        if jump[0] == 1:
            gra[1] = 0
        #跳板們
        elif position[1]>=B[0] and position[1]<=B[0]+13 and position[0]>=B[3] and position[0]<=B[4]:
            gra[1] = 0
        elif position[1]>=CL[0] and position[1]<=CL[0]+13 and position[0]>=CL[3] and position[0]<=CL[4]:
            gra[1] = 0
        elif position[1]>=CR[0] and position[1]<=CR[0]+13 and position[0]>=CR[3] and position[0]<=CR[4]:
            gra[1] = 0 
        elif position[1]>=C[0] and position[1]<=C[0]+13 and position[0]>=C[3] and position[0]<=C[4]:
            gra[1] = 0
        elif position[1]>=TL[0] and position[1]<=TL[0]+13 and position[0]>=TL[3] and position[0]<=TL[4]:
            gra[1] = 0
        elif position[1]>=TR[0] and position[1]<=TR[0]+13 and position[0]>=TR[3] and position[0]<=TR[4]:
            gra[1] = 0 
        elif position[1] >= 500:
            gra[1] = 0
            position[1] = 500
        else:
            gra[1] += 1

#獄警的class
class Police:
    #初始化設定
    def __init__(self, image, position) :
        self.image = image
        self.position = position
    #自動行走
    def automove(self, bg, right, speed, position, screen, lineR, lineL):
        if right[0] == 1:
            speed[0] += 1
            screen.blit(bg, position, position) 
        elif right[0] == 0:
            speed[0] -= 1
            screen.blit(bg, position, position)
        if position[0] >= lineR and right[0] == 1:
            right[0] = 0
        elif position[0] <= lineL and right[0] == 0:                
            right[0] = 1  

#士兵的class
class Soldier:
    #初始化設定
    def __init__(self, image, position) :
        self.image = image
        self.position = position
    #隨機飛出
    def ran_fly(self, bg, position, screen):  
        screen.blit(bg, position, position)
        position[0] -= 4  
        
#圖片下載
imm1 = pg.image.load('player_right1.png').convert_alpha()
imm2 = pg.image.load('player_right2.png').convert_alpha()
imm3 = pg.image.load('player_right3.png').convert_alpha()
imm4 = pg.image.load('player_right4.png').convert_alpha()
imm5 = pg.image.load('player_left1.png').convert_alpha()
imm6 = pg.image.load('player_left2.png').convert_alpha()
imm7 = pg.image.load('player_left3.png').convert_alpha()
imm8 = pg.image.load('player_left4.png').convert_alpha()
imm9 = pg.image.load('player_right_jump.png').convert_alpha()
imm10 = pg.image.load('player_right_front.png').convert_alpha()
imm11 = pg.image.load('player_left_jump.png').convert_alpha()
imm12 = pg.image.load('player_left_front.png').convert_alpha()
mybg = pg.image.load('mybg_temp5.jpg').convert()
police1 = pg.image.load('police_right1.png').convert_alpha()
police2 = pg.image.load('police_right2.png').convert_alpha()
police3 = pg.image.load('police_right3.png').convert_alpha()
police4 = pg.image.load('police_right4.png').convert_alpha()
police5 = pg.image.load('police_left1.png').convert_alpha()
police6 = pg.image.load('police_left2.png').convert_alpha()
police7 = pg.image.load('police_left3.png').convert_alpha()
police8 = pg.image.load('police_left4.png').convert_alpha()
soldier1 = pg.image.load('soldier1.png').convert_alpha()
soldier2 = pg.image.load('soldier2.png').convert_alpha()
soldier3 = pg.image.load('soldier3.png').convert_alpha()
soldier4 = pg.image.load('soldier4.png').convert_alpha()
soldier5 = pg.image.load('soldier5.png').convert_alpha()
policerun0 = pg.image.load('police_right_front.png').convert()
soldierrun0 = pg.image.load('soldier2.png').convert()
win = pg.image.load('win.jpg').convert()

#主角設定
immlist = [imm1, imm2, imm3, imm4, imm5, imm6, imm7, imm8, imm9, imm10, imm11, imm12]
immselect = 0 
immpos = immlist[immselect].get_rect()
immpos[0] = 1100
immpos[1] = 500
imm = Player
imm.__init__(imm, immlist[immselect], immpos)
immright = [0]
immkeylist = []
immjumplimit1 = [540]
immjumplimit2 = [540]

#獄警設定
policelist = [police1, police2, police3, police4, police5, police6, police7, police8]
policedelaycount = 0
policeLBselect = 0
policeLBpos = policelist[policeLBselect].get_rect()
policeLBpos[0] = 0
policeLBpos[1] = 410
mypoliceLB = Police
mypoliceLB.__init__(mypoliceLB, policelist[policeLBselect], policeLBpos)
policeLBright = [1]
policeLBlineR = 480
policeLBlineL = 0

#士兵共用設定
soldierlist = [soldier1, soldier2, soldier3, soldier4, soldier5]
soldierdelaycount = 0
#士兵個別設定
soldierSTselect = 0
soldierSTpos = soldierlist[soldierSTselect].get_rect()
soldierSTpos[0] = 1200
soldierSTpos[1] = 290
mysoldierST = Soldier
mysoldierST.__init__(mysoldierST, soldierlist[soldierSTselect], soldierSTpos)

soldierNDselect = 0
soldierNDpos = soldierlist[soldierNDselect].get_rect()
soldierNDpos[0] = 1620
soldierNDpos[1] = 130
mysoldierND = Soldier
mysoldierND.__init__(mysoldierND, soldierlist[soldierNDselect], soldierNDpos)

soldierRDselect = 0
soldierRDpos = soldierlist[soldierRDselect].get_rect()
soldierRDpos[0] = 2040
soldierRDpos[1] = 70
mysoldierRD = Soldier
mysoldierRD.__init__(mysoldierRD, soldierlist[soldierRDselect], soldierRDpos)

#forever loop
jr = [0]
rr = [0]
running = -1 
okay2 = 0
gamepoint = 0
count = 0
start = 0
while running == -1:
    myscreen.fill((250, 220, 90))
    f = pg.font.SysFont('impact', 150)
    text = f.render("Loading...Start!",True,(255,255,255))
    textRect = text.get_rect()
    textRect.center = (600, 300)
    f1 = pg.font.SysFont('impact', 25)
    presstext = f1.render("press enter to continue",True,(255,255,255))
    presstextRect = presstext.get_rect()
    presstextRect.center = (600, 500)
    f2 = pg.font.SysFont('impact', 26)
    pouttext = f2.render("press enter to continue",True,(200, 160, 30))
    pouttextRect = pouttext.get_rect()
    pouttextRect.center = (600, 500)
    myscreen.blit(pouttext, pouttextRect)
    myscreen.blit(presstext, presstextRect)
    myscreen.blit(text, textRect)
    for event in pg.event.get():
        #點按關閉按鈕
        if event.type == pg.QUIT:
            #停止使用pygame
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                running = 0
    pg.display.flip()
    pg.key.set_repeat(10)

while running == 0:
    myscreen.fill((30, 50, 70))
    f = pg.font.SysFont('microsoftjhengheiui', 30)
    f1 = pg.font.SysFont('microsoftjhengheiui', 25)
    maintext = f.render("※溫馨提醒：",True,(255,255,255))
    text1 = f1.render("如果你會手抖 請不要玩這款遊戲",True,(255,255,255))
    text2 = f1.render("初次製作 有瑕疵下次一定改進（有下次的話）",True,(255,255,255))
    main1text = f.render("※遊玩方法：",True,(255,255,255))
    text3 = f1.render("按up鍵往上跳 按left鍵往左走 按right鍵往右走",True,(255,255,255))
    text4 = f1.render("主角會腿痠跳不起來 若跳不高請長按up鍵直到掉落到底 即可讓主角適應跳躍",True,(255,255,255))
    text5 = f1.render("主角跳起需要時間準備 請將其準備時間差納入跳躍考量",True,(255,255,255))
    text6 = f1.render("本遊戲分為兩關：",True,(255,255,255))
    text7 = f1.render("第一關請躲避「守衛」的視線（停止移動） 運用場景中的物件當作跳板 逃出監獄",True,(255,255,255))
    text8 = f1.render("第二關請躲避「士兵」的攻擊 運用場景中的物件當作跳板 在上層穿梭",True,(255,255,255))
    text9 = f1.render("請注意：",True,(255,255,255))
    text10 = f1.render("逃出監獄後 監獄出口會關閉 不用擔心主角再次落入監獄",True,(255,255,255))
    text11 = f1.render("進入上層後 士兵不會馬上出現",True,(255,255,255))
    text12 = f1.render("須在上層正中間的跳板停留一段時間 士兵才會出發",True,(255,255,255))
    text13 = f1.render("士兵出發前 強烈建議在跳板上讓主角適應跳躍 避免遊戲尚未開始主角即疲乏",True,(255,255,255))
    text14 = f1.render("士兵和守衛的速度不固定 請小心（沒錯這是瑕疵 求大神給解）",True,(255,255,255))
    main2text = f.render("躲過一定數量的士兵即可通關（幾隻？才不告訴逆雷~）",True,(255,255,255))
    main3text = f.render("按下down鍵即開始遊戲啦 遊戲愉快~~",True,(255,255,255))
    text15 = f1.render("守衛",True,(255,255,255))
    text16 = f1.render("士兵",True,(255,255,255))
    myscreen.blit(maintext, (50, 0))
    myscreen.blit(text1, (80, 35))
    myscreen.blit(text2, (80, 60))
    myscreen.blit(main1text, (50, 95))
    myscreen.blit(text3, (80, 130))
    myscreen.blit(text4, (80, 160))
    myscreen.blit(text5, (80, 190))
    myscreen.blit(text6, (80, 230))
    myscreen.blit(text7, (110, 260))
    myscreen.blit(text8, (110, 290))
    myscreen.blit(text9, (80, 320))
    myscreen.blit(text10, (110, 350))
    myscreen.blit(text11, (110, 380))
    myscreen.blit(text12, (110, 410))
    myscreen.blit(text13, (110, 440))
    myscreen.blit(text14, (110, 470))
    myscreen.blit(main2text, (50, 510))
    myscreen.blit(main3text, (50, 550))
    myscreen.blit(policerun0, (1050, 10))
    myscreen.blit(soldierrun0, (1050, 200))
    myscreen.blit(text15, (1000, 10))
    myscreen.blit(text16, (1000, 200))
    for event in pg.event.get():
        #點按關閉按鈕
        if event.type == pg.QUIT:
            #停止使用pygame
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                running = 1
    pg.display.flip()
    pg.key.set_repeat(10)

while running==1:
    #初始顯示設定
    if start == 0:
        myscreen.blit(mybg, (0, 0))
        myscreen.blit(immlist[immselect], immpos)
        myscreen.blit(policelist[policeLBselect], policeLBpos)
        myscreen.blit(soldierlist[soldierSTselect], soldierSTpos)
        myscreen.blit(soldierlist[soldierNDselect], soldierNDpos)
        myscreen.blit(soldierlist[soldierRDselect], soldierRDpos) 
        start = 1 
    #重力
    mygra = [0, 0]
    immjump = [0]
    imm.gravity(imm, mybg, mygra, immjump, immpos, myscreen)
    immpos = immpos.move(mygra)
    myscreen.blit(immlist[immselect], immpos)
    #獄警行走
    if policedelaycount==0:
        policeLBspeed = [0, 0]
        mypoliceLB.automove \
            (mypoliceLB, mybg, policeLBright, policeLBspeed, policeLBpos, myscreen, policeLBlineR, policeLBlineL) 
        policeLBpos = policeLBpos.move(policeLBspeed)
        policeLBselect = int(policeLBpos[0]/20) % 4
        if policeLBright[0] == 0:
            policeLBselect += 4
        myscreen.blit(policelist[policeLBselect], policeLBpos)
    #士兵飛行
    if soldierdelaycount==0 and okay2==1:
        if soldierSTpos[0]<=-120:
            rr[0] = random.randrange(0, 290, 10)
            soldierSTpos[1] = rr[0]
            soldierSTpos[0] = 1200
        mysoldierST.ran_fly(mysoldierST, mybg, soldierSTpos, myscreen)
        soldierSTselect = int(soldierSTpos[0]/20) % 5
        myscreen.blit(soldierlist[soldierSTselect], soldierSTpos)
        if soldierNDpos[0]<=-120:
            rr[0] = random.randrange(0, 290, 10)
            soldierNDpos[1] = rr[0]
            soldierNDpos[0] = 1640
        mysoldierND.ran_fly(mysoldierND, mybg, soldierNDpos, myscreen)
        soldierNDselect = int(soldierNDpos[0]/20) % 5
        myscreen.blit(soldierlist[soldierNDselect], soldierNDpos)
        if soldierRDpos[0]<=-120:
            rr[0] = random.randrange(0, 290, 10)
            soldierRDpos[1] = rr[0]
            soldierRDpos[0] = 2080
        mysoldierRD.ran_fly(mysoldierRD, mybg, soldierRDpos, myscreen)
        soldierRDselect = int(soldierRDpos[0]/20) % 5
        myscreen.blit(soldierlist[soldierRDselect], soldierRDpos)

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
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                running = 1
        
        if event.type != pg.QUIT:
            #主角行走
            immspeed = [0, 0]
            if immjumplimit1[0] > 0:
                imm.playermove \
                    (imm, mybg, immjump, immspeed, immright, immjumplimit1, immpos, myscreen, immkeylist, jr)
            elif immjumplimit2[0] > 0:
                imm.playermove \
                    (imm, mybg, immjump, immspeed, immright, immjumplimit2, immpos, myscreen, immkeylist, jr)
            #跳躍高度
            if immspeed[1]<=0:
                if immjumplimit1[0]<=0 and immjumplimit2[0]<=0:
                    immspeed[1] = 0
                    immjumplimit1[0] = 540
                    immjumplimit2[0] = 540
                elif immjumplimit1[0]<=0 or immjumplimit2[0]<=0:
                    immspeed[1] = 0 
            immpos = immpos.move(immspeed)
            #最外邊界過不去
            if immpos[0] >= 1130 and not('left' in immkeylist):
                immpos[0] = 1130
            if immpos[0] <= -5 and not('right' in immkeylist):
                immpos[0] = -5        

            immselect = int(immpos[0]/20) % 4
            if immright[0] == 0:
                immselect += 4
            if immjump[0] == 1:
                if immright[0] == 0:
                    immselect = 10
                else:
                    immselect = 8
            if len(immkeylist) == 0:
                if immright[0] == 0:
                    immselect = 11
                else:
                    immselect = 9
            myscreen.blit(immlist[immselect], immpos)

    if policedelaycount <2.5:
        policedelaycount += 0.5
    else:
        policedelaycount -= 2.5

    if soldierdelaycount <5.5:
        soldierdelaycount += 0.5
    else:
        soldierdelaycount -= 5.5
    #被撞到
    if abs(immpos.center[1]-soldierSTpos.center[1])<=66 and abs(immpos[0]-soldierSTpos[0])<=66:
        jr[0] = 2        
    if abs(immpos.center[1]-soldierNDpos.center[1])<=66 and abs(immpos[0]-soldierNDpos[0])<=66:
        jr[0] = 2
    if abs(immpos.center[1]-soldierRDpos.center[1])<=66 and abs(immpos[0]-soldierRDpos[0])<=66:
        jr[0] = 2

    #切換場景
    if jr[0] == 2:
        running = 2
    if immpos[1] <= 132:
        count += 0.1
    if immpos[1]<=132 and count>=500:
        okay2 = 1
    if immpos[1] >= 290 and okay2 == 1:
        immpos[1] = 290
    if soldierSTpos[0]==0 or soldierNDpos[0]==0 or soldierRDpos[0]==0:
        gamepoint += 1
    if gamepoint >= 90:
        running = 3 
    pg.display.flip()
    #重複偵測
    pg.key.set_repeat(10)

while running == 2:
    myscreen.fill((20, 90, 90))
    f = pg.font.SysFont('impact', 50)
    text = f.render("died",True,(20,90,50),(255,255,255))
    textRect = text.get_rect()
    textRect.center = (600, 300)
    myscreen.blit(text, textRect)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            #停止使用pygame
            pg.quit()
            sys.exit()
    pg.display.flip()
    pg.key.set_repeat(10)
while running == 3:
    myscreen.blit(win, (0, 0))
    for event in pg.event.get():
        #點按關閉按鈕
        if event.type == pg.QUIT:
            #停止使用pygame
            pg.quit()
            sys.exit()
    pg.display.flip()
    pg.key.set_repeat(10)