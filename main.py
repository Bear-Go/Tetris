import sys
from PyQt5.QtWidgets import QApplication
from window import TetrisWindow


def main():
    app = QApplication(sys.argv)
    ex = TetrisWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
