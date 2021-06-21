import cv2

img = cv2.imread("cube.jpg", -1)
cv2.imshow("image", img)
key = cv2.waitKey(0) & 0xFF

if key == 27:
    cv2.destroyAllWindows()
elif key == ord("s"):
    cv2.imwrite("cube_copy.jpg", img)
    cv2.destroyAllWindows()
    