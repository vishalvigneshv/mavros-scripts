#!/usr/bin/env python

#import necessary packages and function
import rospy
import math
from geometry_msgs.msg import TwistStamped
from geometry_msgs.msg import PoseStamped
from tf.transformations import euler_from_quaternion

def callback(msg): 

    #extract the orientation quaternion from msg
    orientation_q = msg.pose.orientation

    #store the orientation quaternion in a list
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]

    #change the orientation from quaternion form to euler form
    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)

    #print the orientation in euler form
    print(roll, pitch, yaw)  

    velocitymsg.twist.angular.z = 0.5

    #set linear velocity values along x & y axes in velocitymsg for velocity setpoint
    velocitymsg.twist.linear.x = -10*math.sin(yaw) 
    velocitymsg.twist.linear.y = 10*math.cos(yaw) 

    #publish the velocity setpoint
    pub_obj.publish(velocitymsg)

#initialize rospy node circle
rospy.init_node('circle')

#subscribe to /mavros/local_position/pose topic to get orientation data
sub_obj = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, callback) 

#publisher object to publish velocity setpoints
pub_obj = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel', TwistStamped, queue_size=10)

rate = rospy.Rate(10)
velocitymsg = TwistStamped()
rospy.spin()
