from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class GlassWindow(QFrame):

    def __init__(self, title="Window"):
        super().__init__()

        self.setFixedSize(900, 650)

        self.setStyleSheet("""
            QFrame{
                background:rgba(40,40,45,210);
                border:1px solid rgba(255,255,255,60);
                border-radius:20px;
            }

            QLabel{
                color:white;
                background:transparent;
            }

            QPushButton{
                border:none;
                border-radius:7px;
                min-width:14px;
                max-width:14px;
                min-height:14px;
                max-height:14px;
            }
        """)

        layout = QVBoxLayout(self)

        # -------------------------
        # Title Bar
        # -------------------------

        title_bar = QHBoxLayout()

        close = QPushButton()
        close.setStyleSheet(
            "background:#ff5f57;"
        )

        minimize = QPushButton()
        minimize.setStyleSheet(
            "background:#ffbd2e;"
        )

        maximize = QPushButton()
        maximize.setStyleSheet(
            "background:#28c840;"
        )

        title_label = QLabel(title)
        title_label.setFont(
            QFont("Segoe UI", 12)
        )

        title_bar.addWidget(close)
        title_bar.addWidget(minimize)
        title_bar.addWidget(maximize)

        title_bar.addSpacing(15)

        title_bar.addWidget(title_label)

        title_bar.addStretch()

        layout.addLayout(title_bar)

        # -------------------------
        # Content
        # -------------------------

        content = QLabel(
            "Welcome to ViewFree\n\nVision Pro UI is now running."
        )

        content.setAlignment(Qt.AlignCenter)

        content.setFont(
            QFont("Segoe UI", 15)
        )

        layout.addStretch()
        layout.addWidget(content)
        layout.addStretch()