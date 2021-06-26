import numpy as np
import cv2


class CubeSide:
    def __init__(self):

        self.arr = np.zeros(
            shape=(3, 3)
        )  # emty array with 0 later containing the sides colors
        self.reset()
        # red       0
        # blue      1
        # green     2
        # yellow    3
        # orange    4
        # white     5
        self.colors = {
            "red": 0,
            "blue": 1,
            "green": 2,
            "yellow": 3,
            "orange": 4,
            "white": 5,
        }

    # resets the colors of the side to undefind (-1)
    def reset(self):
        self.arr.fill(-1)  # fill with -1

    # prints the CubeSide array
    def print_arr(self):
        print(self.arr)

    # sets array to color
    def set_color(self, posx, posy, color):
        if color == "red":
            self.arr[posx][posy] = 0
        elif color == "blue":
            self.arr[posx][posy] = 1
        elif color == "green":
            self.arr[posx][posy] = 2
        elif color == "yellow":
            self.arr[posx][posy] = 3
        elif color == "orange":
            self.arr[posx][posy] = 4
        elif color == "white":
            self.arr[posx][posy] = 5
        else:  # color not defined
            self.arr[posx][posy] = -1

    def extract_cube_colors(self, img_path, x, y, w, h):
        img = cv2.imread(img_path)

        w1 = int(w / 3)
        h1 = int(h / 3)

        colorlist = []

        y1 = y
        for i in range(3):
            x1 = int(x + i * w1)

            crop_img = img[y1 + 20 : y1 + h1 - 20, x1 + 20 : x1 + w1 - 20]

            avg_color_per_row = np.average(crop_img, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            colorlist.append(avg_color)

        y1 = y1 + h1
        for i in range(3):
            x1 = int(x + i * w1)

            crop_img = img[y1 + 20 : y1 + h1 - 20, x1 + 20 : x1 + w1 - 20]

            avg_color_per_row = np.average(crop_img, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            colorlist.append(avg_color)

        y1 = y1 + h1
        for i in range(3):
            x1 = int(x + i * w1)

            crop_img = img[y1 + 20 : y1 + h1 - 20, x1 + 20 : x1 + w1 - 20]

            avg_color_per_row = np.average(crop_img, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            colorlist.append(avg_color)
