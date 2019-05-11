#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32  
#This class will receive a number and an increment and it will publish the 
# result of adding number+increment in a recursive way.
class Adder_Class():
    def __init__(self):
        rospy.on_shutdown(self.cleanup)
        ###******* INIT PUBLISHERS *******###
        print "Setting publisher..."
        ##	pub = rospy.Publisher('setPoint', UInt16MultiArray, queue_size=1)
        self.pub_sum = rospy.Publisher('sum', Int32, queue_size=1)
        print "Publishers ok"
        print "Starting Node..."
        ############################### SUBSCRIBERS #####################################
        rospy.Subscriber("number", Int32, self.number_cb)
        rospy.Subscriber("increment", Int32, self.increment_cb)
        ############ CONSTANTS ################
        self.number = 0 #The number to be use in the sum
        self.increment = 1 # The increment tu be used in the sum
        #********** INIT NODE **********###
        r = rospy.Rate(1)              #1Hz
        print "Node initialized 1hz"
        while not rospy.is_shutdown():
            self.number=self.number+self.increment #Add here the number and the increment
            self.pub_sum.publish(self.number) #publish the number
            print self.number
            r.sleep()

    def number_cb(self, number):
        ## This function receives a number 
        pass
    def increment_cb(self, increment):
        ## This function receives a number.
        pass
    def cleanup(self):
        #This function is called just before finishing the node
        # You can use it to clean things up before leaving
        # Example: stop the robot before finishing a node.	
        pass


############################### MAIN PROGRAM ####################################
if __name__ == "__main__":
    rospy.init_node("adder_node", anonymous=True)
    try:
	    Adder_Class()
    except:
        rospy.logfatal("adder_node died")