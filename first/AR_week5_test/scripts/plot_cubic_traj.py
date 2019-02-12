#!/usr/bin/env python

import rospy
from std_msgs.msg import String,Float32
from AR_week5_test.msg import cubic_traj_params,cubic_traj_coeffs,plot_data
# from AR_week5_test.srv import *
import matplotlib.pyplot as plt
import numpy as np
import std_msgs.msg as std_msgs




def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %.2f', data.t0)
    # msg = compute_cubic_traj()
    a0 = data.a0
    a1 = data.a1
    a2 = data.a2
    a3 = data.a3
    t0 = data.t0
    tf = data.tf
    T = tf - t0
    # position traj
    T = np.arange(t0,tf,0.01)
    p_traj = [a0 + a1*_T + a2*_T*_T + a3*_T*_T*_T for _T in T]
    # velocity trajectory
    v_traj = [a1 + 2*a2*_T + 3*a3*_T*_T for _T in T]
    # acceleration trajectory 
    a_traj = [2*a2+6*a3*_T for _T in T]
    # plt.figure(num=3,figsize = (8,5))
    # plt.figure(1)
    # plt.plot(T, p_traj)
    # plt.plot(T, v_traj)
    # plt.plot(T, a_traj)
    # p_traj = np.array(T, p_traj)
    # for i in np.arange(t0,tf,0.1):
    #     p_traj = a0 + a1*i + a2*i*i + a3*i*i*i
    #     # velocity trajectory
    #     v_traj = a1 + 2*a2*i + 3*a3*i*i
    #     # acceleration trajectory
    #     a_traj = 2*a2+6*a3*i

    #     try:
    #         talker(p_traj,v_traj,a_traj)
    #     except rospy.ROSInterruptException:
    #         pass
    talker(p_traj,v_traj,a_traj,t0,tf)
    print(data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('plot_cubic_traj', anonymous=True)

    rospy.Subscriber('cubic_traj_planner', cubic_traj_coeffs, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def talker(p_traj,v_traj,a_traj,t0,tf):
    pub = rospy.Publisher('plot', plot_data, queue_size = 10)
    rospy.init_node('plot_cubic_traj', anonymous=True)
    rate = rospy.Rate(0.1)
    # msg = send
    T = np.arange(t0,tf,0.01)
    
    # for _T,_p_traj in zip(T,p_traj):
    #     _pub = [_T,_p_traj]
    #     pub.publish(_pub)
    # rospy.loginfo(p_traj)

    p_out = std_msgs.Float32MultiArray()
    p_out.layout = T
    p_out.data = p_traj

    out_msg = plot_data()
    

    
    if(len(p_traj)>2):
        plt.figure(0)
        plt.clf()
        plt.plot(T,p_traj)
        plt.plot(T,v_traj)
        plt.plot(T,a_traj)

        out_msg.p_out = p_traj
        out_msg.a_out = v_traj
        out_msg.a_out = a_traj
        for _i in range(len(T)):
            out_msg.p_out = p_traj[_i]
            out_msg.a_out = v_traj[_i]
            out_msg.a_out = a_traj[_i]
            pub.publish(out_msg)
        
        
        plt.pause(3)
        plt.close(0)
    # p_out.data = v_traj
    # pub.publish(v_traj)
    # p_out.data = a_traj
    # pub.publish(a_traj)
    rate.sleep()





if __name__ == '__main__':
    listener()
    




