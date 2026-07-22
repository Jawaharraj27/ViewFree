import sys
import os

# ---------------------------------
# Add project root
# ---------------------------------
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
    QWidget,
    QVBoxLayout,
)

from src.qt_ui.glass_window import GlassWindow
from src.qt_ui.camera_widget import CameraWidget


class ViewFreeWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ViewFree OS")
        self.resize(1400, 900)

        self.setStyleSheet("""
            QWidget{
                background:#111114;
            }
        """)

        layout = QVBoxLayout(self)

        layout.addStretch()

        glass = GlassWindow("ViewFree Camera")
        camera = CameraWidget()

        glass.layout().addWidget(camera)
        layout.addWidget(glass)

        layout.addStretch()

        self.setLayout(layout)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = ViewFreeWindow()

    window.show()

    sys.exit(app.exec())