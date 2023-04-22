from src.Launcher.Global import variables
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QWidget,
    QPlainTextEdit,
)


def prepare(w):
    w.DESCRIPTION_CONTAINER = QVBoxLayout()
    w.DESCRIPTION_LABEL = QLabel("Project Description")
    w.DESCRIPTION_CONTENT_LABEL = QPlainTextEdit("No Description Available")
    w.DESCRIPTION_LINE = QWidget()


def work(w):
    w.DESCRIPTION_LABEL.setFont(QFont(w.Pretendard_ExtraLight, 16))
    w.DESCRIPTION_CONTENT_LABEL.setFont(QFont(w.Pretendard_Regular, 20))
    w.DESCRIPTION_CONTENT_LABEL.setReadOnly(True)

    w.DESCRIPTION_LINE.setFixedHeight(1)
    w.DESCRIPTION_LINE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    w.DESCRIPTION_LINE.setStyleSheet("background-color: #ffffff;")

    w.DESCRIPTION_CONTAINER.addWidget(w.DESCRIPTION_LABEL)
    w.DESCRIPTION_CONTAINER.addWidget(w.DESCRIPTION_LINE)
    w.DESCRIPTION_CONTAINER.addWidget(w.DESCRIPTION_CONTENT_LABEL)


def update(w):
    w.DESCRIPTION_CONTENT_LABEL.clear()
    w.DESCRIPTION_CONTENT_LABEL.appendPlainText(
        f"Project: {variables.PROJECT_NAME}\n\n{variables.PROJECT_CONTENT_DESCRIPTION}"
    )
