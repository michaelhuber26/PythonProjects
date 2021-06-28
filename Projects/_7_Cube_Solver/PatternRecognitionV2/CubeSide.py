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
            0: "red",
            1: "blue",
            2: "green",
            3: "yellow",
            4: "orange",
            5: "white",
        }

        self.boundaries = [
            ([50, 40, 100], [110, 70, 255]),  # red pos:  00 01
            ([86, 31, 0], [255, 120, 50]),  # blue      10 11
            ([50, 120, 0], [150, 255, 140]),  # green     20 21
            ([0, 205, 205], [185, 255, 255]),  # yellow    30 31
            ([0, 80, 240], [170, 185, 255]),  # orange    40 41
            ([215, 215, 215], [255, 255, 255]),  # white     50 51
        ]

    # resets the colors of the side to undefind (-1)
    def reset(self):
        self.arr.fill(-1)  # fill with -1

    # prints the CubeSide array
    def print_arr(self):
        print(self.arr)
        for i in range(9):
            print()

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

        print(colorlist)
        self.fill_color_array(colorlist)

    def is_color_found(self, color, boundary):
        found_color = True
        for i in range(0, 3):
            # print("{0} >= {1}".format(boundary[0][i], int(color_bgr[i])))
            if not (
                (int(color[i]) >= boundary[0][i]) and (int(color[i]) <= boundary[1][i])
            ):
                found_color = False
        return found_color

    def fill_color_array(self, colorlist):

        global arr

        self.arr = self.arr.flatten()  # 2d array to 1d with numpy

        retstr = ""
        found_color = False
        cnt = 0
        for colorpos, color_bgr in enumerate(colorlist):
            cnt = 0
            for boundary in self.boundaries:
                found_color = self.is_color_found(color_bgr, boundary)

                if found_color == True:
                    retstr = self.colors[cnt]
                    print("{0}. color: {1} = {2}".format(colorpos, color_bgr, retstr))
                    self.arr[colorpos] = cnt
                cnt += 1

        self.arr = np.reshape(self.arr, (-1, 3))  # 1d arry -> 2d
