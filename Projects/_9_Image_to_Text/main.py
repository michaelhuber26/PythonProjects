from inspect import CO_NEWLOCALS
import os
import numpy as np
import sys
from PIL import Image

# console window:   width: 120 characters
#                   height: 60 characters
CONS_W = 120
CONS_H = 60

# 29 chars
DENSITY = "Ñ@#W$9876543210?!abc;:+=-,._ "


def convImage(path):
    img = Image.open(path)
    img = img.convert("RGB")
    # img.show()
    return img


# for more accurate brightness of pixels Luminance formula (maybe later)
# https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
# https://stackoverflow.com/questions/6442118/python-measuring-pixel-brightness
def getBrightness(x, y, img):
    pixelRGB = img.getpixel((x, y))
    R, G, B = pixelRGB
    brightness = sum([R, G, B]) / 3
    return brightness


def resizeImage(img, name):
    img.thumbnail((CONS_W, CONS_H * 2))
    img.save("img/" + name)
    return img


def getImageSize(img):
    width, height = img.size
    return (width, height)


def getCharForBrightness(brightness):
    DENSITY_rev = DENSITY[::-1]
    step = 255 / 29
    str = ""
    for i in range(0, 30):
        if (brightness) < step * i:
            str = DENSITY_rev[i - 1]
            return str

    return ""


def getConvertedString(arr):
    retstr = ""

    for y in range(CONS_H):
        for x in range(CONS_W):
            retstr += getCharForBrightness(arr[x][y])

    return retstr


def main():
    clear()
    img = Image.open("img/test.png")
    resizeImage(img, "converted.png")

    img = convImage("img/converted.png")
    imgw, imgh = getImageSize(img)
    # x, y = 0, 0
    # getBrightness(x, y, img)

    arr = np.empty([CONS_W, CONS_H])

    for h in range(0, (2 * CONS_H), 2):
        for w in range(CONS_W):
            if (h % 2) == 0:
                arr[w][int(h / 2)] = int(getBrightness(w, h, img))

    # for i in range(255):
    #     print(getCharForBrightness(i), end=" ")
    # print("END")

    print(getConvertedString(arr))
    while True:
        input()


def clear():
    return os.system("cls")


def sysPrint(str):
    sys.stdout.write(str)
    sys.stdout.flush()


if __name__ == "__main__":
    # execute only if run as a script
    main()
