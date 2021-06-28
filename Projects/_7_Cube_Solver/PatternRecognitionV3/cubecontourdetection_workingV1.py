# detects the cube and draw square around it  (dark background)
# import the necessary packages
from CubeSide import CubeSide
import numpy as np
import cv2

# load the image
webcam = cv2.VideoCapture("http://10.0.0.202:8081")
saveImage = True
cube_side = CubeSide()

# returns mask from grayscaled imageFrame
def get_graymask(imageFrame):
    img_gray = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 65, 255, cv2.THRESH_BINARY)
    return thresh


# returns the position, size and the area of the cube (x,y,w,h,area)
def find_cube(thresh):
    x = 0
    y = 0
    w = 0
    h = 0
    contours = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )[-2]

    max_area = 0
    # Draw Rectangle if detected a color square
    for pic, contour in enumerate(contours):
        contours, hierarchy = cv2.findContours(
            thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )

        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            _, _, w, h = cv2.boundingRect(contour)

            ar = w / float(h)  # ar = aspect ratio

            # if the same color is detected in a almost square (80% - 120%)
            if ar >= 0.95 and ar <= 1.05:
                x, y, w, h = cv2.boundingRect(contour)

    return x, y, w, h, max_area


# draws square around the cube to the image frame
def draw_cube_contours(imageFrame):
    global saveImage
    thresh = get_graymask(imageFrame)
    x, y, w, h, area = find_cube(thresh)

    if area > 1000:
        # to save image only once and do not override it every time
        if saveImage == True:
            cv2.imwrite("cube.jpg", imageFrame)
            cube_side.extract_cube_colors("cube.jpg", x, y, w, h)
            cube_side.print_arr()
            saveImage = False

        # print("Rectpos: x: {0} | y: {1} |w: {2} | h: {3}".format(x, y, w, h))
        imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    return imageFrame


def main():
    while 1:

        ret, imageFrame = webcam.read()
        graymask = get_graymask(imageFrame)
        imageFrame = draw_cube_contours(imageFrame)
        # show the video
        cv2.imshow("images", imageFrame)
        cv2.imshow("image gray mask", graymask)

        # cv2.waitKey(0)
        if cv2.waitKey(10) & 0xFF == ord("n"):
            pos += 1
            if pos > 6:
                pos = 0

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
