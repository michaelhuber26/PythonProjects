cube = 'wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'

from rubik_solver import utils


print("\nKociemba:\n {}".format(utils.solve(cube, 'Kociemba')))






'''

Kociemba solver needs the following cubies at place:

4 (Upper center): YELLOW
13 (Left center): BLUE
22 (Front center): RED
31 (Right center): GREEN
40 (Back center): ORANGE
49 (Down center): WHITE


----------------
| 0 | 1 | 2 |
----------------
| 3 | 4 | 5 |
----------------
| 6 | 7 | 8 |
----------------
-------------------------------------------------------------
| 9 | 10 | 11 | 18 | 19 | 20 | 27 | 28 | 29 | 36 | 37 | 38 |
-------------------------------------------------------------
| 12 | 13 | 14 | 21 | 22 | 23 | 30 | 31 | 32 | 39 | 40 | 41 |
-------------------------------------------------------------
| 15 | 16 | 17 | 24 | 25 | 26 | 33 | 34 | 35 | 42 | 43 | 44 |
-------------------------------------------------------------
----------------
| 45 | 46 | 47 |
----------------
| 48 | 49 | 50 |
----------------
| 51 | 52 | 53 |
----------------

'''
