#!/usr/bin/env python

import rospy
from std_msgs.msg import String,Float32

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %.2f", data.data)
    move_2_starting_configuration()


def move_2_starting_configuration():
    # defined in joints space as follows
    
    group_name = "panda_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    start_conf = move_group.get_current_joint_values()
    start_conf[0] = 0
    start_conf[1] = -pi/4
    start_conf[2] = 0
    start_conf[3] = -pi/2
    start_conf[4] = 0
    start_conf[5] = pi/3
    start_conf[6] = 0

    move_group.go(start_conf, wait=True)
    move_group.stop()

def plan_Cartesian_path(data):
    waypoints = []
    group = moveit_commander.MoveGroupCommander("panda_arm")
    # start with the current pose
    waypoints.append(group.get_current_pose().pose)
    wpose = geometry_msgs.msg.Pose()

    wpose.orientation.w = data.data
    #  move forward
    


def listener():
    
    rospy.init_node('move_panda_square', anonymous=True)
    
    rospy.Subscriber("square_size_generator", Float32, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()



