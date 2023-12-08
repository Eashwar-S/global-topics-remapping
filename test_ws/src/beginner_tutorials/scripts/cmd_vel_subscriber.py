#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def cmd_vel_callback(data):
    rospy.loginfo("Received cmd_vel: Linear = %f, Angular = %f", data.linear.x, data.angular.z)

def cmd_vel_subscriber():
    # Initialize the ROS node
    rospy.init_node('cmd_vel_subscriber_node', anonymous=True)

    # Create a subscriber for the /cmd_vel topic
    rospy.Subscriber("cmd_vel", Twist, cmd_vel_callback)

    # Spin to keep the script from exiting
    rospy.spin()

if __name__ == '__main__':
    cmd_vel_subscriber()
