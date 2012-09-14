# Software License Agreement (BSD License)
#
# Copyright (c) 2012, IS4S, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os

from qt_gui.qt_binding_helper import loadUi
from QtGui import QApplication, QCursor, QFileDialog, QIcon, QMenu, QMessageBox, QTableView, QWidget
from QtCore import QRegExp, Qt, qWarning

import roslib
import rospy
import actionlib
import auxos_messages.msg
roslib.load_manifest('rqt_follow_path')

import tf
from tf.transformations import quaternion_from_euler as qfe

import numpy as np
from math import radians

from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path

import math
import csv

def psi2theta(psi):
    return math.pi/2-psi

class FollowPathWidget(QWidget):
    """
    Primary widget for the rqt_path_following_client plugin.
    """
    def __init__(self):
        super(FollowPathWidget, self).__init__()
        ui_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'follow_path_widget.ui')
        loadUi(ui_file, self)
        self.setObjectName('PathFollowingWidget')

        self.path_frame_id = rospy.get_param("~path_frame_id", "odom")
    
    def configure_ros(self):
        """ Set up ROS communications"""
        self._client=actionlib.SimpleActionClient('PlanThenFollowDubinsPath',auxos_messages.msg.PlanThenFollowDubinsPathAction)

    def shutdown_ros(self):
        """ Shutdown ROS communications"""


    def _handle_start_following(self):

        #make sure server is available before sending goal
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        if (not self._client.wait_for_server(rospy.Duration.from_sec(10))):
            QApplication.restoreOverrideCursor()
            msg_box = QMessageBox()
            msg_box.setText("Timeout while looking for path following control server.")
            msg_box.exec_()
            return
        QApplication.restoreOverrideCursor()

        #get path file to load
        filename = QFileDialog.getOpenFileName(self, self.tr('Load Path from File'), '.', self.tr('Path File {.txt} (*.txt)'))
        if filename[0] != '':
            try:
                handle = open(filename[0])
            except IOError as e:
                qWarning(str(e))
                return
        #path_filename.setText(filename)
        print(filename)

        # load path from file
        path_reader=csv.reader(open(filename[0],'rb'),delimiter=';')

        # parse path file and convert to numbers
        temp = [row[0].split() for row in path_reader]
        lines= [[float(num) for num in row] for row in temp]

        # first line of file is radius
        radius = lines[0]
        # remove radius
        del(lines[0])

        now = rospy.Time.now()
        goal = auxos_messages.msg.PlanThenFollowDubinsPathGoal()

        goal.path.header.stamp = now
        goal.path.header.frame_id = self.path_frame_id # TODO: fix this!!!
        for line in lines:
            pose_msg = PoseStamped()
            pose_msg.header.stamp = now
            pose_msg.header.frame_id = goal.path.header.frame_id
            pose_msg.pose.position.x = line[0]
            pose_msg.pose.position.y = line[1]
            quat = qfe(0, 0, psi2theta(line[2]))
            pose_msg.pose.orientation.x = quat[0]
            pose_msg.pose.orientation.y = quat[1]
            pose_msg.pose.orientation.z = quat[2]
            pose_msg.pose.orientation.w = quat[3]
            goal.path.poses.append(pose_msg)

        self._client.send_goal(goal, self._handle_path_complete, self._handle_active, self._handle_feedback)

        print("start following")

    def _handle_stop_following(self):
        print("stop following")

    def _handle_feedback(self, feedback):
        #update labels with feedback - need to use signals and slots
        print('feedback received')

    def _handle_path_complete(self, goal_status, goal_result):
        print(goal_status)
        print(goal_result)
        print('path complete')

    def _handle_active(self):
        print('transitioned to active')

