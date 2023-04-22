from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QSizePolicy,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QWidget,
)


def prepare(w):
    w.ENGINE_UPSIDE_BAR_CONTAINER = QVBoxLayout()
    w.ENGINE_UPSIDE_BAR = QHBoxLayout()
    w.ENGINE_UPSIDE_BAR_LABEL = QLabel(f"Kuromu Engine")
    w.ENGINE_UPSIDE_BAR_VERSION_LABEL = QLabel(f"v{w.config['version']}")
    w.ENGINE_UPSIDE_BAR_CSHTARN_LABEL = QLabel(f"CSHTARN")
    w.ENGINE_UPSIDE_BAR_END_LINE = QWidget()


def work(w):
    w.ENGINE_UPSIDE_BAR_LABEL.setFont(QFont(w.Pretendard_SemiBold, 20))
    w.ENGINE_UPSIDE_BAR.addWidget(w.ENGINE_UPSIDE_BAR_LABEL)

    w.ENGINE_UPSIDE_BAR_VERSION_LABEL.setFont(QFont(w.Pretendard_Light, 10))
    w.ENGINE_UPSIDE_BAR.addWidget(w.ENGINE_UPSIDE_BAR_VERSION_LABEL)

    w.ENGINE_UPSIDE_BAR.addStretch(1)
    w.ENGINE_UPSIDE_BAR_CSHTARN_LABEL.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.ENGINE_UPSIDE_BAR.addWidget(w.ENGINE_UPSIDE_BAR_CSHTARN_LABEL)

    ####################################################################################################################
    w.ENGINE_UPSIDE_BAR_CONTAINER.addLayout(w.ENGINE_UPSIDE_BAR)

    w.ENGINE_UPSIDE_BAR_END_LINE.setFixedHeight(1)
    w.ENGINE_UPSIDE_BAR_END_LINE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    w.ENGINE_UPSIDE_BAR_END_LINE.setStyleSheet("background-color: #ffffff;")

    w.ENGINE_UPSIDE_BAR_CONTAINER.addWidget(w.ENGINE_UPSIDE_BAR_END_LINE)
