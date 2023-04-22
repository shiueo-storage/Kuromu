import os
import sys

import webbrowser
import pickle

from src.Engine.UI import engine_ui
from src.Global import kuromu_data
from src.Launcher.UI.CREATE import create
from src.Launcher.UI.DESCRIPTION import description
from src.Launcher.UI.RECENT_PROJECTS import recent_projects
from src.utils import qt_deleteItemsOfLayout
from src.Launcher.Global import variables
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QWidget,
    QPushButton,
)

from utils import global_path


def prepare(w):
    w.OPTIONS_CONTAINER = QVBoxLayout()
    w.OPTIONS_LABEL = QLabel("Options")
    w.OPTIONS_LINE = QWidget()

    w.OPTIONS_OPEN_BUTTON = QPushButton("Open")
    w.OPTIONS_CREATE_BUTTON = QPushButton("Create")
    w.OPTIONS_BACK_BUTTON = QPushButton("Back")
    w.OPTIONS_CONFIRM_BUTTON = QPushButton("Confirm")
    w.OPTIONS_REFRESH_BUTTON = QPushButton("Refresh")

    w.OPTIONS_DOCUMENTS_BUTTON = QPushButton("Documents")
    w.OPTIONS_DISCORD_BUTTON = QPushButton("Discord")
    w.OPTIONS_EXIT_BUTTON = QPushButton("Exit")


def work(w):
    w.OPTIONS_LABEL.setFont(QFont(w.Pretendard_ExtraLight, 16))

    w.OPTIONS_LINE.setFixedHeight(1)
    w.OPTIONS_LINE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    w.OPTIONS_LINE.setStyleSheet("background-color: #ffffff;")

    w.OPTIONS_OPEN_BUTTON.setFont(QFont(w.Pretendard_Regular, 20))
    w.OPTIONS_OPEN_BUTTON.released.connect(lambda: OPEN_BUTTON_CLICKED(w=w))
    w.OPTIONS_OPEN_BUTTON.setEnabled(False)

    w.OPTIONS_CREATE_BUTTON.setFont(QFont(w.Pretendard_Regular, 20))
    w.OPTIONS_CREATE_BUTTON.released.connect(lambda: CREATE_BUTTON_CLICKED(w=w))

    w.OPTIONS_BACK_BUTTON.setFont(QFont(w.Pretendard_Regular, 20))
    w.OPTIONS_BACK_BUTTON.released.connect(lambda: BACK_BUTTON_CLICKED(w=w))
    w.OPTIONS_BACK_BUTTON.setEnabled(False)

    w.OPTIONS_CONFIRM_BUTTON.setFont(QFont(w.Pretendard_Regular, 20))
    w.OPTIONS_CONFIRM_BUTTON.released.connect(lambda: CONFIRM_BUTTON_CLICKED(w=w))
    w.OPTIONS_CONFIRM_BUTTON.setEnabled(False)

    w.OPTIONS_REFRESH_BUTTON.setFont(QFont(w.Pretendard_Regular, 20))
    w.OPTIONS_REFRESH_BUTTON.released.connect(lambda: REFRESH_BUTTON_CLICKED(w=w))

    w.OPTIONS_DISCORD_BUTTON.setFont(QFont(w.Pretendard_Regular, 20))
    w.OPTIONS_DISCORD_BUTTON.released.connect(lambda: DISCORD_BUTTON_CLICKED())

    w.OPTIONS_DOCUMENTS_BUTTON.setFont(QFont(w.Pretendard_Regular, 20))
    w.OPTIONS_DOCUMENTS_BUTTON.released.connect(lambda: DOCUMENTS_BUTTON_CLICKED())

    w.OPTIONS_EXIT_BUTTON.setFont(QFont(w.Pretendard_Regular, 20))
    w.OPTIONS_EXIT_BUTTON.released.connect(lambda: EXIT_BUTTON_CLICKED())

    w.OPTIONS_CONTAINER.addWidget(w.OPTIONS_LABEL)
    w.OPTIONS_CONTAINER.addWidget(w.OPTIONS_LINE)
    w.OPTIONS_CONTAINER.addWidget(w.OPTIONS_OPEN_BUTTON)
    w.OPTIONS_CONTAINER.addWidget(w.OPTIONS_CREATE_BUTTON)
    w.OPTIONS_CONTAINER.addWidget(w.OPTIONS_BACK_BUTTON)
    w.OPTIONS_CONTAINER.addWidget(w.OPTIONS_CONFIRM_BUTTON)
    w.OPTIONS_CONTAINER.addWidget(w.OPTIONS_REFRESH_BUTTON)
    w.OPTIONS_CONTAINER.addStretch(1)
    w.OPTIONS_CONTAINER.addWidget(w.OPTIONS_DOCUMENTS_BUTTON)
    w.OPTIONS_CONTAINER.addWidget(w.OPTIONS_DISCORD_BUTTON)
    w.OPTIONS_CONTAINER.addWidget(w.OPTIONS_EXIT_BUTTON)


