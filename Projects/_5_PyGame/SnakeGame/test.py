from snake import snake
import random

s = snake(20,30,10,10)


s.addBody(100, 90)

x = random.randint(0, 500 / 10)*10,

print(str(x))

for i in s.body:
    print(i.xpos)
    print(i.ypos)

