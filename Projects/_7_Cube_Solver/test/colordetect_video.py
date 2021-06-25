# import the necessary packages
import numpy as np
import cv2


# load the image

webcam = cv2.VideoCapture("http://10.0.0.202:8081")

# define the list of boundaries

## boundries color BGR not RGB

boundaries = [
	([0, 0, 100],       [80, 80, 255]),		    # red pos:  00 01
	([86, 31, 0],       [255, 120, 50]),		# blue      10 11
	([50, 120, 0],      [150, 255, 100]),       # green     20 21
  	([0, 205, 205],     [185, 255, 255]),  	    # yellow    30 31
	([0, 80, 240],      [70, 130, 255]),  	    # orange    40 41
    ([0, 80, 240],      [70, 130, 255]),  	    # orange    40 41
	([220, 220, 220],   [255, 255, 255])        # white     50 51
]

pos = 0

while(1):

    _, imageFrame = webcam.read()

    # create NumPy arrays from the boundaries
    lower = np.array(boundaries[pos][0], dtype="uint8")
    upper = np.array(boundaries[pos][1], dtype="uint8")

    cv2.putText(imageFrame, "pos: {}".format(pos), (0,30),
                cv2.FONT_HERSHEY_COMPLEX,
                1.0, (255, 0, 0))

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(imageFrame, lower, upper)
    output = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

    # show the video
    cv2.imshow("images", np.hstack([imageFrame, output]))
    #cv2.waitKey(0)

    if cv2.waitKey(10) & 0xFF == ord('n'):
        pos += 1
        if pos > 6: pos = 0

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

