#General Modules
import cv2
import time
import numpy as np
import socket

#PI Camera specific modules
from picamera.array import PiRGBArray
from picamera import PiCamera

#User created modules
import UDP_Client
from Image_Processing import process_image


def getVideo():


    debug = True
    
    #Initialize Camera Stream
    camera = PiCamera()
    camera.resolution=(320,240)
    rawCapture = PiRGBArray(camera,size=(320,240))
    time.sleep(.5)
    ##camera.exposure_mode= 'sports'
    
    #These values are subject to change, use the Testing Suite to determine what range of values you want
    camera.brightness = 24
    
    camera.shutter_speed = 1000
    #print camera.shutter_speed
   # print camera.exposure_speed
   # print camera.framerate
    rawCapture.truncate(0)


    ###Edit the line below and change the IP address to your robot's ip (i.e. "10.30.61.17"), port is an arbitrary number
    #client = UDP_Client.Client("169.254.203.162",3807) #(IP,PORT)
    client = UDP_Client.Client("10.30.61.2",3807) #(IP,PORT)

    #frame_time is a pretty precise way of getting the timestamp of your image if you need it
    frame_time = time.time()
    init_time = time.time()
    frames = 0

    if debug == True:
        log = open("log.txt", "w")
        log.close()
    lastLenRectangles = 0
    for frame in camera.capture_continuous(rawCapture,format = 'rgb',use_video_port = True):
        image = frame.array
        
        
        ###DO YOUR PROCESSING HERE USING OpenCV and the image variable
        ###Refer to the Image Processing module and call its function process_image here
        centers, heights, areaRatios, allHeights, allWidths, newImage =process_image(image)
        #centers, heights, areaRatios, allHeights, allWidths, newImage = [], [], [], [], [], image
                
        ###Input your data and tags into the list below to send data to the rio
        ###This data is converted to a json string FYI, makes the sending faster
        lenRectangles = len(centers)
        client.sendData({"CenterXs":centers, "Heights":heights,"RatioAreas":areaRatios,"LenRectangles":lenRectangles,"AllHeights":allHeights,"AllWidths":allWidths})
        
        #this trunctates the stream of images to grab the current image
        rawCapture.truncate(0)
        #frame_time = time.time()
##        runtime = frame_time - currentTime
        #fps = frames / runtime
        #print fps
        frames += 1

        last_time = frame_time
        frame_time = time.time()
        framerate_time = frame_time - init_time
        fps = frames / framerate_time
        timeDifference = frame_time - last_time

        if debug == True:
            log = open("log.txt", "a")
            logData = "Frame: " + str(frames) + " Timestamp: " + str(frame_time) + " Seconds since last log: " + str(timeDifference)
            logData +=  " Number of Targets: " + str(lenRectangles) + " Heights: " + str(heights)
            logData += " RatioAreas: " + str(areaRatios) + " CenterXs: " + str(centers)
            logData += " Framerate: " + str(fps)
            log.write(logData)
            
            
            if (lastLenRectangles == 0 and lenRectangles > 0) and frames > 1:
                path = "/home/pi/Huskie-Vision/setup/StoredImages/"
                path2 = "/home/pi/Huskie-Vision/setup/StoredImagesRaw/"
                filename1 = path + str(frames) + "BeforeWithoutRectangles" + ".jpg"
                filename2 = path + str(frames) + "AfterWithRectangles" + ".jpg"
                filename3 = path2 + str(frames) + "BeforeWithoutRectanglesRaw" + ".jpg"
                filename4 = path2 + str(frames) + "AfterWithRectanglesRaw" + ".jpg"

                log.write(" Filename 1: " + filename1 + " Filename 2: " + filename2)
                cv2.imwrite(filename1, lastImage)
                cv2.imwrite(filename2, newImage)
                cv2.imwrite(filename3, lastRawImage)
                cv2.imwrite(filename4, image)
            elif (lastLenRectangles > 0 and lenRectangles == 0) and frames > 1:
                path = "/home/pi/Huskie-Vision/setup/StoredImages/"
                path2 = "/home/pi/Huskie-Vision/setup/StoredImagesRaw/"
                filename1 = path + str(frames) + "BeforeWithRectangles" + ".jpg"
                filename2 = path + str(frames) + "AfterWithoutRectangles" + ".jpg"
                filename3 = path2 + str(frames) + "BeforeWithRectanglesRaw" + ".jpg"
                filename4 = path2 + str(frames) + "AfterWithoutRectanglesRaw" + ".jpg"
                log.write(" Filename 1: " + filename1 + " Filename 2: " + filename2)
                cv2.imwrite(filename1, lastImage)
                cv2.imwrite(filename2, newImage)
                cv2.imwrite(filename3, lastRawImage)
                cv2.imwrite(filename4, image)
            lastLenRectangles = lenRectangles
            lastImage = newImage
            lastRawImage = image
            log.write("\n")
            log.close()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        


getVideo()
