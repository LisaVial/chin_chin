import numpy as np
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui

from mea_grid import MeaGrid


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 750)
        self.setWindowTitle('Chin chin!')
        app_icon = QtGui.QIcon('icon.png')
        self.setWindowIcon(app_icon)

        self.mea_grid_widget = MeaGrid(self)
        self.mea_grid_widget.grid_table.itemSelectionChanged.connect(self.on_channel_selection_changed)
        # ...basically you set a centralwidget which will be the focus point of the window
        self.setCentralWidget(self.mea_grid_widget)
        self.text_widget = QtWidgets.QPlainTextEdit(self)
        self.selected_channels_dock_widget = QtWidgets.QDockWidget(self)
        self.selected_channels_dock_widget.setWidget(self.text_widget)
        self.selected_channels_dock_widget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.selected_channels_dock_widget)

    def on_channel_selection_changed(self):
        channels, dead_channels = self.mea_grid_widget.get_selected_channels()
        dead_channels = list(dead_channels)
        channel_labels = [str(ch[0]) for ch in channels]
        channel_indices = [str(ch[1]) for ch in channels]

        channel_str = 'following channels were selected: ' + str(channel_labels) + '\n'
        indices_str = 'This results in the following indices: ' + str(channel_indices) + '\n'
        dead_ch_str = 'With the following dead channels: ' + str(dead_channels)
        self.text_widget.clear()
        self.text_widget.insertPlainText(channel_str)
        self.text_widget.insertPlainText(indices_str)
        self.text_widget.insertPlainText(dead_ch_str)

