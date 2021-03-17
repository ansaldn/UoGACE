#Created By: Ravi Kumar
#Date Created: 10/03/2021
#Version 1
#Description : Calculates the dimension of object in a image based on cameras feild of view

#importing all the dependicies
from scipy.spatial import distance as dist
import numpy as np
import cv2

#define midpoint
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)


def x_cord_contour(contours):
    # gives x co ordinates for center contoure
    if cv2.contourArea(contours)>10:
        A = cv2.moments(contours)
        return(int(A['m10']/A['m00']))



# read image turn it into grayscale and blur it using gaussian low pass filter
#add the directory and name of image
image = cv2.imread("/home/ravi/OD/test/Image_1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)


# detect edge , dilate nad erode the image and close gaps between object
corner = cv2.Canny(gray, 50, 100)
corner = cv2.dilate(corner, None, iterations=5)
corner = cv2.erode(corner, None, iterations=3)

# find contours 
contours, hierarchy = cv2.findContours(corner.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

cntrs_sort = sorted(contours, key = x_cord_contour, reverse = False)
pixelsPerMetric = None

# loop over the contours 
for a in cntrs_sort:
	# if contour is not big enough, ignore it
	if cv2.contourArea(a) < 100:
		continue

	# calculating the box for the image
	orig = image.copy()
	box = cv2.minAreaRect(a)
	box = cv2.boxPoints(box) 
	box = np.array(box, dtype="int")
	
	
	#draw the contours
	cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

	for (x, y) in box:
		cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

	# calculate the midpoint betweel top left and top right & bottom left and bottom right of the contour
	(tl, tr, br, bl) = box
	(Xtltr, Ytltr) = midpoint(tl, tr)
	(Xblbr, Yblbr) = midpoint(bl, br)

	# calculate the mid point between top left and bottom left then topright and bottom right 
	(Xtlbl, Ytlbl) = midpoint(tl, bl)
	(Xtrbr, Ytrbr) = midpoint(tr, br)

	# cmark mid point on the images
	cv2.circle(orig, (int(Xtltr), int(Ytltr)), 3, (0, 0, 255), -1)
	cv2.circle(orig, (int(Xblbr), int(Yblbr)), 3, (0, 0, 255), -1)
	cv2.circle(orig, (int(Xtlbl), int(Ytlbl)), 3, (0, 0, 255), -1)
	cv2.circle(orig, (int(Xtrbr), int(Ytrbr)), 3, (0, 0, 255), -1)

	# connect the mid points
	cv2.line(orig, (int(Xtltr), int(Ytltr)), (int(Xblbr), int(Yblbr)),
		(255, 0, 255), 2)
	cv2.line(orig, (int(Xtlbl), int(Ytlbl)), (int(Xtrbr), int(Ytrbr)),
		(255, 0, 255), 2)

	# calculate euclideam distance between the mid points 
	distA = dist.euclidean((Xtltr, Ytltr), (Xblbr, Yblbr))
	distB = dist.euclidean((Xtlbl, Ytlbl), (Xtrbr, Ytrbr))

	# when no pixel matric data is availible , calculating matric data as the ratio to 	distance of field of view of camera 

	if pixelsPerMetric is None:
		pixelsPerMetric = distB / 1

	# compute the size of the object
	dimA = distA / pixelsPerMetric
	dimB = distB / pixelsPerMetric
	
	#text to show the dimensions
	cv2.putText(orig, "Width : {:.1f}in".format(dimA),
		(15,30), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
	cv2.putText(orig, "Height: {:.1f}in".format(dimB),
		(15,60), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
             
    # show the output image
	cv2.imshow("Image", orig)
	cv2.waitKey(0)
    
cv2.destroyAllWindows()
