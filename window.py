from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter, QPen, QColor, QRadialGradient, QIcon
from PyQt5.QtCore import Qt, QPoint


class TetrisWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName('MainWindow')
        self.setWindowTitle('Tetris')
        self.setWindowIcon(QIcon('images/T.ico'))
        self.setFixedSize(650, 650)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            print('w')
        elif event.key() == Qt.Key_A:
            print('a')
        elif event.key() == Qt.Key_S:
            print('s')
        elif event.key() == Qt.Key_D:
            print('d')
