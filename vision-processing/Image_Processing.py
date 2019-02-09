##This file processes the stream of images
import cv2
import time
import numpy as np
import math
# from imutils import perspective



###Set these to your preferred ranges for HSV based on the data you collected from the Testing Suite
lowerC = np.array([10,50, 20],np.uint8)
upperC = np.array([75, 255, 93],np.uint8)

def process_image(image, showImages):
    originalImage=image
    originalImage2 = image
    
    totalArea,ratioArea,centerX,centerY,width,height,rectangles,distance = 0,0,0,0,0,0,0,0
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
    centers = []
    heights = []
    areaRatios = []
    allWidths = []
    allHeights = []
    newImage = image
    try:
        rectangles, origContours, newImage = detectRectangles(newFrame)
        if showImages:
            cv2.drawContours(originalImage2,rectangles,-1,(24,255,0),3)
            cv2.imshow("Post-processing", originalImage2)
            cv2.drawContours(originalImage,origContours,-1,(24,255,0),3)
        
            cv2.imshow("Original", originalImage)
        
        for i in range(0, len(rectangles), 2):
            lRect, rRect = rectangleStats([rectangles[i], rectangles[i+1]])
            centerX, centerY = getCenter(lRect, rRect)
            centers.append(centerX)
            areaRatio = getRatioArea(lRect, rRect)
            areaRatios.append(areaRatio)
            height = (rRect[3]+lRect[3])/2.0
            heights.append(height)
            allHeights.append(lRect[3])
            allHeights.append(rRect[3])
            allWidths.append(lRect[2])
            allWidths.append(rRect[2])
        #leftRectangle, rightRectangle = rectangleStats(rectangles)
    
        #centerX,centerY = getCenter(leftRectangle,rightRectangle)
        
        #ratioArea = getRatioArea(leftRectangle,rightRectangle)
        #width = rightRectangle[0] - leftRectangle[0] +leftRectangle[2]
        #height =(rightRectangle[3]+leftRectangle[3])/2.0
       # print (height*height)
        #totalArea = width * height
        #print height
       #approximate distance between camera and target (caluculated by using area and regression)
        #distance= 1474/height
       # print(height*(-1.5)+290)
       # print distance
       
        
        ###operations on the frame come here, set all the variables to desired numbers based on contours and other things you find from the image
        ###ex. targetX = getX(thresholdedFrame)
        
    except Exception as e:
       # print e
        pass
    
    return centers, heights, areaRatios, allHeights, allWidths, newImage 
    #return totalArea,ratioArea,centerX,centerY,width,height,rectangles,distance

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
    ###print (targetH)
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
##    cv2.drawContours(image,contours,-1,(24,255,0),3)
##    cv2.imshow('a',image)
    rectangles = findRectangles(contours)
    rectangles = sorted(rectangles, key = cv2.contourArea,reverse=True)[:10]
    index = len(rectangles)-1
    #####print "Before:" , len(rectangles)
    while index>=0:
        
        #########cv2.imshow('b',image)
        x,y,w,h = cv2.boundingRect(rectangles[index])
        area= cv2.contourArea(rectangles[index])
       
        #checks if area is within reasonable range
        # Previously area < 150, lowered to increase ability to pick up
        # rectangles from further distances

        if area< 25  or area>11000:
            #print(area)
            #print ("Area Deletion")
            rectangles.pop(index)
            
         #checks for correct aspect ratiorectangles of the rectangles
            #5 used to be 7.25
        elif (abs(float(h)/w - 5) >4 ):
            #print ("Ratio Deletion", area)
            #print (abs(float(h)/w))
            rectangles.pop(index)
            

        #print("Length: ", len(rectangles))
        index-=1
    # Remove rectangles if there are duplicates of an angle
    # Can only be one 14.5 degree angle and -14.5 degree angle
    # rectData contains a string for each rectangle that says
    # if it a left rectangle or a right rectangle
    rectData = []
    ####print rectangles
    xCords=[]
    for i in range(len(rectangles)):
        rectangle = rectangles[i]
        xCords.append(int(rectangle[0,0]))
    xCords.sort()
    sortedRectangles=[]
    for coordinate in xCords:
        for j in rectangles:
            if int(j[0,0])==coordinate:
                sortedRectangles.append(j)
                break
                
    rectangles=sortedRectangles
    for i in range(len(rectangles)):
        rectangle = rectangles[i]
        #first point is always bottom most and then goes clockwise from there
        x1= rectangle[0,0]
        y1= rectangle[0,1]
        
        x2= rectangle[1,0]
        y2= rectangle[1,1]

