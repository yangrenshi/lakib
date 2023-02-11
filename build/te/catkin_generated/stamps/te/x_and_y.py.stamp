#! /usr/bin/env python
#coding=utf-8
 
import rospy
from sensor_msgs.msg import LaserScan
import struct
import serial
import math

def cb(msg):	
    # a = 180*4
    # dist = data.ranges[a]
    scan_filter = []
    # scan_angle = []
    for i in range(90,136):
        j = i*4
        dist = msg.ranges[j]
        if dist == 0:
            continue
        else: 
            if dist < 3.3:
                scan_filter.append(i)
                scan_filter.append(dist)
    rospy.loginfo(f"Distant={str(min(scan_filter))}和角度{str(scan_filter.index(min(scan_filter)-1))}")
    # if min(scan_filter) <3.3:
    #     dist1 = min(scan_filter)
    # x = dist1*math.cos(scan_filter.index(min(scan_filter)))
    # y = dist1 * math.sin(scan_filter.index(min(scan_filter)))
    # #rospy.loginfo(f"前方测{a/4}度的距离为 : {dist}米" )
    # temp = struct.pack("<BBff",0x2C,0x12,x,y)
    # rospy.loginfo(f"前方测的x和y为 : {x}和{y}米" )
    # ser.write(temp)
    #ser.write(str(a).encode("gbk"))


    
    # data1 = ustruct.pack("<bbhhffb",      #格式为俩个字符俩个短整型(2字节)
    #                     0x2C,                      #帧头1
    #                     0x12,                      #帧头2
    #                     int(x), # up sample by 4   #数据1
    #                     int(y), # up sample by 4    #数据2
    #                     # float(y), # up sample by 4    #数据1
    #                     # float(x), # up sample by 4    #数据2
    #                     0x5B)
        
        
if __name__ == "__main__" :
    port = '/dev/tty'  # 串口号
    baudrate = 9600  # 波特率
    ser = serial.Serial(port, baudrate, timeout=9)
    rospy.init_node('te')
    rospy.Subscriber('scan',LaserScan,cb)
    rospy.spin()
    ser.close()

# 90-135
# 对应1.5707963267948966-2.356194490192345