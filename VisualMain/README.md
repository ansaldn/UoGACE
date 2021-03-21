# Visual Main
This section of the Github describes the sourcefiles required for object detection & tracking with the process & steps required to set up and configue your device.


## Table of Contents 
[Deliverables](#main-folder)

[How To Use Object & Multi Object Tracking](#how-to-track-multiple-objects)

[Dependancies](#dependancies)

[Dependancies](#development-stage-artifacts)

## Main folder
In the Main folder you will find:
<details><summary>2 Object Tracking</summary>
<p>

###  Tracking of 2 objects (2objectstrack.py)
This file is the core Source file for tracking multiple objects.





```python
print("hello world!")
```
</p>
</details>

<details><summary>Converting RGB Values to HSV Model</summary>
<p>

####  Converting RGB Values to HSV Model (RGBConvert.py)
This file is an executable file which enables users to convert RGB values to HSV model which enables them to be tracked by Python object tracking.

</p>
</details>

## How to Track Multiple Objects
<details><summary>Requirements</summary>
<p>
  
* Python 4 Enviroment with Open CV4.1.1 Installed

* 1x Serial Webcam

* Coloured Objects to track 

</p>
</details>


<details><summary>Steps</summary>
<p>

If you allready know the RGB variables of the two colours you would like to track please skip to step 6

1. Open the webcam.
2. Capture image using webcam or use Printscreen Keyboard Input to copy/save image.
3. Copy the image across to a Paint editor.
4. Use the select colour picker tool on the colour of the object you want to track.
5. Note the RGB value from the application
6. Navigate to RGB Convert.py
7. Using Pythin CLI Launch and enter the 3 RGB values as command line arguments seperated by 1 white space Example: RGBConvert.py 100 100 100
8. The program will respond with lower and upper bounds printed to the CLI interface.
9. Open One of the two Object Tracking Python scripts (objecttracking.py) for Tracking of 1 object & (2objectstrack.py) for Tracking of 2 objects. ..
for 2 Object Tracking you'll need to navigate to lines 24 -> 27 These Look like:

```python
object1Lower = (8, 100, 100)
object1Upper = (28, 255, 255)
carlower = (160, 100, 100)
carupper = (180, 255, 255)
```

10. Navigate to the lines which contain the HSV Colour model bounds for lower and upper bounds.
11. Enter the RGB Convert HSV Values into the required lines 
12. Save the Python Script
13. Return to the Python CLI and execute the program using Python 3

</p>
</details>



## Dependancies
<details><summary>Dependancies</summary>
<p>
  
### Nano install_opencv.sh
This file will install OpenCV and all dependencies with the rquired libraries. 

</p>
</details>

## Development Stage Artifacts
<details><summary>Development Stage Artifacts</summary>
<p>
  
### WebcamCV2.py
This file will open the USB Camera 2 (can be changed to other camera) by the use of OpenCV (Open Source Computer Vision Library). This represents a test file which will make sure that everyone's OpenCV is correctly installed. 
### NoWebcame AlternativeV2.py
An early stage derisking activity to support users if they dont have a usb webcame. 
### CameraTest.py
This is an early stage of project which opens the camera using openCV and converts the camera feed into grayscale and HSV and shows it on the screen
### colourshow.py
The file was used for demonstrative purposes in understanding masks and how OpenCV converts colours to masks. 
### RGBConvert.py
This file Converts BGR colour to HSV Colour with lower and upper bounds; output to be used within the colourshow.py file. 
The webcameCV2.py will be used to display the video on the screen and then a print screen functionallity will be used to take the RGB colour description of the object and use it for finding the HSV colours. 
### Resize.py
This file takes all the image in the directory and converts it to the same set resolution , this helps in image training in Tenserflow
### DimesionCalculation.py
This file calculates size of an object in an image based on the camera viewing angle using Euclidean geometry.

</p>
</details>
