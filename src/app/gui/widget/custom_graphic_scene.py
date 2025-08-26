import typing

from PySide6.QtCore import QObject, Qt, Signal, Slot
from PySide6.QtWidgets import (
    QGraphicsItem,
    QGraphicsScene,
    QGraphicsSceneMouseEvent,
    QWidget,
)


class CustomGraphicScene(QGraphicsScene):
    sigSelectedItem = Signal(QGraphicsItem)
    sigNoItemSelected = Signal()

    def __init__(
        self, width: float, height: float, parent: typing.Optional[QObject] = None
    ) -> None:
        super().__init__(parent)

        self.setSceneRect(-width // 2, -height // 2, width, height)
        self.setItemIndexMethod(QGraphicsScene.NoIndex)
        self.focusItemChanged.connect(self._onFocusItemChanged)

    @Slot(list)
    def addItems(self, items: typing.List[QGraphicsItem]) -> None:
        for item in items:
            self.addItem(item)

    @Slot(list)
    def delItems(self, items: typing.List[QGraphicsItem]) -> None:
        for item in items:
            self.removeItem(item)

    @Slot(QGraphicsItem, QGraphicsItem, Qt.FocusReason)
    def _onFocusItemChanged(
        self, new: QGraphicsItem, old: QGraphicsItem, reason: Qt.FocusReason
    ) -> None:
        if new is None:
            self.sigNoItemSelected.emit()
        else:
            self.sigSelectedItem.emit(new)
