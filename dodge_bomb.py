import random
import tkinter as tk
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    #kk_img_re = pg.transform.flip(kk_img, True, False)
    #kk_img_0 = pg.transform.rotozoom(kk_img_re, 90, 1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bomb_img = pg.Surface((20, 20))
    pg.draw.circle(bomb_img, (255, 0, 0), (10, 10), 10)
    bomb_x = random.randint(0, WIDTH)
    bomb_y = random.randint(0, HEIGHT)
    bomb_img.set_colorkey((0, 0, 0))
    bomb_rct = bomb_img.get_rect()
    bomb_rct.center = bomb_x, bomb_y  
    gokk = {
        pg.K_UP: (0, -5),
        pg.K_DOWN: (0, 5),
        pg.K_LEFT: (-5, 0),
        pg.K_RIGHT: (5, 0),
    }
    vx, vy = 5, 5

    #kk_rct_kind = {
    #    kk_img_0: (0, -5)
    #}

    def check_rct(rect: pg.Rect) -> tuple[bool, bool]:
        """
        こうかとん、爆弾が画面内か画面外かを判定
        引数：こうかとんrect or 爆弾rect
        戻り値：横、縦方向の判定結果タプル
        (True:画面内　/　False:画面外)
        """
        yoko, tate = True, True
        if rect.left < 0 or WIDTH < rect.right:
            yoko = False
        if rect.top < 0 or HEIGHT < rect.bottom:
            tate = False
        return yoko, tate
    clock = pg.time.Clock()
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        if kk_rct.colliderect(bomb_rct):
            kk_rct.center = 900, 400

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, mv in gokk.items():
            if key_lst[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)
        if check_rct(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
         
        bomb_rct.move_ip(vx, vy)
        yoko, tate = check_rct(bomb_rct)
        if 0 < vx <= 10 :
            vx += 0.03
        if 0 < vy <= 10:
            vy += 0.03
        if not yoko:
            vx *= -1
            if 0 < vx < 10:
                vx -= 0.03
        if not tate:
            vy *= -1
            if 0 < vy < 10:
                vy -= 0.03
        screen.blit(bomb_img, bomb_rct)

        pg.display.update()
        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()