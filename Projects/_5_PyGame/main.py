import pygame as pg

pg.init()

FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 500

win = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("FIRST GAME")
clock = pg.time.Clock()

x = 20
y = 20
width = 50
height = 50
vel = 5


run = True
while run:
    dt = clock.tick(FPS) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_UP] and y != 0:
        y -= vel

    if keys[pg.K_DOWN]and y != (WIN_HEIGHT - height):
        y += vel

    if keys[pg.K_LEFT] and x != 0:
        x -= vel

    if keys[pg.K_RIGHT] and x != (WIN_WIDTH - width):
        x += vel

    win.fill((0, 0, 0))
    pg.draw.rect(win, (255, 255, 255), (x, y, width, height))
    pg.display.update()

pg.quit()
