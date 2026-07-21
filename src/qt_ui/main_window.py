import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

from src.qt_ui.camera_widget import CameraWidget
from src.qt_ui.glass_window import GlassWindow


class ViewFreeWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ViewFree OS")

        self.resize(1600, 900)

        self.setStyleSheet("""
            QWidget{
                background:#111114;
            }
        """)

        # -----------------------
        # Full Screen Camera
        # -----------------------

        self.camera = CameraWidget(self)
        self.camera.setGeometry(0, 0, 1600, 900)

        # -----------------------
        # Floating AI Window
        # -----------------------

        self.ai = GlassWindow("AI Assistant")
        self.ai.setParent(self)

        self.ai.move(980, 180)

        self.ai.raise_()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = ViewFreeWindow()

    window.show()

    sys.exit(app.exec())