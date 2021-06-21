# import the necessary packages
import numpy as np
import cv2

# load the image
webcam = cv2.VideoCapture("http://10.0.0.202:8081")

# define the list of boundaries
# boundries color BGR not RGB
boundaries = [
    ([50, 40, 100],     [100, 60, 255]),		# red pos:  00 01
    ([86, 31, 0],       [255, 120, 50]),		# blue      10 11
    ([50, 120, 0],      [150, 255, 135]),       # green     20 21
    ([0, 205, 205],     [185, 255, 255]),  	    # yellow    30 31
    ([0, 80, 240],      [160, 160, 255]),  	    # orange    40 41
    ([215, 215, 215],   [255, 255, 255])        # white     50 51
]

pos = 0
side = np.zeros(shape=(3, 3))  # emty array with 0
side.fill(-1)  # fill with -1

detectedfields = 0


#returns the name of the color
def getColorName(color):
    if(color == boundaries[0][1]):
        return "red"
    if(color == boundaries[1][1]):
        return "blue"
    if(color == boundaries[2][1]):
        return "green"
    if(color == boundaries[3][1]):
        return "yellow"
    if(color == boundaries[4][1]):
        return "orange"
    if(color == boundaries[5][1]):
        return "white"


def fillSideArray(color, posx, posy):
    if(color == boundaries[0][1]):
        side[posx][posy] = 0
    if(color == boundaries[1][1]):
        side[posx][posy] = 1
    if(color == boundaries[2][1]):
        side[posx][posy] = 2
    if(color == boundaries[3][1]):
        side[posx][posy] = 3
    if(color == boundaries[4][1]):
        side[posx][posy] = 4
    if(color == boundaries[5][1]):
        side[posx][posy] = 5


def checkfields(detectedfields):
    if(detectedfields == 9):
        return True
    return False
    

def findColorSquares(mask, imageFrame, color):
    global detectedfields
    # Konturen finden
    cnts = cv2.findContours(mask.copy(),
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    # Draw Rectangle if detected a color square
    for pic, contour in enumerate(cnts):
        area = cv2.contourArea(contour)
        if(area > 750):
            x, y, w, h = cv2.boundingRect(contour)
            ar = w / float(h)  # ar = aspect ratio
            
            # if the same color is detected in a almost square (80% - 120%)
            if(ar >= 0.8 and ar <= 1.2):
                imageFrame = cv2.rectangle(
                    imageFrame, (x, y), (x + w, y + h), (255, 255, 0), 2)
                cv2.putText(imageFrame, getColorName(color), (x+int(w/2)-20, y+int(h/2)),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.33, (0, 0, 0))
                
                detectedfields += 1
            
            # if 2 fields are next to each other
            elif(ar >= 2 * 0.8 and ar <= 2 * 1.2):
                imageFrame = cv2.rectangle(
                    imageFrame, (x, y), (x + w, y + h), (255, 255, 0), 2)
                cv2.putText(imageFrame, getColorName(color), (x+int(w/2)-20, y+int(h/2)),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.33, (0, 0, 0))

                detectedfields += 2

    return imageFrame


def main():
    while(1):
        global detectedfields
        detectedfields = 0
        
        _, imageFrame = webcam.read()
        for boundary in boundaries:

            # create NumPy arrays from the boundaries
            lower = np.array(boundary[0], dtype="uint8")
            upper = np.array(boundary[1], dtype="uint8")

            # find the colors within the specified boundaries and apply
            # the mask
            mask = cv2.inRange(imageFrame, lower, upper)
            output = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

            imageFrame = findColorSquares(mask, imageFrame, boundary[1])



        if ( checkfields(detectedfields) == True):
            print("All fields detected!")



        # detection of single biggest Area with same mask (color)
        # if len(cnts) > 0:
        #     area_cords = max(cnts, key=cv2.contourArea)  # coordinates of rectangle
        #     (xg, yg, wg, hg) = cv2.boundingRect(area_cords)
        #     cv2.rectangle(output, (xg, yg), (xg+wg, yg+hg), (0, 255, 0), 2)

        # output red mask
        # lower = np.array(boundaries[0][0], dtype="uint8")
        # upper = np.array(boundaries[0][1], dtype="uint8")
        # mask = cv2.inRange(imageFrame, lower, upper)
        # output = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

        # show the video
        cv2.imshow("images", np.hstack([imageFrame, output]))

        # cv2.waitKey(0)
        if cv2.waitKey(10) & 0xFF == ord('n'):
            pos += 1
            if pos > 5:
                pos = 0

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
