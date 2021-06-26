# import the necessary packages
import numpy as np
import cv2

# load the image
webcam = cv2.VideoCapture("http://10.0.0.202:8081")



def main():
    while(1):

        ret, imageFrame = webcam.read()

        img_gray = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img_gray, 65, 255, cv2.THRESH_BINARY)

        contours = cv2.findContours(thresh.copy(),
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]

        max_area = 0

        # Draw Rectangle if detected a color square
        for pic, contour in enumerate(contours):
            contours, hierarchy = cv2.findContours(
                thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


            area = cv2.contourArea(contour)
            if(area > max_area):
                max_area = area
                _, _, w, h = cv2.boundingRect(contour)

                ar = w / float(h)  # ar = aspect ratio

                 # if the same color is detected in a almost square (80% - 120%)
                if(ar >= 0.95 and ar <= 1.05):
                    x, y, w, h = cv2.boundingRect(contour)

        if max_area > 750:
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (255, 255, 0), 2)


        # show the video
        cv2.imshow("images", imageFrame)
        cv2.imshow("image gray", thresh)



        

    #cv2.waitKey(0)
        if cv2.waitKey(10) & 0xFF == ord('n'):
            pos += 1
            if pos > 6:
                pos = 0

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
