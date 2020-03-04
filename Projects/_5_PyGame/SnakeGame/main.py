import pygame as pg
from copy import deepcopy
from snake import snake

pg.init()

FPS = 20
WIN_WIDTH = 500
WIN_HEIGHT = 500


def main():

    win = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pg.display.set_caption("FIRST GAME")
    clock = pg.time.Clock()

    width = 10
    height = 10
    xpos = 50
    ypos = 50
    xvel = 0
    yvel = height

    sn = snake(xpos, ypos, xvel, yvel)

    for i in range(20):
        sn.addBody(sn.body[i].xpos + width,
                       sn.body[i].ypos, 0, 0)
        
    temp = deepcopy(sn)
    
    print(id(sn.body[0].xpos))
    print(id(temp.body[0].xpos))

    run = True
    while run:
        
        dt = clock.tick(FPS) / 1000
        temp = deepcopy(sn)

        for i in range(len(sn.body)):
            print(str(i) + " \t X: " +
                  str(sn.body[i].xpos) + "  \t\t Y: " + str(sn.body[i].ypos) +" \t TEMP: X: " +
                  str(temp.body[i].xpos) + "  \t\t Y: " + str(temp.body[i].ypos))


        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()

        if keys[pg.K_UP]and yvel == 0:
            yvel = -height
            xvel = 0

        if keys[pg.K_DOWN]and yvel == 0:
            yvel = height
            xvel = 0

        if keys[pg.K_LEFT] and xvel == 0:
            xvel = -width
            yvel = 0

        if keys[pg.K_RIGHT] and xvel == 0:
            xvel = width
            yvel = 0

        
        sn.body[0].xpos = xpos
        sn.body[0].ypos = ypos
        sn.body[0].xvel = xvel
        sn.body[0].yvel = yvel

        for i in range(len(sn.body) - 1):
            sn.body[i+1].xpos = temp.body[i].xpos
            sn.body[i+1].ypos = temp.body[i].ypos

        if sn.body[0].xpos == 0 or sn.body[0].xpos == (WIN_WIDTH - width) or sn.body[0].ypos == 0 or sn.body[0].ypos == (WIN_HEIGHT - height):
            print("GAME OVER!")
            xpos = 50
            ypos = 50
            xvel = 0
            yvel = 0

            for i in range(len(sn.body) - 1):
                sn.body[i].xpos = xpos + (i*width)
                sn.body[i].ypos = ypos
                
            #run = False
            #  exit()

        else: 
            if xvel != 0:
                xpos += xvel
            if yvel != 0:
                ypos += yvel

        


        
        # pg.draw.rect(win, (255, 0, 0), (sn.body[0].xpos, sn.body[0].ypos, width, height))
        # pg.draw.rect(win, (0, 255, 0), (sn.body[1].xpos, sn.body[1].ypos, width, height))
        # pg.draw.rect(win, (0, 0, 255), (sn.body[2].xpos, sn.body[2].ypos, width, height))
        # pg.draw.rect(win, (255, 255, 0), (sn.body[3].xpos, sn.body[3].ypos, width, height))
        
        # den body der snake erst im nächsten frame zeichnen, damit xpos und ypos der bodyteile stimmen


        win.fill((0, 0, 0))

        for i in range(len(sn.body)):
           pg.draw.rect(win, (255, 255, 255), (sn.body[i].xpos, sn.body[i].ypos, width, height))


        pg.display.update()

       
    pg.quit()


if __name__ == '__main__':
    main()
