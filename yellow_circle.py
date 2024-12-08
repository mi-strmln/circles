from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QPainter, QColor, QPolygon
import sys
import random
from UI import Ui_MainWindow

class Circle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.size = random.randint(20, 200)
        self.color = ((255 - random.randint(0, 255)), (255 - random.randint(0, 255)),
                      (255 - random.randint(0, 255)))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(100, 800), random.randint(100, 600)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
