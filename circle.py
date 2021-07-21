#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import TwistStamped
from geometry_msgs.msg import PoseStamped
from tf.transformations import euler_from_quaternion

def callback(msg): 

    orientation_q = msg.pose.orientation

    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]

    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)

    print(roll, pitch, yaw)  #made for my reference, remove if you want
    
    velocitymsg.twist.linear.x = -10*math.sin(yaw) #math.sin(yaw)
    velocitymsg.twist.linear.y = 10*math.cos(yaw) #math.cos(yaw) 

    pub_obj.publish(velocitymsg)


rospy.init_node('circle')
sub_obj = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, callback) 
pub_obj = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel', TwistStamped, queue_size=10)
rate = rospy.Rate(10)
velocitymsg = TwistStamped()
posemsg = PoseStamped()

velocitymsg.twist.angular.z = 0.5
     
rospy.spin()




