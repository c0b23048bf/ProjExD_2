import os
import sys
import pygame as pg
from random import randint


WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg") 
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    clock = pg.time.Clock()
    tmr = 0
    bomb_x ,bomb_y = randint(0,HEIGHT-20),randint(0,HEIGHT-20)
    
    bomb = pg.Surface((20,20))
    bomb.set_colorkey((0,0,0))
    pg.draw.circle(bomb,(255,0,0),(10,10),10)
    bomb_rect = bomb.get_rect()
    bomb_rect.center = bomb_x,bomb_y
    vx,vy = 5,5
    
    
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            

            
        screen.blit(bg_img, [0, 0])
        bomb_x,bomb_y = bomb_x + vx ,bomb_y + vy
        screen.blit(bomb,[bomb_x,bomb_y])
        
        key_lst = pg.key.get_pressed()
        sum_list = {pg.K_UP:(0,-5),pg.K_DOWN:(0,+5),pg.K_LEFT:(-5,0),pg.K_RIGHT:(+5,0)}
        for key,value in zip(sum_list.keys(),sum_list.values()):
            if key_lst[key]: 
                kk_rct.move_ip(value)
                
        b_v =  check_bound(bomb_rect)
        if b_v[0] == False:
            vx *= -1
            print("a")
        if b_v[1] == False:
            vy *= -1
            print("b")
            
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)
"""       
def vvv(kk_r):
    kv = [True,True,True,True]
    if kk_r.left < 0 :
        kv[0] = False
        print("dd")
    if kk_r.right > 1600:
        kv[1] = False
    if kk_r.top < 0:
        kv[2] = False
    if kk_r.bottom > 900:
        kv[3] = False
        print("dx")
    
    return kv
"""

def check_bound(obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    引数：こうかとんRectかばくだんRect
    戻り値：タプル（横方向判定結果，縦方向判定結果）
    画面内ならTrue，画面外ならFalse
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: # 横方向判定
        yoko = False
        print(9)
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom: # 縦方向判定
        tate = False
        print(8)
    return yoko, tate
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
