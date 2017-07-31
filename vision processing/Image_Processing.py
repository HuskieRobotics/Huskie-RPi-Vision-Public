##This file processes the stream of images
import cv2
import time
import numpy as np


###Set these to your preferred ranges for HSV based on the data you collected from the Testing Suite
lowerC = np.array([40,75, 25])
upperC = np.array([70, 255, 190])

def process_image(image):
    #Initialize all the data you are going to collect to 0. This ensures that if the target is not detected, it will return 0 and not an error
    #ex. targetX,targetY,Area = 0,0,0

    #using hsv to threshold is recommended, the inRange function basically cuts out all colors that arent wanted
    hsvFrame = cv2.cvtColor(image, COLOR_RGV2HSV)
    thresholdedFrame = cv2.inRange(newFrame, lowerC, upperC)

    try:
        ###operations on the frame come here, set all the variables to desired numbers based on contours and other things you find from the image
        ###ex. targetX = getX(thresholdedFrame)
        
    except:
        pass

    ###Here return the data you have collected
    ###ex return targetX,targetY,Area
    return


###SET THE REST OF YOUR FUNCTIONS AND OPERATIONS ON THE FRAME HERE

#things to try

#Finding contours : foo, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Finding rectangles around contour : rectangle = np.int0(cv2.boxPoints(cv2.minAreaRect(contour)))
#Finding area of contour : area = cv2.contourArea(contour)


#USE THE INTERNET AND VAST AMOUNTS OF INFORMATION TO FIGURE OUT WHICH CV2 FUNCTIONS
#YOU NEED TO USE IN ORDER TO GET THE DATA YOU WANT, OUR GITHUB HAS MANY USEFUL LINKS
