cmake_minimum_required(VERSION 3.0.2)
project(global_topics_remapper)
find_package(catkin REQUIRED COMPONENTS
  rospy
)

# catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS rospy
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# install(PROGRAMS
#   scripts/remap_topics_executable.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )
