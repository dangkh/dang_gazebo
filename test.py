#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import sys
import cv2
from cv_bridge import CvBridge, CvBridgeError
import matplotlib.pyplot as plt

now = False

def callback(data):
    try:
      cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
    
    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)
    
    cv2.imshow("Image window", cv_image)
    cv2.waitKey(1100)
    plt.imshow(cv_image)
 
  

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    # counter = 0
    # # while now == False:
    # #   counter+=1
    # #   print("now: ",now, "run times: ", counter)
    # #   rospy.Subscriber("/image_raw_dang", Image, callback)
    # #   if now: return
    # data = None
    # while counter <= 200 and data == None:
    #   counter += 1
    #   data = rospy.wait_for_message("/image_raw_dang", Image, timeout=5)
    #   callback(data)
    # spin() simply keeps python from exiting until this node is stopped
    # rospy.spin()
    for i in range(100):


if __name__ == '__main__':
    listener()
