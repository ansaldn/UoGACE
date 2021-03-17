from scipy.spatial import distance as dist

import cv2


source = cv2.imread("/home/ravi/collection/Image_16.jpg")
source = cv2.calcHist(source, [0,1,2], None , [8,8,8], [0, 256, 0, 256, 0, 256])
source = cv2.normalize(source,source).flatten()
dest = cv2.imread("/home/ravi/collection/Image_7.jpg")
dest = cv2.calcHist(dest, [0,1,2], None , [8,8,8], [0, 256, 0, 256, 0, 256])
dest = cv2.normalize(dest,dest).flatten()
getdistance = dist.cityblock(source,dest)
print("distance",getdistance*100)
