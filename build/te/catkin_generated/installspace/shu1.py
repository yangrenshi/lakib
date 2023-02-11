#!/usr/bin/env python3
#coding=utf-8
 
import rospy
from sensor_msgs.msg import LaserScan
import struct
import serial

def cb(data):	
    a = 180*4
    dist = data.ranges[a]
    #rospy.loginfo(f"前方测{a/4}度的距离为 : {dist}米" )
    temp = struct.pack("<BBf",0x2C,0x12,dist)
    #ser.write(temp)
    ser.write(str(a).encode("gbk"))
    #print(ser.is_open)
    
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
