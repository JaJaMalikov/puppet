from PySide6.QtCore import QObject, Qt, Signal, Slot


class SpriteListBoxController(QObject):
    def __init__(self) -> None:
        super().__init__()