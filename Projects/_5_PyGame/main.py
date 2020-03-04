import pygame as pg

pg.init()

FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 500


def main():

    win = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pg.display.set_caption("FIRST GAME")
    clock = pg.time.Clock()

    xpos = 20
    ypos = 20
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

        if keys[pg.K_UP] and ypos != 0:
            ypos -= vel

        if keys[pg.K_DOWN]and ypos != (WIN_HEIGHT - height):
            ypos += vel

        if keys[pg.K_LEFT] and xpos != 0:
            xpos -= vel

        if keys[pg.K_RIGHT] and xpos != (WIN_WIDTH - width):
            xpos += vel

        win.fill((0, 0, 0))
        pg.draw.rect(win, (255, 255, 255), (xpos, ypos, width, height))
        pg.display.update()


    pg.quit()



if __name__ == '__main__':
    main()
