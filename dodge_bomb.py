import os
import pygame as pg
from random import randint
import sys
import time

WIDTH, HEIGHT = 1400, 700
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    #ディスプレイ設定
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode(( WIDTH , HEIGHT ))
    
    #背景設定
    bg_img = pg.image.load("fig/pg_bg.jpg") 
    
    #こうかとん描画
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    
    #反転こうかとん
    kk_img2 = pg.transform.flip(kk_img,False,True)
    kk_img2 = pg.transform.rotozoom(kk_img2,0 , 1.0)
    
    #時間設定
    clock = pg.time.Clock()
    tmr = 0
    
    #爆弾の描画と移動量
    bomb = pg.Surface((20 , 20))
    bomb.set_colorkey((0 , 0 , 0))
    pg.draw.circle(bomb , (255 , 0 , 0) , (10 , 10) , 10)
    bomb_rect = bomb.get_rect()
    bomb_rect.center = randint(0 , HEIGHT-20) , randint(0 , HEIGHT-20)
    vx,vy = 5 , 5
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            

        #背景と爆弾
        screen.blit(bg_img, [0 , 0])
        bomb_rect.move_ip(vx , vy)
        screen.blit(bomb , bomb_rect)
        
        sx = 0
        sy = 0
        
        #キーによるこうかとんの制御
        key_lst = pg.key.get_pressed()
        sum_list = {pg.K_UP:(0 , -5) , pg.K_DOWN:(0 , +5),pg.K_LEFT:(-5 , 0),pg.K_RIGHT:(+5 , 0)}
        for key,value in zip(sum_list.keys(),sum_list.values()):
            if key_lst[key]: 
                kk_rct.move_ip(value)
                b_v =  check_bound(kk_rct)
                sx += value[0]
                sy += value[1]
                if b_v[0] == False:
                    kk_rct.move_ip((-value[0] , value[1]))
                if b_v[1] == False:
                    kk_rct.move_ip((value[0] , -value[1]))
        
        #壁の反射
        b_v =  check_bound(bomb_rect)
        if b_v[0] == False:
            vx *= -1
            print("a")
        if b_v[1] == False:
            vy *= -1
            print("b")
        
        #爆弾とこうかとんの衝突
        if kk_rct.colliderect(bomb_rect):
            gameover(screen)
            pg.display.update()
            time.sleep(5)
            break
        
        screen.blit(hanntenn(kk_img , kk_img2 , sx , sy) , kk_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


#Game over
def gameover(screen):
    rrr = pg.Surface((WIDTH , HEIGHT))
    pg.draw.rect(rrr , (0 , 0 , 0) , (0 , 0 , WIDTH , HEIGHT) , width = 0)
    rrr.set_alpha(200)
    screen.blit(rrr , [0 , 0])
    fonto = pg.font.Font(None , 80)
    txt = fonto.render("Game Over" , True , (255,255,255))
    screen.blit(txt , [WIDTH/2 -100 , HEIGHT/2])
    kk_img3 = pg.transform.rotozoom(pg.image.load("fig/8.png") , 0, 1.0)
    kk_rct3 = kk_img3.get_rect()
    kk_rct3.center = WIDTH/2 -150 , HEIGHT/2
    screen.blit(kk_img3 , kk_rct3)
    kk_img4 = pg.transform.rotozoom(pg.image.load("fig/8.png") , 0, 1.0)
    kk_rct4 = kk_img4.get_rect()
    kk_rct4.center = WIDTH/2 + 250 , HEIGHT/2
    screen.blit(kk_img4 , kk_rct4)

#こうかとんの反転
def hanntenn(kk_img , kk_img2 , sx , sy):
    vvv = {(0 , -5):pg.transform.rotozoom(kk_img2 , -90 , 1.0),
    (+5 , -5):pg.transform.rotozoom(kk_img2 , -135 , 1.0),
    (+5 , 0):pg.transform.rotozoom(kk_img2 , -180 , 1.0),
    (+5 , +5):pg.transform.rotozoom(kk_img2 , -225 , 1.0),
    (0 , +5):pg.transform.rotozoom(kk_img2 , 90 , 1.0),
    (-5 , +5):pg.transform.rotozoom(kk_img , 45 , 1.0),
    (-5 , 0):pg.transform.rotozoom(kk_img , 0 , 1.0),
    (-5 , -5):pg.transform.rotozoom(kk_img , -45 , 1.0),
    }
    if (sx , sy) in vvv:
        up_kk_img = vvv[(sx , sy)]
        return up_kk_img
    else:
        return kk_img

#ばくだんの反転
def check_bound(obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    引数：こうかとんRectかばくだんRect
    戻り値：タプル（横方向判定結果，縦方向判定結果）
    画面内ならTrue，画面外ならFalse
    """
    yoko , tate = True , True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: # 横方向判定
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom: # 縦方向判定
        tate = False
    return yoko , tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
