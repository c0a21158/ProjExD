import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")#タイトルバーに表示する
    screen_sfc = pg.display.set_mode((1600,900))#Surface
    screen_rect =screen_sfc.get_rect()#Rect
    bgimag_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    bgimag_rect=bgimag_sfc.get_rect()#Rect
    screen_sfc.blit(bgimag_sfc,bgimag_rect)

    #練習3
    kkimag_sfc = pg.image.load("fig/6.png")#Surface
    kkimag_sfc = pg.transform.rotozoom(kkimag_sfc,0,2.0)#Surface
    kkimag_rect = kkimag_sfc.get_rect() #Rect
    kkimag_rect.center = 900,400



    #練習5：爆弾
    bmimag_sfc = pg.Surface((20,20)) #Surface
    pg.draw.circle(bmimag_sfc, (255,0,0),(10,10),10) #Surface
    bmimag_rect = bmimag_sfc.get_rect() #Rect
    bmimag_rect.centerx = random.randint(0,screen_rect.width)
    bmimag_rect.centery = random.randint(0,screen_rect.height)
   


    #練習6
    vx, vy = +1, +1


    while True:
        screen_sfc.blit(bgimag_sfc,bgimag_rect)
        screen_sfc.blit(kkimag_sfc,kkimag_rect)

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        

        #練習4
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True:kkimag_rect.centery -= 1
        if key_states[pg.K_DOWN] == True:kkimag_rect.centery += 1
        if key_states[pg.K_LEFT] == True:kkimag_rect.centerx -= 1
        if key_states[pg.K_RIGHT] == True:kkimag_rect.centerx += 1

        bmimag_rect.move_ip(vx,vy)
        screen_sfc.blit(bmimag_sfc,bmimag_rect)
        
        pg.display.update()
        clock.tick(1000)


    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
