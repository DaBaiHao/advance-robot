#!/usr/bin/env python
import rospy
from std_msgs.msg import String,Float32
import random


def talker():
    pub = rospy.Publisher('square_size_generator', Float32, queue_size = 10)
    rospy.init_node('square_size_generator', anonymous=True)
    rate = rospy.Rate(0.1) 
    while not rospy.is_shutdown():
        row = random.uniform(0.05,0.20)
        rospy.loginfo(row)
        pub.publish(row)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
