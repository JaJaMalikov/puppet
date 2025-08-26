import typing

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QAction, QDockWidget, QWidget


class MaximizableDock(QDockWidget):
    def __init__(self, parent: typing.Optional[QWidget]) -> None:
        super().__init__(parent)

        self.topLevelChanged.connect(self.onTopLevelChanged)

        self.fullScreen = QAction("Full Screen")
        self.fullScreen.setShortcut("F12")
        self.fullScreen.triggered.connect(self.onFullScreen)
        self.addAction(self.fullScreen)

    @Slot(bool)
    def onTopLevelChanged(self, value: bool) -> None:
        if self.isFloating():
            self.setWindowFlags(
                Qt.CustomizeWindowHint
                | Qt.Window
                | Qt.WindowMinimizeButtonHint
                | Qt.WindowMaximizeButtonHint
                | Qt.WindowCloseButtonHint
            )
            self.show()

    @Slot()
    def onFullScreen(self) -> None:
        if self.isFloating():
            if not self.windowState() & Qt.WindowFullScreen:
                self.setWindowState(Qt.WindowFullScreen)
            else:
                self.setWindowState(Qt.WindowMaximized)
