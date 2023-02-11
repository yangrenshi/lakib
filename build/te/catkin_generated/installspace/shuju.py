#！/usr/bin/env python
#coding=utf-8

import rospy
from sensor_msgs.msg import LaserScan

def cb(data):
	a = 270
	for i in range(45,316):
		if data.ranges[i] != 0:
			dist = data.ranges[a]
			# if dist < 1:
			rospy.loginfo(f"前方测{a}度的距离为 : {dist}米" )

if __name__ == "__main__" :
    rospy.init_node('ske')
    rospy.Subscriber('scan',LaserScan,cb)
    rospy.spin()
