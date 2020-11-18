#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point32
from common_msgs.msg import point_vector

rospy.init_node('custom_publisher')
pub = rospy.Publisher('common_msgs',point_vector, queue_size=1)
msg = point_vector()
rate = rospy.Rate(1)
count = 0.
while not rospy.is_shutdown():
    msg.timestamp.data = count % 2
    msg.point.x = msg.timestamp.data
    msg.point.y = msg.timestamp.data + 0.3
    msg.point.z = msg.timestamp.data + 0.8
    pub.publish(msg)
    print "publish:", msg.point.x,  msg.point.y, msg.point.z
    count += 1.3
    rate.sleep()
