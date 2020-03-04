from snake import snake

s = snake(20,30,10,10)


s.addBody(100, 90, 80, 70)

for i in s.body:
    print(i.xpos)
    print(i.ypos)
    print(i.xvel)
    print(i.yvel)
    


