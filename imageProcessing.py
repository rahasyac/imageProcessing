# Name : FNU Rahasya Chandan
# UTA Id: 1000954962
#: Image Processing

import numpy as np 
import matplotlib.pyplot as plt # matlab plotting in python
from PIL import Image # Open Image
from scipy import ndimage # Image manupilation and processing

# function to display orginal image
def origIm(image, title, number):
    plt.figure(number) # Create a new figure
    plt.title(title) # set the title for the current axis
    plt.imshow(image, cmap = "gray")
    plt.show()
    
# function to display Blur with lowFilter image
def blur(image, title, number):
    plt.figure(number) # Create a new figure
    plt.title(title) # set the title for the current axis
    blur_movavg = np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]) #10-point moving average with value of 0.1
    result_arr = []
    
    for line in range(len(image)):
        result = np.convolve(image[line,:], blur_movavg)
        result_arr.append(result)
    plt.imshow(result_arr, cmap = "gray")
    plt.show()

# function to display edge detcetion with HighFilter image
def HPfilter(image, title, number):
    plt.figure(number) # Create a new figure
    plt.title(title) # set the title for the current axis
    HPfilter = np.array([1,-1]) # h[n] = {1, -1}
    result_arr = []
    
    for line in range(len(image)):
        result = np.convolve(image[line,:], HPfilter)
        result_arr.append(result)
    plt.imshow(result_arr, cmap = "gray")
    plt.show()

# function to open image file
def fileOpen(file):
    plt.figure(1)
    im = Image.open(file)
    imArray = np.array(im)
    im.close()
    return(imArray)
    plt.show()


boatIm = fileOpen("boat.512.tiff")
clockIm = fileOpen("clock-5.1.12.tiff")
professorIm = fileOpen("darinGrayNoise.jpg")
manIm = fileOpen("man-5.3.01.tiff")
tankIm = fileOpen("tank-7.1.07.tiff")

#display Original, Blur with lowFilter, edge detcetion with HighFilter for Boat Image 
origIm(boatIm, "Boat Image", 1)
blur(boatIm, "LowPass Filter", 2)
HPfilter(boatIm, "HighPass Filter", 3)

#display Original, Blur with lowFilter, edge detcetion with HighFilter for Clock Image 
origIm(clockIm, "Clock Image", 4)
blur(clockIm, "LowPass Filter", 5)
HPfilter(clockIm, "HighPass Filter", 6)

#display Original, Blur with lowFilter, edge detcetion with HighFilter for Man Image 
origIm(manIm, "Man Image", 7)
blur(manIm, "LowPass Filter", 8)
HPfilter(manIm, "HighPass Filter", 9)

#display Original, Blur with lowFilter, edge detcetion with HighFilter for Tank Image
origIm(tankIm, "Tank Image", 10)
blur(tankIm, "LowPass Filter", 11)
HPfilter(tankIm, "HighPass Filter", 12)

#display Original, Blur with lowFilter, edge detcetion with HighFilter for Professor Image 
origIm(professorIm, "Darin Gray", 13)
blur(professorIm, "LowPass Filter", 14)
# to remove salt and pepper noise to orginal image
plt.figure(15)
plt.title("Median Filter")
outputImage = ndimage.median_filter(professorIm, 5) # inputImage = professorIm 
plt.imshow(outputImage, cmap = "gray")
plt.show()

