from PySide6.QtWidgets import QGridLayout

from src.Launcher.UI.DESCRIPTION import description
from src.Launcher.UI.OPTIONS import options
from src.Launcher.UI.RECENT_PROJECTS import recent_projects
from src.Launcher.UI.UPSIDE_BAR import upside_bar


def prepare(w):
    w.PROJECT_GRID = QGridLayout()
    upside_bar.prepare(w=w)
    recent_projects.prepare(w=w)
    description.prepare(w=w)
    options.prepare(w=w)


def work(w):
    upside_bar.work(w=w)
    recent_projects.work(w=w)
    description.work(w=w)
    options.work(w=w)

    # Final
    w.PROJECT_GRID.addLayout(w.UPSIDE_BAR_CONTAINER, 0, 0, 1, 12)
    w.PROJECT_GRID.addLayout(w.RECENT_PROJECTS_CONTAINER, 1, 0, 1, 5)
    w.PROJECT_GRID.addLayout(w.DESCRIPTION_CONTAINER, 1, 5, 1, 5)
    w.PROJECT_GRID.addLayout(w.OPTIONS_CONTAINER, 1, 10, 1, 2)
    w.setLayout(w.PROJECT_GRID)
