import os.path
import pickle

from src.Global import kuromu_data
from src.Launcher.Global import variables
from src.Launcher.UI.DESCRIPTION import description
from utils import global_path
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QSizePolicy,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QGroupBox,
    QScrollArea,
)


def prepare(w):
    with open(global_path.get_proj_abs_path("dump/Recent_Projects.cshtarn"), "rb") as f:
        data = pickle.load(f)

    refresh_data = set()
    for i in data:
        if os.path.isfile(i):
            refresh_data.add(i)

    with open(global_path.get_proj_abs_path("dump/Recent_Projects.cshtarn"), "wb") as f:
        pickle.dump(refresh_data, f)
    w.RECENT_PROJECTS_CONTAINER = QVBoxLayout()
    w.RECENT_PROJECTS_LABEL = QLabel("Recent Projects")
    w.RECENT_PROJECTS_NO_PROJECTS_LABEL = QLabel("No Recent Projects")

    w.RECENT_PROJECTS_GROUP_BOX = QGroupBox()
    w.RECENT_PROJECTS_VERTICAL_BOX = QVBoxLayout()
    w.RECENT_PROJECTS_SCROLL_AREA = QScrollArea()
    w.RECENT_PROJECTS_LINE = QWidget()


def work(w):
    with open(global_path.get_proj_abs_path("dump/Recent_Projects.cshtarn"), "rb") as f:
        recent_projects_data = pickle.load(f)
    variables.PROJECT_CONTENT = recent_projects_data

    if recent_projects_data:
        for recent_projects in recent_projects_data:
            data = kuromu_data.open_kuromu(recent_projects)
            button = QPushButton(data.PROJECT_NAME)
            button.setFont(QFont(w.Pretendard_Regular, 20))
            button.setObjectName(recent_projects)
            button.released.connect(
                lambda x=button: recent_projects_button_clicked(w=w, button=x)
            )
            w.RECENT_PROJECTS_VERTICAL_BOX.addWidget(button)
    else:
        w.RECENT_PROJECTS_NO_PROJECTS_LABEL.setFont(QFont(w.Pretendard_Regular, 20))
        w.RECENT_PROJECTS_VERTICAL_BOX.addWidget(w.RECENT_PROJECTS_NO_PROJECTS_LABEL)

    w.RECENT_PROJECTS_VERTICAL_BOX.addStretch(1)
    w.RECENT_PROJECTS_LABEL.setFont(QFont(w.Pretendard_ExtraLight, 16))

    w.RECENT_PROJECTS_GROUP_BOX.setLayout(w.RECENT_PROJECTS_VERTICAL_BOX)
    w.RECENT_PROJECTS_SCROLL_AREA.setWidget(w.RECENT_PROJECTS_GROUP_BOX)
    w.RECENT_PROJECTS_SCROLL_AREA.setWidgetResizable(True)

    w.RECENT_PROJECTS_LINE.setFixedHeight(1)
    w.RECENT_PROJECTS_LINE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    w.RECENT_PROJECTS_LINE.setStyleSheet("background-color: #ffffff;")

    w.RECENT_PROJECTS_CONTAINER.addWidget(w.RECENT_PROJECTS_LABEL)
    w.RECENT_PROJECTS_CONTAINER.addWidget(w.RECENT_PROJECTS_LINE)
    w.RECENT_PROJECTS_CONTAINER.addWidget(w.RECENT_PROJECTS_SCROLL_AREA)


def recent_projects_button_clicked(w, button):
    data = kuromu_data.open_kuromu(path=button.objectName())
    variables.PROJECT_NAME = data.PROJECT_NAME
    variables.PROJECT_CONTENT_DESCRIPTION = data.DESCRIPTION
    variables.PROJECT_LOCATION = data.LOCATION
    description.update(w)
    w.OPTIONS_OPEN_BUTTON.setEnabled(True)
