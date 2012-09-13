import qt_gui.qt_binding_helper  # @UnusedImport

from qt_gui.plugin import Plugin
from follow_path_widget import FollowPathWidget

class FollowPath(Plugin):

    def __init__(self, context):
        super(FollowPath, self).__init__(context)
        # give QObjects reasonable names
        self.setObjectName('PathFollowingClient')

        # create widget object
        self._widget = FollowPathWidget()

        # add widget to the user interface
        context.add_widget(self._widget)

        # set up subscriptions to needed topics
        self._widget.configure_ros()

    def shutdown_plugin(self):
        # TODO unregister all publishers here
        self._widget.shutdown_ros()

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        # instance_settings.set_value(k, v)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        pass

    #def trigger_configuration(self):
        # Comment in to signal that the plugin has a way to configure it
        # Usually used to open a dialog to offer the user a set of configuration