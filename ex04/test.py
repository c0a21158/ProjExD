import pygame as pg
import sys




def main():
    pg.display.set_caption("初めて初めてのPygame")#タイトルバーに表示する
    
    screen = pg.display.set_mode((800,600))#800x600の画面Surfaceを生成する
    tori_img = pg.image.load("ex03/fig/6.png")    #Surface
    tori_img = pg.transform.rotozoom(tori_img,0,2.0)#Surface
    tori_rect=tori_img.get_rect()
    tori_rect.center = 700,400
    screen.blit(tori_img, tori_rect)
    pg.display.update()
    clock.tick(5)


if __name__ == "__main__":
    clock = pg.time.Clock
    pg.init()
    main()#gameのメイン
    pg.quit()
    sys.exit()
