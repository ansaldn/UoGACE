#Created By RAvi Kumar
#Date : 01/03/2021
#Version:1
#Description: Converting All pictures in a Folder to a same resoultion for tensorflow training purpose
#Importing sevral images from Python Imaging Library
from PIL import Image
import os, sys

#declaring diectory of the images
directory = "/home/ravi/OD/dataset/"
dirs = os.listdir( directory )

#resizes images to the set parameters and rewrite the images with resized followed by counting
#the resized image is saved in jpg or JPEG format
def resize():
    a = 0 
    for image in dirs:
	#loop to open each image using pil then resize and saves it

        if os.path.isfile(directory+image):
            im = Image.open(directory+image)
            f, e = os.path.splitext(directory+image)
            imResize = im.resize((720,576), Image.ANTIALIAS)
            imResize.save('Image_'+str(a)+'.jpg', 'JPEG', quality=90)
            a=a+1
            print("resizedimage " + str(a))

resize()