##        dx = x1-x2
##        dy = y1-y2
##
##        angle = math.acos((dy)/math.sqrt((dx**2)+(dy**2)))
##        if angle<0:
##            rectData.append("left")
##        else:
##            rectData.append("right")

        x3 = rectangle[2,0]
        y3= rectangle[2,1]

        distance1 =  math.sqrt(((x1-x2)**2)+((y1-y2)**2))
        
        distance2 =  math.sqrt(((x2-x3)**2)+((y2-y3)**2))

        if(distance1>distance2):
            rectData.append("right")
        else:
            rectData.append("left")
    # Remove stray rectangles, and narrow in on a specific vision target
    if rectData[0] == "right":
        rectData.pop(0)
        rectangles.pop(0)
    if rectData[-1] == "left":
        rectData.pop(-1)
        rectangles.pop(-1)
##    if len(rectangles) == 6:
##        rectangles.pop(0)
##        rectData.pop(0)
##        rectangles.pop(0)
##        rectData.pop(0)
##        rectangles.pop(-1)
##        rectData.pop(-1)
##        rectangles.pop(-1)
##        rectData.pop(-1)
##    if len(rectangles) == 4:
##        rect0, rect1 = rectangleStats([rectangles[0], rectangles[1]])
##        rect2, rect3 = rectangleStats([rectangles[2], rectangles[3]])
##        lcenterX = float(rect0[0]+rect0[2]+rect1[0])/2.0
##        rcenterX = float(rect2[0]+rect2[2]+rect3[0])/2.0
##        if abs(160-lcenterX) < abs(160-rcenterX):
##            rectangles.pop(-1)
##            rectangles.pop(-1)
##            rectData.pop(-1)
##            rectData.pop(-1)
##        else:
##            rectangles.pop(0)
##            rectangles.pop(0)
##            rectData.pop(0)
##            rectData.pop(0)
####        rectangle = rectangles[i]
####        leftMost = 1000
####        leftMostIndex = -1
####        secondLeftMost = 1000
####        secondLeftMostIndex = -1
####        for j in range(len(rectangle)):
####            if rectangle[j, 0] < leftMost:
####                secondLeftMost = leftMost
####                secondLeftMostIndex = leftMostIndex
####                leftMost = rectangle[j, 0]
####                leftMostIndex = j
####            elif rectangle[j, 0] < secondLeftMost:
####                secondLeftMost = rectangle[j, 0]
####                secondLeftMostIndex = j
####        if rectangle[leftMostIndex, 1] > rectangle[secondLeftMostIndex, 1]:
####            rectData.append(True)
####        else:
####            rectData.append(False)
    #####print rectData
    #####print "After:", len(rectangles)
##    if len(rectangles)>=1:
##        print (rectangles[0][3])
##        print (rectangles[1][3])
    #moved this frm the top on 3/10/18
    ###cv2.drawContours(image,rectangles,-1,(24,255,0),3)
    ###cv2.imshow('c',image)
    return rectangles, contours, image



def findRectangles(contours):
    returnList = []
    for r in contours:
        returnList.append(np.int0(cv2.boxPoints(cv2.minAreaRect(r))))
    return returnList









#things to try

#Finding contours : foo, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Finding rectangles around contour : rectangle = np.int0(cv2.boxPinAreaRect(contour)))
#Finding area of contour : area = cv2.contourArea(contour)


#USE THE INTERNET AND VAST AMOUNTS OF INFORMATION TO FIGURE OUT WHICH CV2 FUNCTIONS
#YOU NEED TO USE IN ORDER TO GET THE DATA YOU WANT, OUR GITHUB HAS MANY USEFUL LINKS
