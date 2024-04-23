import os
import sys
import pygame as pg
from random import randint
import time

WIDTH, HEIGHT = 1400, 700
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg") 
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    
    kk_img2 = pg.transform.flip(kk_img,False,True)
    kk_img2 = pg.transform.rotozoom(kk_img2,0,1.0)
    
    vvv = {(0,-5):pg.transform.rotozoom(kk_img2,-90,1.0),
        (+5,-5):pg.transform.rotozoom(kk_img2,-135,1.0),
        (+5,0):pg.transform.rotozoom(kk_img2,-180,1.0),
        (+5,+5):pg.transform.rotozoom(kk_img2,-225,1.0),
        (0,+5):pg.transform.rotozoom(kk_img2,90,1.0),
        (-5,+5):pg.transform.rotozoom(kk_img,45,1.0),
        (-5,0):pg.transform.rotozoom(kk_img,0,1.0),
        (-5,-5):pg.transform.rotozoom(kk_img,-45,1.0),
    }
    
    clock = pg.time.Clock()
    tmr = 0
    
    bomb = pg.Surface((20,20))
    bomb.set_colorkey((0,0,0))
    pg.draw.circle(bomb,(255,0,0),(10,10),10)
    bomb_rect = bomb.get_rect()
    bomb_rect.center = randint(0,HEIGHT-20),randint(0,HEIGHT-20)
    vx,vy = 5,5
    
    
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            

            
        screen.blit(bg_img, [0, 0])
        bomb_rect.move_ip(vx,vy)
        screen.blit(bomb,bomb_rect)
        
        sx = 0
        sy = 0
        
        key_lst = pg.key.get_pressed()
        sum_list = {pg.K_UP:(0,-5),pg.K_DOWN:(0,+5),pg.K_LEFT:(-5,0),pg.K_RIGHT:(+5,0)}
        for key,value in zip(sum_list.keys(),sum_list.values()):
            if key_lst[key]: 
                kk_rct.move_ip(value)
                b_v =  check_bound(kk_rct)
                sx += value[0]
                sy += value[1]
                if b_v[0] == False:
                    kk_rct.move_ip((-value[0],value[1]))
                if b_v[1] == False:
                    kk_rct.move_ip((value[0],-value[1]))

                
        b_v =  check_bound(bomb_rect)
        if b_v[0] == False:
            vx *= -1
            print("a")
        if b_v[1] == False:
            vy *= -1
            print("b")
        
        if kk_rct.colliderect(bomb_rect):
            back = pg.Surface((WIDTH,HEIGHT))
            pg.draw.rect(back,(255,255,255),(10,10),10)
            back.set_alpha(0.5)
            fonto = pg.font.Font(None,80)
            txt = fonto.render("Game Over",True,(255,255,255))
            screen.blit(txt, [300,200])
            time.sleep(5)
            break
            
        if (sx,sy) in vvv:
            up_kk_img = vvv[(sx,sy)]
            screen.blit(up_kk_img, kk_rct)
        else:
            screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)
        



def check_bound(obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    引数：こうかとんRectかばくだんRect
    戻り値：タプル（横方向判定結果，縦方向判定結果）
    画面内ならTrue，画面外ならFalse
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: # 横方向判定
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom: # 縦方向判定
        tate = False
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
