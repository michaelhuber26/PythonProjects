from snake import snake
import random

s = snake(20,30,10,10)


s.addBody(100, 90, 80, 70)

x = random.randint(0, 500 / 10)*10,

print(str(x))

for i in s.body:
    print(i.xpos)
    print(i.ypos)
    print(i.xvel)
    print(i.yvel)
    


