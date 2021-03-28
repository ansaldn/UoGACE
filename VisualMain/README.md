# Visual Main
This section of the Github describes the sourcefiles required for object detection & tracking with the process & steps required to set up and configue your device.


## Table of Contents 
[Deliverables](#main-folder)

[How To Use Object & Multi Object Tracking](#how-to-track-multiple-objects)

[Dependancies](#dependancies)

[Development Stage Artifacts](#development-stage-artifacts)

## Main folder
In the Main folder you will find:
<details><summary>2 Object Tracking</summary>
<p>

###  Tracking of 2 objects (2objectstrack.py)
This file is the core Source file for tracking multiple objects.

</p>
</details>

<details><summary>Converting RGB Values to HSV Model</summary>
<p>

####  Converting RGB Values to HSV Model (RGBConvert.py)
This file is an executable file which enables users to convert RGB values to HSV model which enables them to be tracked by Python object tracking.
A pixel is always represented by the three main colours -> RED, GREEN, BLUE (RGB); each of the colours may have a value between 0-255.
But when working with the environment of OpenCV and computer graphical representations, HSV colour model will be used. 
Hue, Saturation, Value (HUE) is the alternative way of representing the RGB colours when working with OpenCV therefore, to tack an object with certain colour the RGB to HSV code 
converter will be used to define the lower and upper bounds of the HSV model. 

Figures below show the difference between RGB and HSV colour models. 

RGB Model

![How to RGB Model](https://github.com/da5905p/UoGACE/blob/main/VisualMain/Images/RGB.png)

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

If RGB values of Object which you wish to track are allready known please skip to step 5.

1. Open the webcam you are using to do object detection 
We have supplied a file called WebcamCV2.py which can be found under the Visual Main Branch:VisualMain/DevelopmentStage/WebcamCV2.py
3. Capture image using webcam or use Printscreen Keyboard Input to save the image with desired Object Inside.
4. Copy the image across to a Paint editor.


**<details><summary>4. Paint RGB Explained</summary>**
<p>
  
1. Select the colour Picker tool
2. Click the Picker tool upon the object you wish  to track
3. Open the edit colours tool
4. Read the RGB Value of desired object 

![How to RGB Image](https://github.com/da5905p/UoGACE/blob/main/VisualMain/Images/How-to-get-RGB.png)

</p>
</details>

5. Navigate to RGB Convert.py With RGB values for Tracking
6. Using Pythin CLI Launch and enter the 3 RGB values as command line arguments seperated by 1 white space Example: RGBConvert.py 100 100 100

**<details><summary>Example execution of RGB Convert with Command line Arguments</summary>**
<p>
  
  The Script should be executed in the following format:
Python3 RGBconv.py Red_value Green_value Blue_value

![How to RGB Image2](https://github.com/da5905p/UoGACE/blob/main/VisualMain/Images/RGBConv.png)
  
  </p>
</details>
 
8. The program will respond with lower and upper bounds printed to the CLI interface. 
9. Enter these bounds into the Object decection file of choice for 2 Object Tracking you'll need to navigate to lines 24 -> 27.

***<details><summary>Bounds variables (Lines 24 --> 27)</summary>***
<p>
  
```python
object1Lower = (8, 100, 100)
object1Upper = (28, 255, 255)
carlower = (160, 100, 100)
carupper = (180, 255, 255)
```
</p>
</details>

12. Save the Python Script
13. Return to the Python CLI and execute the program using Python 3

</p>
</details>



## Dependancies
<details><summary>Dependancies</summary>
<p>
  To check sucessfull installation of opencv dependencies command 'jtop' in the CLI can be used 
  ![OpenCV](https://github.com/da5905p/UoGACE/blob/main/VisualMain/Images/dependancies.png)
  
  
  
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
This file takes all the image in the directory and converts it to the same set resolution , this helps in image training in Tenserflow. In 'line 24' of the source file the desired output resolution must be mentioned , the directory of the pictures must be mentioned in line 10 of the source code . 
### DimesionCalculation.py
This file calculates size of an object in an image based on the camera viewing angle using Euclidean geometry. The user must input the camera's field of view in meters in 'line 90' of the source file . 
### ForeignObjectDetection.Py
This file detects any foreign object introduced to the frame and save a snapshot of it in the set directory . The file runs with setting the initial frame as the base frame and then subtract the new frame from the  initial frame the difference in the frames is the object introduced to the frame , once an object is detected the base frame is updated to the new frame to detect any further changes . The user must set the direcory to save the detected object snapshot in 'line 72' of the source file . 


</p>
</details>
