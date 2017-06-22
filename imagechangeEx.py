#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sip

from PyQt5.QtWidgets import QWidget, QComboBox, QVBoxLayout, QLabel, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# sip.setapi('QString', 2)
# sip.setapi('QVariant', 2)


class ImageChanger(QWidget):
    def __init__(self, images, parent=None):
        super(ImageChanger, self).__init__(parent)

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(images)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.comboBox)

class MyWindow(QWidget):
    def __init__(self, images, parent=None):
        super(MyWindow, self).__init__(parent)
        self.label = QLabel(self)
        self.imageChanger = ImageChanger(images)
        self.imageChanger.move(self.imageChanger.pos().y(), self.imageChanger.pos().x() + 100)
        self.imageChanger.show()
        self.imageChanger.comboBox.currentIndexChanged[str].connect(self.changeImage)
        self.layout = QVBoxLayout(self)

    @pyqtSlot(str)
    def changeImage(self, pathToImage):
        pixmap = QPixmap(pathToImage)


if __name__ == "__main__":
    import sys

    images = [  "left.png",
                "right.png",
                "Temmie.png",
                ]

    app = QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow(images)
    main.show()

    sys.exit(app.exec_())