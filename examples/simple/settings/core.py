import os


def project_dir(base):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), base).replace('\\', '/')
    )


PROJECT_DIR = project_dir


def gettext(val):
    return val
