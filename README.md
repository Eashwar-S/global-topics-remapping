# Remapping global topics in ROS

The python file "change_name.py" goes through all the .py and .cpp in the workspace and replaces absolute declaration of subscriber or publisher i.e "/topic_name" to relative path "topic_name". This will allow to add namespaces to global ROS topics.

## TODO 
Need to extend this global parameters.

## Usage
Place the change_name.py Python file in the directory above the source files and provide the directory path of the source files inside the code.
```
$ git clone https://github.com/Eashwar-S/global-topics-remapping.git
$ mv change_name.py test_ws/
$ cd test_ws/
$ pwd
/home/ros/Desktop/global-topics-remapping/test_ws
```
Provide the pwd + '/src' as the folder path inside the change_name.py file.