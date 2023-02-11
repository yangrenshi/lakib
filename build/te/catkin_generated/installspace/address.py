#!/usr/bin/env python3
#coding=utf-8
import rospy
import math
from sensor_msgs.msg import LaserScan

def index(a,a_min,a_inc):
	return int(((a*math.pi)/180 - a_min)/a_inc)

def main():
	rospy.init_node('te')
	rospy.Subscriber('scan',LaserScan,cb,queue_size=10)
	rospy.spin()

def cb(data):
    scan_filter=[]
    for i in range(index(90,data.angle_min,data.angle_increment),index(135,data.angle_min,data.angle_increment)):  
        if data.ranges[i]*4 <=3.2:
            scan_filter.append(data.ranges[i]) 

    rospy.loginfo('distance:' + str(min(scan_filter)))
    # if min(scan_filter) < 0.2:



if __name__ == "__main__" :
    main()