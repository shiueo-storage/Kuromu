from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QSizePolicy,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QWidget,
)


def prepare(w):
    w.UPSIDE_BAR_CONTAINER = QVBoxLayout()
    w.UPSIDE_BAR = QHBoxLayout()
    w.UPSIDE_BAR_LABEL = QLabel(f"Kuromu Engine")
    w.UPSIDE_BAR_VERSION_LABEL = QLabel(f"v{w.config['version']}")
    w.UPSIDE_BAR_CSHTARN_LABEL = QLabel(f"CSHTARN")
    w.UPSIDE_BAR_END_LINE = QWidget()


def work(w):
    w.UPSIDE_BAR_LABEL.setFont(QFont(w.Pretendard_SemiBold, 20))
    w.UPSIDE_BAR.addWidget(w.UPSIDE_BAR_LABEL)

    w.UPSIDE_BAR_VERSION_LABEL.setFont(QFont(w.Pretendard_Light, 10))
    w.UPSIDE_BAR.addWidget(w.UPSIDE_BAR_VERSION_LABEL)

    w.UPSIDE_BAR.addStretch(1)
    w.UPSIDE_BAR_CSHTARN_LABEL.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.UPSIDE_BAR.addWidget(w.UPSIDE_BAR_CSHTARN_LABEL)

    ####################################################################################################################
    w.UPSIDE_BAR_CONTAINER.addLayout(w.UPSIDE_BAR)

    w.UPSIDE_BAR_END_LINE.setFixedHeight(1)
    w.UPSIDE_BAR_END_LINE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    w.UPSIDE_BAR_END_LINE.setStyleSheet("background-color: #ffffff;")

    w.UPSIDE_BAR_CONTAINER.addWidget(w.UPSIDE_BAR_END_LINE)
