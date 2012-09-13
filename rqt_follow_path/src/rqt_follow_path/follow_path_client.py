import roslib
roslib.load_manifest('rqt_follow_path')
import rospy

import qt_gui.qt_binding_helper  # @UnusedImport
import QtCore, QtGui
from follow_path_widget import FollowPathWidget

def handle_shutdown():
    print('Shutting down ROS node.')
    global Form
    Form.shutdown_ros()

if __name__ == "__main__":
    # start up ROS
    rospy.init_node('test_follow_path_widget')
    rospy.on_shutdown(handle_shutdown)
    import sys
    app = QtGui.QApplication(sys.argv)
    print('Loading widget.')
    global Form
    Form = FollowPathWidget()
    print('Configuring ROS node')
    Form.configure_ros()
    Form.show()
    sys.exit(app.exec_())
