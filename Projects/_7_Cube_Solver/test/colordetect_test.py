# import the necessary packages
import numpy as np
import argparse
import cv2



# load the image
image = cv2.imread("cube.jpg")

# define the list of boundaries

## boundries color BGR not RGB

boundaries = [
	([0, 0, 100], [80, 80, 255]),		# red
	([86, 31, 0], [255, 120, 50]),		# blue
	([50, 120, 0], [150, 255, 100]),	# green
  	([0, 205, 205], [185, 255, 255]),  	# yellow
	([0, 80, 240], [70, 130, 255]),  	# orange
	([220, 220, 220], [255, 255, 255])	# white
]

# loop over the boundaries
for (lower, upper) in boundaries:

	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype="uint8")
	upper = np.array(upper, dtype="uint8")

	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask=mask)
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
