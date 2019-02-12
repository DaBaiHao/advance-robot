#!/usr/bin/env python

import rospy

from std_msgs.msg import String
from AR_week5_test.msg import cubic_traj_params,cubic_traj_coeffs
from AR_week5_test.srv import *


def compute_cubic_coeffs(request):
	# p0, pf,v0,vf,t0,tf
	p0 = request.p0 
	pf = request.pf
	v0 = request.v0
	vf = request.vf
	t0 = request.t0
	tf = request.tf

	h = pf - p0
	T = tf - t0

	a0 = p0
	a1 = v0
	a2 = (3*h - (2*v0+vf)*T)/(T*T)
	a3 = (-2*h+(v0+vf)*T)/(T*T*T)
	return a0,a1,a2,a3








def compute_cubic_coeffs_server():
	rospy.init_node('compute_cubic_coeffs_server')
	s = rospy.Service('compute_cubic_coeffs', compute_cubic_traj, compute_cubic_coeffs)
	print ("Ready to compute_cubic_coeffs.")
	rospy.spin()


if __name__ == "__main__":
	compute_cubic_coeffs_server()