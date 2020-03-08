import pygame as pg
from copy import deepcopy
from snake import snake
from game_part import game_part
import random
import sys

pg.init()

FPS = 18
WIN_WIDTH = 500
WIN_HEIGHT = 500
WIDTH = 10
HEIGHT = 10

win = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("SNAKE GAME")
clock = pg.time.Clock()


font = pg.font.SysFont(None, 20)
click = False

def main():
    click = False
    while True:
        win.fill((0,0,0))
        draw_text("main menu", font, (255, 255, 255), win, 20, 20)

        mx, my = pg.mouse.get_pos()

        btn_1 = pg.Rect(50, 100, 200, 50)
        btn_2 = pg.Rect(50, 200, 200, 50)
        btn_3 = pg.Rect(50, 300, 200, 50)

        
        if btn_1.collidepoint((mx, my)):
            if click:
                snake_game()

        if btn_2.collidepoint((mx,my)):
            if click:
                options()
        if btn_3.collidepoint((mx, my)):
            if click:
                pg.quit()
                sys.exit()

        pg.draw.rect(win, (255, 0, 0), btn_1)
        pg.draw.rect(win, (255, 0, 0), btn_2)
        pg.draw.rect(win, (255, 0, 0), btn_3)

        draw_text("Play", font, (255, 255, 255), win, 125, 120)


        click = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pg.display.update()
        clock.tick(60)


def snake_game(): 

    xpos = random.randrange(10, WIN_WIDTH - WIDTH, WIDTH)
    ypos = random.randrange(10, WIN_HEIGHT - HEIGHT, HEIGHT)
    xvel = 0
    yvel = 0

    sn = snake(xpos, ypos)
    food = placeFood()

    temp = deepcopy(sn)

    # print(id(sn.body[0].xpos))
    # print(id(temp.body[0].xpos))

    game_over = False
    run = True
    while run:
        dt = clock.tick(FPS) / 1000
        temp = deepcopy(sn)

        win.fill((0, 0, 0))

        for i in range(len(sn.body)):
            print(str(i) + " \t X: " +
                  str(sn.body[i].xpos) + "  \t\t Y: " + str(sn.body[i].ypos) + " \t TEMP: X: " +
                  str(temp.body[i].xpos) + "  \t\t Y: " + str(temp.body[i].ypos))


        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                    main()


        keys = getKeys()

        ##------------------------For TESTING--------------------##
        ##

        if keys[pg.K_LSHIFT]:
            sn.addBody(sn.body[0].xpos + WIDTH, sn.body[0].ypos)

        if keys[pg.K_TAB]:
            # auch der Head wird deleted ^^
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

        # check if snake run into itself
        for i in range(len(sn.body) - 1):
            if sn.body[0].xpos == sn.body[i+1].xpos and sn.body[0].ypos == sn.body[i+1].ypos:
                game_over = True

        # check if snake run into  the border
        if sn.body[0].xpos < 0 or sn.body[0].xpos > (WIN_WIDTH - WIDTH) or sn.body[0].ypos < 0 or sn.body[0].ypos > (WIN_HEIGHT - HEIGHT):
            game_over = True

        if game_over:
            print("GAME OVER!")
            xpos = 50
            ypos = 50
            xvel = 0
            yvel = HEIGHT

            food = placeFood()
            print(food.xpos, food.ypos)

            for i in range(len(sn.body) - 1):
                sn.deleteBody()

            sn = snake(xpos, ypos)
            game_over = False
            death_screen()
            #run = False
            #  exit()

        else:
            if sn.body[0].xpos == food.xpos and sn.body[0].ypos == food.ypos:
                food = placeFood()
                sn.addBody(sn.body[0].xpos + WIDTH,
                           sn.body[0].ypos)

            if xvel != 0:
                xpos += xvel
            if yvel != 0:
                ypos += yvel

            sn.body[0].xpos = xpos
            sn.body[0].ypos = ypos

            for i in range(len(sn.body) - 1):
                sn.body[i+1].xpos = temp.body[i].xpos
                sn.body[i+1].ypos = temp.body[i].ypos

       

        for i in range(len(sn.body)):
            pg.draw.rect(win, (255, 255, 255),
                         (sn.body[i].xpos + 1, sn.body[i].ypos + 1, WIDTH - 2, HEIGHT - 2))
            # damit der head eine andere Farbe hat
            # if(i == 0):
            #     pg.draw.rect(win, (0, 0, 255),
            #                 (sn.body[i].xpos, sn.body[i].ypos, WIDTH, HEIGHT))
            # else:
            #     pg.draw.rect(win, (255, 255, 255),
            #             (sn.body[i].xpos, sn.body[i].ypos, WIDTH, HEIGHT))

        # Draw Food
        pg.draw.rect(win, (255, 0, 0), (food.xpos, food.ypos, WIDTH, HEIGHT))
        draw_text("SCORE: " + str(len(sn.body)),
                  font, (255, 255, 255), win, 20, 20)
        pg.display.update()

    pg.quit()


def options():
    running = True
    while running:
        win.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), win, 20, 20)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        pg.display.update()
        clock.tick(60)


def death_screen():
    running = True
    while running:
        win.fill((0, 0, 0))

        draw_text('Press Enter to Respawn or Esc to Close', font, (255, 255, 255), win, int(WIN_WIDTH/4), int(WIN_HEIGHT/2) -20)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    main()
                if event.key == pg.K_RETURN:
                    snake_game()

        pg.display.update()
        clock.tick(60)




def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def getKeys():
    return pg.key.get_pressed()


def placeFood():
    return game_part(random.randrange(10, WIN_WIDTH - WIDTH, WIDTH),
                     random.randrange(10, WIN_HEIGHT - HEIGHT, HEIGHT))


if __name__ == '__main__':
    main()
