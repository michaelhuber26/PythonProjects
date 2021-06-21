import msvcrt

while True:
    enter = msvcrt.getch()
    print(": {0} == {1}".format(enter, enter.decode('ASCII')))

    if(enter.decode('ASCII') == '\r'):
        print("ENTER")