def OPEN_BUTTON_CLICKED(w):
    qt_deleteItemsOfLayout.delete(parent_layout=w.UPSIDE_BAR_CONTAINER)
    w.UPSIDE_BAR_CONTAINER.setParent(None)

    qt_deleteItemsOfLayout.delete(parent_layout=w.RECENT_PROJECTS_CONTAINER)
    w.RECENT_PROJECTS_CONTAINER.setParent(None)

    qt_deleteItemsOfLayout.delete(parent_layout=w.DESCRIPTION_CONTAINER)
    w.DESCRIPTION_CONTAINER.setParent(None)

    qt_deleteItemsOfLayout.delete(parent_layout=w.OPTIONS_CONTAINER)
    w.OPTIONS_CONTAINER.setParent(None)

    data = kuromu_data.open_kuromu(path=variables.PROJECT_LOCATION)

    engine_ui.prepare(w=w, project_data=data)
    engine_ui.work(w=w)


def CREATE_BUTTON_CLICKED(w):
    qt_deleteItemsOfLayout.delete(parent_layout=w.RECENT_PROJECTS_CONTAINER)
    w.RECENT_PROJECTS_CONTAINER.setParent(None)
    qt_deleteItemsOfLayout.delete(parent_layout=w.DESCRIPTION_CONTAINER)
    w.DESCRIPTION_CONTAINER.setParent(None)

    create.prepare(w=w)
    create.work(w=w)
    w.PROJECT_GRID.addLayout(w.CREATE_CONTAINER, 1, 0, 1, 10)

    w.OPTIONS_BACK_BUTTON.setEnabled(True)
    w.OPTIONS_CREATE_BUTTON.setEnabled(False)
    w.OPTIONS_REFRESH_BUTTON.setEnabled(False)


def BACK_BUTTON_CLICKED(w):
    qt_deleteItemsOfLayout.delete(parent_layout=w.CREATE_CONTAINER)
    w.CREATE_CONTAINER.setParent(None)

    recent_projects.prepare(w=w)
    recent_projects.work(w=w)
    description.prepare(w=w)
    description.work(w=w)
    w.PROJECT_GRID.addLayout(w.RECENT_PROJECTS_CONTAINER, 1, 0, 1, 5)
    w.PROJECT_GRID.addLayout(w.DESCRIPTION_CONTAINER, 1, 5, 1, 5)
    w.OPTIONS_BACK_BUTTON.setEnabled(False)
    w.OPTIONS_OPEN_BUTTON.setEnabled(False)
    w.OPTIONS_CREATE_BUTTON.setEnabled(True)
    w.OPTIONS_REFRESH_BUTTON.setEnabled(True)


def CONFIRM_BUTTON_CLICKED(w):
    new_project_path = os.path.join(
        w.CREATE_LOCATION_LINE.text(), w.CREATE_PROJECT_NAME_LINE.text() + ".kuromu"
    ).replace("\\", "/")

    kuromu_data.make_kuromu(
        path=new_project_path,
        project_name=w.CREATE_PROJECT_NAME_LINE.text(),
        dev_name=w.CREATE_DEV_NAME_LINE.text(),
        description=w.CREATE_DESCRIPTION_LINE.text(),
        location=new_project_path,
    )

    with open(global_path.get_proj_abs_path("dump/Recent_Projects.cshtarn"), "rb") as f:
        data = pickle.load(f)
    data.add(new_project_path)
    with open(global_path.get_proj_abs_path("dump/Recent_Projects.cshtarn"), "wb") as f:
        pickle.dump(data, f)

    print("engine start", new_project_path)


def REFRESH_BUTTON_CLICKED(w):
    qt_deleteItemsOfLayout.delete(parent_layout=w.RECENT_PROJECTS_CONTAINER)
    w.RECENT_PROJECTS_CONTAINER.setParent(None)
    qt_deleteItemsOfLayout.delete(parent_layout=w.DESCRIPTION_CONTAINER)
    w.DESCRIPTION_CONTAINER.setParent(None)
    recent_projects.prepare(w=w)
    recent_projects.work(w=w)
    description.prepare(w=w)
    description.work(w=w)
    w.PROJECT_GRID.addLayout(w.RECENT_PROJECTS_CONTAINER, 1, 0, 1, 5)
    w.PROJECT_GRID.addLayout(w.DESCRIPTION_CONTAINER, 1, 5, 1, 5)
    w.OPTIONS_BACK_BUTTON.setEnabled(False)
    w.OPTIONS_OPEN_BUTTON.setEnabled(False)
    w.OPTIONS_CREATE_BUTTON.setEnabled(True)
    w.OPTIONS_REFRESH_BUTTON.setEnabled(True)


def DOCUMENTS_BUTTON_CLICKED():
    webbrowser.open("https://cshtarn.github.io/Kuromu")


def DISCORD_BUTTON_CLICKED():
    webbrowser.open("https://discord.gg/9epHu6qeCZ")


def EXIT_BUTTON_CLICKED():
    sys.exit()
