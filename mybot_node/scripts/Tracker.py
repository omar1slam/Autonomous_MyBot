#!/usr/bin/env python  

import math as m
import rospy
from geometry_msgs.msg import Twist, Pose
from std_msgs.msg import String , Float32MultiArray
from nav_msgs.msg import Odometry
import numpy as np
x_current=0.0
y_current=0.0
yaw=0.0
pathx = []
pathy = []
a = Twist()
rospy.init_node('Setter',anonymous=True)

pub = rospy.Publisher('/mybot/cmd_vel',Twist,queue_size=10)
def go2pos(x_target,y_target):
    global x_current
    global y_current, z, yaw

    velc_msg = Twist()
    while(1):
        
        C = 0.35
        distance = m.sqrt(((x_target-x_current)**2)+((y_target-y_current)**2))
        V = distance*C

        C2 = 2                                               
        yaw_target = m.atan2(y_target-y_current,x_target-x_current)
        W = (yaw_target-yaw)*C2
        velc_msg.linear.x = V
        velc_msg.angular.z = W
        pub.publish(velc_msg)
        #print(V,W)
        #print('current goal', x_target , y_target)
        #print('current pos',x_current,y_current,distance)
        if (distance<0.5):
            count = 0
            while (count<100000):
                velc_msg.linear.x = 0
                velc_msg.angular.z = 0
                pub.publish(velc_msg)
                count = count +1
            break
        '''
        yaw_target = m.atan2(y_target-y_current,x_target-x_current)
        distance = m.sqrt(((x_target-x_current)**2)+((y_target-y_current)**2))
        if distance >= 0.5:
            if abs(yaw_target - yaw) > 0.1:
                velc_msg.linear.x = 0.0
                velc_msg.angular.z = 5
            elif abs(yaw_target - yaw) < 0.1:
                velc_msg.linear.x = 1
                velc_msg.angular.z = 0.0
        else:
            #error = (target_x-x)/target_x
            #print ("error=",error)
            velc_msg.linear.x = 0.0
            velc_msg.angular.z = 0.0
            print("The goal has reached :) ")
            break
        pub.publish(velc_msg)
        '''
        

def current_pos(data):
    global x_current,y_current,yaw
    x_current = data.pose.pose.position.x
    y_current = data.pose.pose.position.y
    yaw = data.pose.pose.orientation.z
    
def path(data):
    msg = data.data
    global pathx , pathy
    index = len(msg)/2
    pathx = msg[:index]
    pathy = msg[index:]

boolean = 0
sub = rospy.Subscriber('/odom',Odometry,current_pos)
while not rospy.is_shutdown():
    
    
    #print(x_current,y_current,yaw)
    #go2pos(10.0,3.0)
    sub2 = rospy.Subscriber('path',Float32MultiArray,path)

    if (len(pathx) != 0) & (boolean == 0) :
        for i in range(0,len(pathx)):
            print(pathx[i],pathy[i])
            go2pos(pathx[i],pathy[i])
            if (i == len(pathx)):
                boolean = 1


    
    
  
    

   
