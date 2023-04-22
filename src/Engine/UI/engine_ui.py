from src.Engine.UI.UPSIDE_BAR import upside_bar


def prepare(w, project_data):
    w.PROJECT_DATA = project_data
    upside_bar.prepare(w=w)
    print(w.PROJECT_DATA.LOCATION)


def work(w):
    upside_bar.work(w=w)

    # Final
    w.PROJECT_GRID.addLayout(w.ENGINE_UPSIDE_BAR_CONTAINER, 0, 0, 1, 12)
    w.setLayout(w.PROJECT_GRID)
