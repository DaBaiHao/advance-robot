#!/usr/bin/env python


import rospy
from std_msgs.msg import String,Float32
from AR_week5_test.msg import cubic_traj_params,cubic_traj_coeffs
from AR_week5_test.srv import *

send = cubic_traj_coeffs()
def compute_cubic_coeffs_client(p0,pf,v0,vf,t0,tf):
    rospy.wait_for_service('compute_cubic_coeffs')
    try:
        compute_cubic_coeffs_1 = rospy.ServiceProxy('compute_cubic_coeffs', compute_cubic_traj)
        request = compute_cubic_trajRequest(p0,pf,v0,vf,t0,tf)
        a = compute_cubic_coeffs_1(request)
        print (a.a0)
        send.a0 = a.a0
        send.a1 = a.a1
        send.a2 = a.a2
        send.a3 = a.a3
        send.t0 = t0
        send.tf = tf

        
        
        return a.a0
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %.2f', data.t0)
    # msg = compute_cubic_traj()
    p0 = data.p0
    pf = data.pf
    v0 = data.v0
    vf = data.vf
    t0 = data.t0
    tf = data.tf
    
    data1 = compute_cubic_coeffs_client(p0,pf,v0,vf,t0,tf)
    talker()
    print(data1)
    # pt = a0 + a1*t + a2*t^2 + a3*t^3
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('cubic_traj_planner', anonymous=True)

    rospy.Subscriber('points_generator', cubic_traj_params, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def talker():
    pub = rospy.Publisher('cubic_traj_planner', cubic_traj_coeffs, queue_size = 10)
    rospy.init_node('cubic_traj_planner', anonymous=True)
    rate = rospy.Rate(1/20)
    msg = send
    
    rospy.loginfo(msg)
    pub.publish(msg)
    rate.sleep()






if __name__ == '__main__':
    listener()
    