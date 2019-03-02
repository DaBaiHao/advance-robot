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

    plan, fraction = plan_Cartesian_path(data)
    display_trajectory(plan)
    execute_plan(plan)

    
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

    waypoints = []
    scale = data.data
    wpose = group.get_current_pose().pose
    wpose.position.z -= scale * 0.1  # First move up (z)
    wpose.position.y += scale * 0.2  # and sideways (y)
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.y -= scale * 0.1  # Third move sideways (y)
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = group.compute_cartesian_path(
                                   waypoints,   # waypoints to follow
                                   0.01,        # eef_step
                                   0.0)         # jump_threshold
    return plan, fraction

def display_trajectory(plan):

    display_trajectory_publisher = rospy.Publisher('display_planned_path',
                                                    moveit_msgs.msg.DisplayTrajectory,
                                                    queue_size=20)
    robot = moveit_commander.RobotCommander()

    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = robot.get_current_state()
    display_trajectory.trajectory.append(plan)
    # Publish
    display_trajectory_publisher.publish(display_trajectory)

def execute_plan(plan):
    group_name = "panda_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    move_group.execute(plan, wait=True)

def listener():
    
    rospy.init_node('move_panda_square', anonymous=True)
    
    rospy.Subscriber("square_size_generator", Float32, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()



