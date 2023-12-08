#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def rotate_turtle():
    # Initialize the ROS node
    rospy.init_node('rotate_turtle_node', anonymous=True)

    # Create a publisher for the /cmd_vel topic
    cmd_vel_pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)

    # Set the publishing rate (10 Hz in this example)
    rate = rospy.Rate(10)

    # Create a Twist message to send linear and angular velocities
    twist_msg = Twist()

    # Set linear velocity (0.2 m/s)
    twist_msg.linear.x = 0.2

    # Set angular velocity (1 rad/s)
    twist_msg.angular.z = 1.0

    while not rospy.is_shutdown():
        # Publish the Twist message
        cmd_vel_pub.publish(twist_msg)

        # Sleep to maintain the specified publishing rate
        rate.sleep()

if __name__ == '__main__':
    try:
        rotate_turtle()
    except rospy.ROSInterruptException:
        pass
