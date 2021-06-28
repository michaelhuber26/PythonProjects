import numpy as np
import cv2

img = cv2.imread("cube.jpg")
x = 198
y = 85
w = 318
h = 317

crop_img = img[y : y + h, x : x + w]

cv2.imwrite("cropped.jpg", crop_img)


colorlist = []
w1 = int(w / 3)
h1 = int(h / 3)

y1 = y
for i in range(3):
    x1 = int(x + i * w1)

    crop_img = img[y1 + 20 : y1 + h1 - 20, x1 + 20 : x1 + w1 - 20]

    cv2.imwrite("1cropped" + str(i) + ".jpg", crop_img)
    avg_color_per_row = np.average(crop_img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    colorlist.append(avg_color)
    print(avg_color)

y1 = y1 + h1
for i in range(3):
    x1 = int(x + i * w1)

    crop_img = img[y1 + 20 : y1 + h1 - 20, x1 + 20 : x1 + w1 - 20]

    cv2.imwrite("2cropped" + str(i) + ".jpg", crop_img)
    avg_color_per_row = np.average(crop_img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    colorlist.append(avg_color)
    print(avg_color)

y1 = y1 + h1
for i in range(3):
    x1 = int(x + i * w1)

    crop_img = img[y1 + 20 : y1 + h1 - 20, x1 + 20 : x1 + w1 - 20]

    cv2.imwrite("3cropped" + str(i) + ".jpg", crop_img)
    avg_color_per_row = np.average(crop_img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    colorlist.append(avg_color)
    print(avg_color)


def getColorName(color):
    if color == 0:
        return "red"
    if color == 1:
        return "blue"
    if color == 2:
        return "green"
    if color == 3:
        return "yellow"
    if color == 4:
        return "orange"
    if color == 5:
        return "white"


def is_color_found(color, boundary):
    found_color = True
    for i in range(0, 3):
        # print("{0} >= {1}".format(boundary[0][i], int(color_bgr[i])))
        if not (
            (int(color[i]) >= boundary[0][i]) and (int(color[i]) <= boundary[1][i])
        ):
            found_color = False
    return found_color


boundaries = [
    ([50, 40, 100], [100, 60, 255]),  # red pos:  00 01
    ([86, 31, 0], [255, 120, 50]),  # blue      10 11
    ([50, 120, 0], [150, 255, 135]),  # green     20 21
    ([0, 205, 205], [185, 255, 255]),  # yellow    30 31
    ([0, 80, 240], [160, 160, 255]),  # orange    40 41
    ([215, 215, 215], [255, 255, 255]),  # white     50 51
]

arr = np.zeros(shape=(3, 3))  # emty array with 0 later containing the sides colors

# prints color names (eg. blue) from colorlist
def get_colornames():
    global arr
    arr = arr.flatten()  # 2d array to 1d with numpy

    retstr = ""
    found_color = False
    cnt = 0
    for colorpos, color_bgr in enumerate(colorlist):
        cnt = 0
        for boundary in boundaries:
            found_color = is_color_found(color_bgr, boundary)

            if found_color == True:
                retstr = getColorName(cnt)
                print("{0}. color: {1} = {2}".format(colorpos, color_bgr, retstr))
                arr[colorpos] = cnt
            cnt += 1

    arr = np.reshape(arr, (-1, 3))  # 1d arry -> 2d


get_colornames()
print(arr)
