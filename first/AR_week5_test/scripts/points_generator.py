#!/usr/bin/env python


import rospy
from std_msgs.msg import String,Float32
from AR_week5_test.msg import cubic_traj_params
import random


def talker():
    # pub = rospy.Publisher('points_generator', String, queue_size=10)
    
    pub = rospy.Publisher('points_generator', cubic_traj_params, queue_size = 10)
    rospy.init_node('points_generator', anonymous=True)
    rate = rospy.Rate(1/20) # 10hz
    msg = cubic_traj_params()
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        msg.p0 = random.uniform(10,-10)
        msg.pf = random.uniform(10,-10)
        msg.v0 = random.uniform(10,-10)
        msg.vf = random.uniform(10,-10)
        msg.t0 = 0
        dt = random.uniform(5,10)
        msg.tf = msg.t0 + dt
        rospy.loginfo(msg)

        # pub.publish(p0)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
