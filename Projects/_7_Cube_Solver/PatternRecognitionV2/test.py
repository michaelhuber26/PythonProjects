import numpy as np
import cv2

img = cv2.imread("cube.jpg")
x = 155
y = 83
w = 325
h = 322

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

print(colorlist[2])
