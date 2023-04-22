from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QSizePolicy,
    QVBoxLayout,
    QLabel,
    QWidget,
    QGroupBox,
    QScrollArea,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
    QFileDialog,
)


def prepare(w):
    w.CREATE_UPDATE_TIMER = QTimer()

    w.CREATE_CONTAINER = QVBoxLayout()
    w.CREATE_LABEL = QLabel("Create New Project")

    w.CREATE_PROJECT_NAME_LABEL = QLabel("Project Name")
    w.CREATE_PROJECT_NAME_LINE = QLineEdit()

    w.CREATE_DEV_NAME_LABEL = QLabel("DEV Name")
    w.CREATE_DEV_NAME_LINE = QLineEdit()

    w.CREATE_DESCRIPTION_LABEL = QLabel("Description")
    w.CREATE_DESCRIPTION_LINE = QLineEdit("Simple Description")

    w.CREATE_LOCATION_LABEL = QLabel("Location")
    w.CREATE_LOCATION_HORIZONTAL_BOX = QHBoxLayout()
    w.CREATE_LOCATION_FILE_BUTTON = QPushButton("Open")
    w.CREATE_LOCATION_FILE_DIALOG = QFileDialog()
    w.CREATE_LOCATION_LINE = QLineEdit()

    w.CREATE_GROUP_BOX = QGroupBox()
    w.CREATE_VERTICAL_BOX = QVBoxLayout()
    w.CREATE_SCROLL_AREA = QScrollArea()
    w.CREATE_LINE = QWidget()


def work(w):
    w.CREATE_UPDATE_TIMER.setInterval(1000 / 20)
    w.CREATE_UPDATE_TIMER.timeout.connect(lambda: update(w=w))
    w.CREATE_UPDATE_TIMER.start()

    w.CREATE_PROJECT_NAME_LABEL.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.CREATE_VERTICAL_BOX.addWidget(w.CREATE_PROJECT_NAME_LABEL)
    w.CREATE_PROJECT_NAME_LINE.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.CREATE_VERTICAL_BOX.addWidget(w.CREATE_PROJECT_NAME_LINE)

    w.CREATE_DEV_NAME_LABEL.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.CREATE_VERTICAL_BOX.addWidget(w.CREATE_DEV_NAME_LABEL)
    w.CREATE_DEV_NAME_LINE.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.CREATE_VERTICAL_BOX.addWidget(w.CREATE_DEV_NAME_LINE)

    w.CREATE_DESCRIPTION_LABEL.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.CREATE_VERTICAL_BOX.addWidget(w.CREATE_DESCRIPTION_LABEL)
    w.CREATE_DESCRIPTION_LINE.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.CREATE_VERTICAL_BOX.addWidget(w.CREATE_DESCRIPTION_LINE)

    w.CREATE_LOCATION_LABEL.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.CREATE_VERTICAL_BOX.addWidget(w.CREATE_LOCATION_LABEL)
    w.CREATE_LOCATION_LINE.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.CREATE_LOCATION_LINE.setEnabled(False)
    w.CREATE_LOCATION_HORIZONTAL_BOX.addWidget(w.CREATE_LOCATION_LINE)
    w.CREATE_LOCATION_FILE_BUTTON.setFont(QFont(w.Pretendard_ExtraLight, 20))
    w.CREATE_LOCATION_FILE_BUTTON.released.connect(
        lambda: CREATE_LOCATION_FILE_BUTTON_CLICKED(w=w)
    )
    w.CREATE_LOCATION_HORIZONTAL_BOX.addWidget(w.CREATE_LOCATION_FILE_BUTTON)

    w.CREATE_VERTICAL_BOX.addLayout(w.CREATE_LOCATION_HORIZONTAL_BOX)

    w.CREATE_VERTICAL_BOX.addStretch(1)
    w.CREATE_LABEL.setFont(QFont(w.Pretendard_ExtraLight, 16))

    w.CREATE_GROUP_BOX.setLayout(w.CREATE_VERTICAL_BOX)
    w.CREATE_SCROLL_AREA.setWidget(w.CREATE_GROUP_BOX)
    w.CREATE_SCROLL_AREA.setWidgetResizable(True)

    w.CREATE_LINE.setFixedHeight(1)
    w.CREATE_LINE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    w.CREATE_LINE.setStyleSheet("background-color: #ffffff;")

    w.CREATE_CONTAINER.addWidget(w.CREATE_LABEL)
    w.CREATE_CONTAINER.addWidget(w.CREATE_LINE)
    w.CREATE_CONTAINER.addWidget(w.CREATE_SCROLL_AREA)


def CREATE_LOCATION_FILE_BUTTON_CLICKED(w):
    f = w.CREATE_LOCATION_FILE_DIALOG.getExistingDirectory(w, "Select Directory")

    if f:
        w.CREATE_LOCATION_LINE.setText(f)


def update(w):
    if (
        w.CREATE_PROJECT_NAME_LINE.text()
        and w.CREATE_DEV_NAME_LINE.text()
        and w.CREATE_DESCRIPTION_LINE.text()
        and w.CREATE_LOCATION_LINE.text()
    ):
        w.OPTIONS_CONFIRM_BUTTON.setEnabled(True)
    else:
        w.OPTIONS_CONFIRM_BUTTON.setEnabled(False)
