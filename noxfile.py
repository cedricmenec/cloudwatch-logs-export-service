import nox

PYTHON_VERSIONS = [
    "3.9"
]


@nox.session(python="3.9", reuse_venv=True)
def pycharm(session):
    """Development Session"""
    session.install("-r", "src/requirements-dev.txt")


@nox.session(python="3.9", reuse_venv=True)
def wsl(session):
    """WSL Session"""
    session.install("-r", "src/requirements-dev.txt")
