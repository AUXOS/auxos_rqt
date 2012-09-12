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


class PathFollowingWidget(QWidget):
    """
    Primary widget for the rqt_path_following_client plugin.
    """
    def __init__(self):
        super(PathFollowingWidget, self).__init__()
        ui_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'path_following_widget.ui')
        loadUi(ui_file, self)
        self.setObjectName('PathFollowingWidget')

    def _handle_start_following(self):
        # get path file to load
        # filename = QFileDialog.getOpenFileName(self, self.tr('Load Path from File'), '.', self.tr('Path File {.txt} (*.txt)'))
        # if filename[0] != '':
        #     try:
        #         handle = open(filename[0])
        #     except IOError as e:
        #         qWarning(str(e))
        #         return
        # path_filename.setText(filename)

        print("start following")

    def _handle_stop_following(self):
        print("stop following")
