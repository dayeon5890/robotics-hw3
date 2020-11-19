#!/usr/bin/env python
import rospy
from common_msgs.srv import DivTwoNum, DivTwoNumResponse

def service_callback(request):
    response = DivTwoNumResponse(div=request.a - request.b)
    print "request data:", request.a, request.b, ", response:", response.div
    return response

rospy.init_node('service_server')
service = rospy.Service('div_two_number', DivTwoNum, service_callback)
rospy.spin()
