import sys
from random import randint

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QWidget

from ui import Ui_RandCirc


class RandCirc(QWidget, Ui_RandCirc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn.clicked.connect(self.trigger)
        self.flag = False
        self.x = self.width()
        self.y = self.height()

    def trigger(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            r = randint(30, 300)
            x, y = randint(r, self.x - r), randint(r, self.y - r)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(color)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandCirc()
    ex.show()
    sys.exit(app.exec())
