from re import A
import pygame as pg
import sys
import random
import time


class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)      # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.bgi_sfc = pg.image.load(image)     # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()  # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self,image:str,size:float,xy):
        self.sfc = pg.image.load(image)                      # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()                       # Rect
        self.rct.center = xy

    def blit(self, scr : Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def uppdate(self,scr:Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)


class Bomb:
    def __init__(self,color,size,vxy,scr:Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size,size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy
    
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def uppdate(self,scr:Screen):
        self.rct.move_ip(self.vx,self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

class Buki:#武器の表示
    def __init__(self,image,size,xy):
        self.sfc = pg.image.load(image)#画像の読み込み
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)#画像サイズ
        self.rct = self.sfc.get_rect()                       
        self.rct.center = xy

    def blit(self, scr : Screen):#貼り付け
        scr.sfc.blit(self.sfc, self.rct)
    
    def uppdate(self,scr:Screen):#更新
        self.rct.move_ip()
        yoko, tate = check_bound(self.rct, scr.rct)
        self.rct *= yoko
        self.rct *= tate
        self.blit(scr)


def main():
    clock = pg.time.Clock()

    # スクリーンと背景画像
    scr = Screen("がんばれ、こうかとん",(1600,900),"fig/pg_bg.jpg")
    # こうかとん
    kkt = Bird("fig/6.png",2.0,(900, 400))
    # 爆弾
    bkd = Bomb((255,0,0),10,(+1,+1),scr)
    # 武器
    bki = Buki("fig/pg_bg.png",20,20)
    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.uppdate(scr)
        bkd.uppdate(scr)

        if kkt.rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(1000)
    

def check_bound(rct, scr_rct):
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

def time_time():#時間を表示
    end = time.time()
    return print(f"タイム：{end - start}")

if __name__ == "__main__":

    start = time.time()
    pg.init()
    main()
    time_time()#最終タイムの表示
    pg.quit()
    sys.exit()
