#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtle_pub.srv import DrawCircle, DrawCircleResponse
from turtlesim.srv import TeleportAbsolute

def handle_draw_circle(req):
    rospy.loginfo("Drawing circle at (%f, %f) with radius %f", req.x, req.y, req.radius)
    
    # Teleport to the specified location
    teleport = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
    teleport(req.x, req.y, 0)  # Assuming 0 orientation

    # Start drawing the circle
    draw_circle(req.radius)
    
    return DrawCircleResponse(True)

def draw_circle(radius):
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    # Calculate the linear and angular velocity to draw a circle
    linear_velocity = radius
    angular_velocity = 1.0  # You can adjust this value for different circle speeds

    twist = Twist()
    twist.linear.x = linear_velocity
    twist.angular.z = angular_velocity

    # Publish the Twist message
    for _ in range(360):  # Assuming 1 degree per iteration
        pub.publish(twist)
        rate.sleep()

if __name__ == "__main__":
    rospy.init_node('draw_circle_server')
    s = rospy.Service('draw_circle', DrawCircle, handle_draw_circle)
    rospy.spin()