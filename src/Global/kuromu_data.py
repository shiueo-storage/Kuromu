import pickle


class kuromu_data:
    def __init__(
        self, project_name=None, dev_name=None, description=None, location=None
    ):
        self.PROJECT_NAME = project_name
        self.DEV_NAME = dev_name
        self.DESCRIPTION = description
        self.LOCATION = location


def open_kuromu(path):
    with open(path, "rb") as f:
        data = pickle.load(f)
        return data


def make_kuromu(path, project_name, dev_name, description, location):
    data = kuromu_data(
        project_name=project_name,
        dev_name=dev_name,
        description=description,
        location=location,
    )
    with open(path, "wb") as f:
        pickle.dump(data, f)
