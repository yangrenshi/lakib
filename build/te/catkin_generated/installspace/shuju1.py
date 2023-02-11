#！/usr/bin/env python
#coding=utf-8

import rospy
from sensor_msgs.msg import LaserScan

def cb(data):
	a = 90*4
	dist = data.ranges[a]
	rospy.loginfo(f"前方测{a/4}度的距离为 : {dist}米" )

if __name__ == "__main__" :
    rospy.init_node('ske')
    rospy.Subscriber('scan',LaserScan,cb)
    rospy.spin()
