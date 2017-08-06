# Huskie-RPi-Vision-Public
Our teams template for future vision projects. Contains a variety of setup scripts that should be run to enable the camera and import OpenCV libraries. Also has a template for processing images via the Pi Camera and creating a UDP server. 


## Stuff to buy 

1. Buy a Raspberry Pi and Pi Camera v2 from [here](https://www.raspberrypi.org/products/)

2. Buy a case [here](https://www.amazon.com/Raspberry-Model-Protective-Heatsinks-Clear/dp/B01CDVSBPO/ref=sr_1_4?s=electronics&ie=UTF8&qid=1501820103&sr=1-4&keywords=raspberry+pi+case)

3. Buy a [camera case](https://www.amazon.com/Latest-Raspberry-Camera-Case-Megapixel/dp/B00IJZJKK4/ref=sr_1_2?s=electronics&ie=UTF8&qid=1501820315&sr=1-2&keywords=camera+case+raspberry+pi)

4. You'll also need a mini sd card (8GB +), you can buy this anywhere

5. Buy a [LED RING](http://www.andymark.com/product-p/am-3596.htm)

## Setup

1. Download Raspbian onto your personal computer: [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) or [Noobs](https://www.raspberrypi.org/downloads/noobs/) if you are less experienced with linux. I currently use NOOBS but Raspbian works the same.

2. Download [SD Formatter](https://www.sdcard.org/downloads/formatter_4/) and follow these [instructions](https://www.raspberrypi.org/documentation/installation/noobs.md)

3. Once your SD card is formatted and in the pi, you have two options: either use a monitor with mouse and keyboard to access pi or learn how to [SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/README.md)

4. Make sure your pi is connected to the internet and install git via ```sudo apt-get install git``` or follow these [instructions](https://www.raspberrypi.org/learning/getting-started-with-git/worksheet/)

5. Then fork this [repository](https://github.com/HuskieRobotics/Huskie-RPi-Vision-Public) and clone it. Instructions [here](https://guides.github.com/activities/forking/)... If you do not have access to the desktop/web browser you may just clone the repository.
To just clone use ```git clone https://github.com/HuskieRobotics/Huskie-RPi-Vision-Public```

6. Now run my setup file (it may take up to an hour to compile the opencv library, be patient). Use the command ```sh /home/pi/Huskie-RPi-Vision-Public/setup/Setup Script.sh```


## Programming Vision
1. Take a look at the vision files and fill in your code as necessary. There are a variety of comments that detail exactly how and where to write your code. 

2. Also make sure to use the Testing Suite to tune your camera using HSV, Brightness, ISO, etc. It contains trackbars that you can slide around to tune. 

## Important Links

Team 254 Vision Video SUPER HELPFUL: [here](https://www.team254.com/documents/vision-control/)

Learning about OpenCV: [here](http://docs.opencv.org/3.1.0/d2/d96/tutorial_py_table_of_contents_imgproc.html)

Learning about Contours: [here](http://docs.opencv.org/3.1.0/d3/d05/tutorial_py_table_of_contents_contours.html)

What is UDP: [here](http://searchmicroservices.techtarget.com/definition/UDP-User-Datagram-Protocol)

## 3D Printed Camera Cases

Our GrabCad Partner space has the files for all of this: [here](https://workbench.grabcad.com/workbench/projects/gcGE8V6qjJTC8MVGvCVHrsE53Zv-qneaUuiebfHzCsZ08G#/space/gcYgMNwN-ZOnUh87_eJl-JzqzF4mV5uck80jfpLCJ3wMqS)  This model actually has a spot for the LED ring to sit on. 


