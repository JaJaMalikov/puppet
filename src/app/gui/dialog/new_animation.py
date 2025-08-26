import typing

from PySide6.QtCore import Qt, Slot, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)


class NewAnimationDialog(QDialog):
    """Boîte de dialogue pour créer une nouvelle animation."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Create a new animation")
        self.setFixedSize(300, 100)

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self._buttonBox = QDialogButtonBox(buttons)
        self._buttonBox.accepted.connect(self.accept)
        self._buttonBox.rejected.connect(self.reject)

        self._name = QLineEdit("")
        self._name.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9_()]*")))
        self._label = QLabel("Name")

        hbox = QHBoxLayout()
        hbox.addWidget(self._label)
        hbox.addWidget(self._name)

        vbox = QVBoxLayout(self)
        vbox.addLayout(hbox)
        vbox.addStretch()
        vbox.addWidget(self._buttonBox)

    def name(self) -> str:
        """Retourne le nom saisi par l'utilisateur."""
        return self._name.text()
