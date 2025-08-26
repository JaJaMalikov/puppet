from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QPushButton


class ColorButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setCheckable(False)

        self._default = "#ffffff"
        self.setColor(self._default)

    @Slot(str)
    def setColor(self, color: str):
        if color:
            self.setStyleSheet(f"background-color: {color}")
        else:
            self.setStyleSheet("")

    def color(self):
        return self._color
