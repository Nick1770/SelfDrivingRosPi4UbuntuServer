#! /usr/bin/python3

import rospy
from std_msgs.msg import String
import serial

def callback(data, ser):
	msg = data.data
	
	ser.write(msg.encode())
	print(msg)
if __name__ == '__main__':
	ser = serial.Serial("/dev/ttyS0", 115200)
	
	rospy.init_node('Serial_Publisher')
	control_listener = rospy.Subscriber("control_cmd", String, callback, (ser))
	rospy.spin()
