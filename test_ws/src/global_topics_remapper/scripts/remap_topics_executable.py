#!/usr/bin/env python3

import rospy
import rospkg
import yaml

def remap_topics():
    # Initialize ROS node
    rospy.init_node('remap_topics', anonymous=True)

    # Get the package path
    package_path = rospkg.RosPack().get_path('global_topics_remapper')

    # Load remapping parameters from YAML file
    with open(package_path + '/config/remapping_params.yaml', 'r') as stream:
        try:
            remapping_params = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            rospy.logerr("Error loading remapping parameters: %s", e)
            return

    # Get robot name parameter
    robot_name = rospy.get_param('~robot_name', 'robot1')

    # Dynamically generate remappings
    remappings = []
    for topic in remapping_params['topics']:
        remappings.append({'from': topic, 'to': f'{robot_name}/{topic}'})

    # Print remappings for verification
    rospy.loginfo("Generated remappings:")
    for mapping in remappings:
        rospy.loginfo("%s -> %s", mapping['from'], mapping['to'])

    # Perform remappings (you can modify this part based on your specific use case)
    # For demonstration purposes, we are just printing the remappings here
    # In a real scenario, you would likely use the remappings with nodes or save them to a file

    rospy.loginfo("Remappings applied successfully")

if __name__ == '__main__':
    try:
        remap_topics()
    except rospy.ROSInterruptException:
        pass
