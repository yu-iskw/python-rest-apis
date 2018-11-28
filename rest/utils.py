import os


def get_project_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
