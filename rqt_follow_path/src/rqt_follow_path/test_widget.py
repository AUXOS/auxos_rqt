import roslib
roslib.load_manifest('rqt_follow_path')
import qt_gui.qt_binding_helper  # @UnusedImport
import QtCore, QtGui
from follow_path_widget import FollowPathWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = FollowPathWidget()
    Form.show()
    sys.exit(app.exec_())