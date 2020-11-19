#!/usr/bin/env python
import rospy
from common_msgs.srv import DivTwoNum, DivTwoNumRequest

rospy.init_node('service_client')
rospy.wait_for_service('div_two_number')
requester = rospy.ServiceProxy('div_two_number', DivTwoNum)
print "requester type:", type(requester), ", callable?", callable(requester)
rate = rospy.Rate(10)
count = 0
while count < 100:
    if count % 10 == 0:
        req = DivTwoNumRequest(a=count, b=count/2)
        res = requester(req)
        print count, "request:", req.a, req.b, "response:", res.div
    rate.sleep()
    count += 1
