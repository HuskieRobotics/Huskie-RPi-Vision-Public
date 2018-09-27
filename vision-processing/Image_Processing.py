##This file processes the stream of images
import cv2
import time
import numpy as np


###Set these to your preferred ranges for HSV based on the data you collected from the Testing Suite
lowerC = np.array([10,50, 20],np.uint8)
upperC = np.array([75, 255, 93],np.uint8)

def process_image(image):
    originalImage=image
    
    totalArea,ratioArea,centerX,centerY,width,height,rectangles = 0,0,0,0,0,0,0
    #Initialize all the data you are going to collect to 0. This ensures that if the target is not detected, it will return 0 and not an error
    #ex. targetX,targetY,Area = 0,0,0

    #using hsv to threshold is recommended, the inRange function basically cuts out all colors that arent wanted
    hsvFrame = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    newFrame = cv2.inRange(hsvFrame,lowerC,upperC)
    #cv2.imshow('b',newFrame) 
    a,contours,hierarchy = cv2.findContours(newFrame,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    #print len(contours)
    thresholdedFrame = cv2.inRange(hsvFrame, lowerC, upperC)
    #cv2.drawContours(originalImage,contours,-1,(255,165,0),3)
##    
    #cv2.imshow('a',newFr)
   # cv2.imshow('a',originalImage)
    try:
        rectangles = detectRectangles(newFrame)
        leftRectangle, rightRectangle = rectangleStats(rectangles)
    
        centerX,centerY = getCenter(leftRectangle,rightRectangle)
        
        ratioArea = getRatioArea(leftRectangle,rightRectangle)
        width = rightRectangle[0] - leftRectangle[0] +leftRectangle[2]
        height =(rightRectangle[3]+leftRectangle[3])/2.0
       # print (height)

       #approximate distance between camera and target (caluculated by using area and quadratic regression)
        distance=((0.0018524597*height*height)+(-1.08509246*height)+178.7074289)
       # print(height*(-1.5)+290)
        
        totalArea = width * height 
        
        ###operations on the frame come here, set all the variables to desired numbers based on contours and other things you find from the image
        ###ex. targetX = getX(thresholdedFrame)
        
    except Exception as e:
       # print e
        pass
    
    
    return totalArea,ratioArea,centerX,centerY,width,height,rectangles, distance

    ###Here return the data you have collected
    ###ex return targetX,targetY,Area
##    rectangles = detectRectangles(image)
##    leftRectangle, rightRectangle = rectangleStats(rectangles)
##    
##    centerX,centerY = getCenter(leftRectangle,rightRectangle)
##    ratioArea = getRatioArea(leftRectangle,rightRectangle)
##    width = rightRectangle[0] - leftRectangle[0] +leftRectangle[2]
##    height =(rightRectangle[3]+leftRectangle[3])/2.0
##    totalArea = width * height 
##    
##    return totalArea,ratioArea,centerX,centerY,width,height,rectangles





    
    


###SET THE REST OF YOUR FUNCTIONS AND OPERATIONS ON THE FRAME HERE









def processImage(image):

    rectangles = detectRectangles(image)
    leftRectangle, rightRectangle = rectangleStats(rectangles)
    
    centerX,centerY = getCenter(leftRectangle,rightRectangle)
    ratioArea = getRatioArea(leftRectangle,rightRectangle)
    width = rightRectangle[0] - leftRectangle[0] +leftRectangle[2]
    height =(rightRectangle[3]+leftRectangle[3])/2.0
    totalArea = width * height 
    
    return totalArea,ratioArea,centerX,centerY,width,height,rectangles

def calculations(frame):
    rectangles = detectRectangles(image)
    leftRectangle, rightRectangle = rectangleStats(rectangles)
    targetX,targetY = getCenter(leftRectangle,rightRectangle)
    targetW = rightRectangle[0] - leftRectangle[0] +leftRectangle[2]
    targetH =(rightRectangle[3]+leftRectangle[3])/2.0
    print (targetH)
    return (targetX, targetY, targetW, targetH)


def getRatioArea(leftRectangle,rightRectangle):
    return float(leftRectangle[2]*leftRectangle[3]) / float(rightRectangle[2]*rightRectangle[3])
    
def rectangleStats(rectangles):
    x,y,w,h = cv2.boundingRect(rectangles[0])
    x2,y2,w2,h2 = cv2.boundingRect(rectangles[1])
    if x<x2:
        leftRectangle = [x,y,w,h]
        rightRectangle = [x2,y2,w2,h2]
    else:
        leftRectangle = [x2,y2,w2,h2]
        rightRectangle = [x,y,w,h]
    return leftRectangle,rightRectangle


def getCenter(leftRectangle,rightRectangle):
    #x + w + x2 / 2.0 middle of two x coordinates
    centerX = float(leftRectangle[0]+leftRectangle[2]+rightRectangle[0])/2.0
    #2(y)+h +2(y2)+h2 / 4.0  average of the two height centers
    centerY = float((2*leftRectangle[1])+leftRectangle[3]+(2*rightRectangle[1])+rightRectangle[3])/4.0
    
    return centerX,centerY

    
def detectRectangles(image):
    a,contours,hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    rectangles = findRectangles(contours)
    rectangles = sorted(rectangles, key = cv2.contourArea,reverse=True)[:10]
    index = len(rectangles)-1
    print "Before:" , len(rectangles)
    while index>=0:
        
        cv2.imshow('b',image)
        
        x,y,w,h = cv2.boundingRect(rectangles[index])
        area= cv2.contourArea(rectangles[index])
       
        #checks if area is within reasonable range
        if area< 150  or area>15000:
            #print(area)
            #print ("Area Deletion")
            rectangles.pop(index)
         #checks for correct aspect ratiorectangles of the rectangles
        elif (abs(float(h)/w - 7.25) >4 ):
            #print ("Ratio Deletion", area)
            #print (abs(float(h)/w))
            rectangles.pop(index)
        #print("Length: ", len(rectangles))
            
        index-=1
    print "After:", len(rectangles)
##    if len(rectangles)>=1:
##        print (rectangles[0][3])
##        print (rectangles[1][3])
    #moved this frm the top on 3/10/18
    cv2.drawContours(image,rectangles,-1,(24,255,0),3)
    cv2.imshow('c',image)
    return rectangles


def findRectangles(contours):
    returnList = []
    for r in contours:
        returnList.append(np.int0(cv2.boxPoints(cv2.minAreaRect(r))))
    return returnList









#things to try

#Finding contours : foo, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Finding rectangles around contour : rectangle = np.int0(cv2.boxPoints(cv2.minAreaRect(contour)))
#Finding area of contour : area = cv2.contourArea(contour)


#USE THE INTERNET AND VAST AMOUNTS OF INFORMATION TO FIGURE OUT WHICH CV2 FUNCTIONS
#YOU NEED TO USE IN ORDER TO GET THE DATA YOU WANT, OUR GITHUB HAS MANY USEFUL LINKS
