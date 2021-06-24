import numpy as np

class CubeSide:

    def __init__(self):

        self.arr = np.zeros(shape=(3, 3))  # emty array with 0 later containing the sides colors
        self.reset()
        # red       0
        # blue      1 
        # green     2 
        # yellow    3
        # orange    4
        # white     5
       
    # resets the colors of the side to undefind (-1)   
    def reset(self):
        self.arr.fill(-1)  # fill with -1

    def print_arr(self):
        print(self.arr)

    def set_color(self, posx, posy, color):
        if(color == 'red'):
            self.arr[posx][posy]= 0
        elif(color == 'blue'):
            self.arr[posx][posy]= 1
        elif(color == 'green'):
            self.arr[posx][posy]= 2
        elif(color == 'yellow'):
            self.arr[posx][posy]= 3
        elif(color == 'orange'):
            self.arr[posx][posy]= 4
        elif(color == 'white'):
            self.arr[posx][posy]= 5
        else: # color not defined
            self.arr[posx][posy] = -1
    
  



