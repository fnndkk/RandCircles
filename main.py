import sys
import io

from random import randint

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>RandCirc</class>
 <widget class="QWidget" name="RandCirc">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>800</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="btn">
   <property name="geometry">
    <rect>
     <x>690</x>
     <y>10</y>
     <width>101</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>create circle</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class RandCirc(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

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
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            qp.drawEllipse(x, y, r, r)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandCirc()
    ex.show()
    sys.exit(app.exec())


