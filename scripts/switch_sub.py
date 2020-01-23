#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

s = [0, 0, 0, 0, 0, 0, 0]

def switch0_callback(msg):
    if msg.data:
        s[0] = 1
    else:
        s[0] = 0

def switch1_callback(msg):
    if msg.data:
        s[1] = 1
    else:
        s[1] = 0

def switch2_callback(msg):
    if msg.data:
        s[2] = 1
    else:
        s[2] = 0

def switch3_callback(msg):
    if msg.data:
        s[3] = 1
    else:
        s[3] = 0

def switch4_callback(msg):
    if msg.data:
        s[4] = 1
    else:
        s[4] = 0

def switch5_callback(msg):
    if msg.data:
        s[5] = 1
    else:
        s[5] = 0

def switch6_callback(msg):
    if msg.data:
        s[6] = 1
    else:
        s[6] = 0


if __name__ == "__main__":
	rospy.init_node("switch_sub")
	sub0 = rospy.Subscriber("switch0", Bool, switch0_callback, queue_size=10)
	sub1 = rospy.Subscriber("switch1", Bool, switch1_callback, queue_size=10)
        sub2 = rospy.Subscriber("switch2", Bool, switch2_callback, queue_size=10)
        sub3 = rospy.Subscriber("switch3", Bool, switch3_callback, queue_size=10)
        sub4 = rospy.Subscriber("switch4", Bool, switch4_callback, queue_size=10)
        sub5 = rospy.Subscriber("switch5", Bool, switch5_callback, queue_size=10)
        sub6 = rospy.Subscriber("switch6", Bool, switch6_callback, queue_size=10)
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            if s == [1, 0, 0, 0, 0, 0, 0]:
                print ('a')
            elif s == [1, 1, 0, 0, 0, 0, 0]:
                print ('b')
            elif s == [1, 0, 0, 1, 0, 0, 0]:
                print ('c')
            elif s == [1, 0, 0, 1, 1, 0, 0]:
                print ('d')
            elif s == [1, 0, 0, 0, 1, 0, 0]:
                print ('e')
            elif s == [1, 1, 0, 1, 0, 0, 0]:
                print ('f')
            elif s == [1, 1, 0, 1, 1, 0, 0]:
                print ('g')
            elif s == [1, 1, 0, 0, 1, 0, 0]:
                print ('h')
            elif s == [0, 1, 0, 1, 0, 0, 0]:
                print ('i')
            elif s == [0, 1, 0, 1, 1, 0, 0]:
                print ('j')
            elif s == [1, 0, 1, 0, 0, 0, 0]:
                print ('k')
            elif s == [1, 1, 1, 0, 0, 0, 0]:
                print ('l')
            elif s == [1, 0, 1, 1, 0, 0, 0]:
                print ('m')
            elif s == [1, 0, 1, 1, 1, 0, 0]:
                print ('n')
            elif s == [1, 0, 1, 0, 1, 0, 0]:
                print ('o')
            elif s == [1, 1, 1, 1, 0, 0, 0]:
                print ('p')
            elif s == [1, 1, 1, 1, 1, 0, 0]:
                print ('q')
            elif s == [1, 1, 1, 0, 1, 0, 0]:
                print ('r')
            elif s == [0, 1, 1, 1, 0, 0, 0]:
                print ('s')
            elif s == [0, 1, 1, 1, 1, 0, 0]:
                print ('t')
            elif s == [1, 0, 1, 0, 0, 1, 0]:
                print ('u')
            elif s == [1, 1, 1, 0, 0, 1, 0]:
                print ('v')
            elif s == [0, 1, 0, 1, 1, 1, 0]:
                print ('w')
            elif s == [1, 0, 1, 1, 0, 1, 0]:
                print ('x')
            elif s == [1, 0, 1, 1, 1, 1, 0]:
                print ('y')
            elif s == [1, 0, 1, 0, 1, 1, 0]:
                print ('z')
            else:
                print (' ')

        rate.sleep()
