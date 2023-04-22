import os
import sys
import json

from PySide6.QtGui import QIcon
from utils import global_path
from src.utils import font
from src.Launcher.UI import launcher_ui
from PySide6.QtWidgets import QApplication, QWidget

global_path.set_proj_abs_path(os.path.abspath(__file__))


class Kuromu_Window(QWidget):
    def __init__(self):
        super(Kuromu_Window, self).__init__()
        with open(global_path.get_proj_abs_path("dump/Kuromu/config.json"), "r") as j:
            config = json.load(j)

        font.load_font(w=self)
        self.config = config

        launcher_ui.prepare(w=self)

        self.setWindowTitle("Kuromu Engine")
        self.setWindowIcon(QIcon(global_path.get_proj_abs_path("assets/kuromu.png")))
        self.setMinimumSize(600, 200)
        self.resize(1280, 720)
        self.initUI()

    def initUI(self):
        with open(
            file=global_path.get_proj_abs_path("dump/Kuromu/stylesheet.txt"), mode="r"
        ) as f:
            self.setStyleSheet(f.read())

        launcher_ui.work(w=self)

    def updateUI(self):
        pass


if __name__ == "__main__":
    Kuromu_Q_App = QApplication()
    Kuromu_app_GUI = Kuromu_Window()
    Kuromu_app_GUI.show()
    sys.exit(Kuromu_Q_App.exec())
