import roslib
roslib.load_manifest('path_following_client')
import qt_gui.qt_binding_helper  # @UnusedImport
import QtCore, QtGui
from path_following_widget import PathFollowingWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = PathFollowingWidget()
    Form.show()
    sys.exit(app.exec_())