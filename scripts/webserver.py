#!/usr/bin/env python
import rospy
import os
import SimpleHTTPServer


def kill():
    os.system("kill -KILL " + str(os.getpid()))


os.chdir(os.path.dirname(__file__) + "/../contents")
rospy.init_node("webserver")
rospy.on_shutdown(kill)
SimpleHTTPServer.test()
