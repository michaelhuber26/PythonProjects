import pygame as pg
from copy import deepcopy
from snake import snake
from game_part import game_part
import random

pg.init()

FPS = 20
WIN_WIDTH = 500
WIN_HEIGHT = 500
WIDTH = 10
HEIGHT = 10


def main():

    win = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pg.display.set_caption("SNAKE GAME")
    clock = pg.time.Clock()

    xpos = 50
    ypos = 50
    xvel = 0
    yvel = HEIGHT

    sn = snake(xpos, ypos, xvel, yvel)
    food = placeFood()


    # for i in range(20):
    #     sn.addBody(sn.body[i].xpos + WIDTH,
    #                sn.body[i].ypos, 0, 0)

    temp = deepcopy(sn)

    print(id(sn.body[0].xpos))
    print(id(temp.body[0].xpos))

    run = True
    game_start = False
    while run:

        dt = clock.tick(FPS) / 1000
        temp = deepcopy(sn)

        for i in range(len(sn.body)):
            print(str(i) + " \t X: " +
                  str(sn.body[i].xpos) + "  \t\t Y: " + str(sn.body[i].ypos) + " \t TEMP: X: " +
                  str(temp.body[i].xpos) + "  \t\t Y: " + str(temp.body[i].ypos))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = getKeys()

        ##------------------------For TESTING--------------------##
        ## 

        if keys[pg.K_LSHIFT]:
            sn.addBody(sn.body[0].xpos + WIDTH, sn.body[0].ypos, 0, 0)

        if keys[pg.K_TAB]:
            #auch der Head wird deleted ^^
            sn.deleteBody()

        ##--------------------------------------------------------##

        if keys[pg.K_UP]and yvel == 0:
            yvel = -HEIGHT
            xvel = 0

        if keys[pg.K_DOWN]and yvel == 0:
            yvel = HEIGHT
            xvel = 0

        if keys[pg.K_LEFT] and xvel == 0:
            xvel = -WIDTH
            yvel = 0

        if keys[pg.K_RIGHT] and xvel == 0:
            xvel = WIDTH
            yvel = 0

        
        if sn.body[0].xpos == 0 or sn.body[0].xpos == (WIN_WIDTH - WIDTH) or sn.body[0].ypos == 0 or sn.body[0].ypos == (WIN_HEIGHT - HEIGHT):
            print("GAME OVER!")
            xpos = 50
            ypos = 50
            xvel = 0
            yvel = HEIGHT

            food = placeFood()

            for i in range(len(sn.body) - 1):
                sn.body[i].xpos = xpos + (i*WIDTH)
                sn.body[i].ypos = ypos

            #run = False
            #  exit()

        

        else:
            if sn.body[0].xpos == food.xpos and sn.body[0].ypos == food.ypos:
                food = placeFood()
                sn.addBody(sn.body[0].xpos + WIDTH,
                           sn.body[0].ypos, 0, 0)

            if xvel != 0:
                xpos += xvel
            if yvel != 0:
                ypos += yvel

            sn.body[0].xpos = xpos
            sn.body[0].ypos = ypos
            #sn.body[0].xvel = xvel
            #sn.body[0].yvel = yvel

            for i in range(len(sn.body) - 1):
                sn.body[i+1].xpos = temp.body[i].xpos
                sn.body[i+1].ypos = temp.body[i].ypos

        
       
        win.fill((0, 0, 0))

        for i in range(len(sn.body)):
            pg.draw.rect(win, (255, 255, 255),(sn.body[i].xpos, sn.body[i].ypos, WIDTH, HEIGHT))
            # damit der head eine andere Farbe hat
            # if(i == 0):
            #     pg.draw.rect(win, (0, 0, 255),
            #                 (sn.body[i].xpos, sn.body[i].ypos, WIDTH, HEIGHT))
            # else:
            #     pg.draw.rect(win, (255, 255, 255),
            #             (sn.body[i].xpos, sn.body[i].ypos, WIDTH, HEIGHT))
        
        
        pg.draw.rect(win, (255, 0, 0),(food.xpos, food.ypos, WIDTH, HEIGHT))

       

        pg.display.update()


    pg.quit()


def getKeys():
    return pg.key.get_pressed()


def placeFood():
    return game_part(random.randint(0, WIN_WIDTH / WIDTH)*WIDTH,
                     random.randint(0, WIN_HEIGHT / HEIGHT)*HEIGHT, 0, 0)


if __name__ == '__main__':
    main()
