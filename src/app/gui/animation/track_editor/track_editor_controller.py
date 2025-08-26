import typing

from PySide6.QtCore import QObject, Qt, Signal, Slot

from ...dialog import NewAnimationDialog


class TrackEditorController(QObject):
    sigCreateNewAnimation = Signal(str)

    def __init__(self) -> None:
        super().__init__()

    @Slot()
    def newAnimation(self) -> None:
        dialog = NewAnimationDialog()
        if dialog.exec_() == NewAnimationDialog.Accepted:
            name = dialog.name()
            self.sigCreateNewAnimation.emit(name)
