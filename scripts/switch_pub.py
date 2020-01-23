#!/usr/bin/env python 

import rospy
from std_msgs.msg import Bool

if __name__ == "__main__":
	rospy.init_node("switch_pub")
	pub0 = rospy.Publisher("switch0", Bool, queue_size=10)
        pub1 = rospy.Publisher("switch1", Bool, queue_size=10)
        pub2 = rospy.Publisher("switch2", Bool, queue_size=10)
        pub3 = rospy.Publisher("switch3", Bool, queue_size=10)
        pub4 = rospy.Publisher("switch4", Bool, queue_size=10)
        pub5 = rospy.Publisher("switch5", Bool, queue_size=10)
        pub6 = rospy.Publisher("switch6", Bool, queue_size=10)
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():

            with open("/dev/rtswitch0", "r") as f:
	        s = f.read(1)
                if s == '0':
                    pub0.publish(True)
                else:
                    pub0.publish(False)

            with open("/dev/rtswitch1", "r") as f:
                s = f.read(1)
                if s == '0':
                    pub1.publish(True)
                else:
                    pub1.publish(False)

            with open("/dev/rtswitch2", "r") as f:
                s = f.read(1)
                if s == '0':
                    pub2.publish(True)
                else:
                    pub2.publish(False)

            with open("/dev/rtswitch3", "r") as f:
                s = f.read(1)
                if s == '0':
                    pub3.publish(True)
                else:
                    pub3.publish(False)        
            with open("/dev/rtswitch4", "r") as f:
                s = f.read(1)
                if s == '0':
                    pub4.publish(True)
                else:
                    pub4.publish(False)

            with open("/dev/rtswitch5", "r") as f:
                s = f.read(1)
                if s == '0':
                    pub5.publish(True)
                else:
                    pub5.publish(False)

            with open("/dev/rtswitch6", "r") as f:
                s = f.read(1)
                if s == '0':
                    pub6.publish(True)
                else:
                    pub6.publish(False)
            
