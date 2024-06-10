#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

# Constants for the turtle's movements
LINEAR_VELOCITY = 1.0  # Reduced speed for better control
ANGULAR_VELOCITY = 1.0  # Angular velocity to make the turtle move in a circle

def turtle_controller():
    rospy.init_node("turtle_controller")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)  # Control rate: 10 Hz

    rospy.loginfo("Node has been started.")

    while not rospy.is_shutdown():
        msg = Twist()
        rospy.sleep(1)
        msg.linear.x = 5
        pub.publish(msg)
        rospy.sleep(2)
        msg.linear.x= 0
        msg.angular.z =1.57
        pub.publish(msg)
        rospy.sleep(2)
        msg.linear.x = 2*3.14*5
        msg.angular.z = 2*3.14
        pub.publish(msg)
        rospy.sleep()
        rate.sleep()

if __name__== '__main__':
    try:
        turtle_controller()
    except rospy.ROSInterruptException:
        pass