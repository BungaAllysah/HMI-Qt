# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtQml import QQmlApplicationEngine  # noqa: E402
from PySide2.QtGui import QGuiApplication  # noqa: E402


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
