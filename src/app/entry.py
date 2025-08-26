import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from qtmodern import styles

from .gui import AppWindow

try:
    from PySide6.QtWinExtras import QtWin

    QtWin.setCurrentProcessExplicitAppUserModelID("com.paspallas.tool.puppet")
except ImportError:
    pass


def start() -> None:
    """Démarre l'application principale."""
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    app = QApplication([])
    styles.dark(app)

    main_window = AppWindow()

    desktop = QApplication.desktop().screenGeometry(0)
    main_window.move(desktop.left(), desktop.top())
    main_window.showMaximized()

    sys.exit(app.exec_())
