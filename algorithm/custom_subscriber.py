#!/usr/bin/env python
import rospy
from common_msgs.msg import point_vector

def callback(msg):
    print "subscribe:", msg.point.x, msg.point.y , msg.point.z

rospy.init_node('custom_subscriber')
sub = rospy.Subscriber('common_msgs', point_vector, callback)
rospy.spin()
