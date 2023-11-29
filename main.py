import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor
import random


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.add_random_circle)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

    def add_random_circle(self):
        diameter = random.randint(10, 100)
        circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        color = QColor(255, 255, 0)
        circle.setBrush(color)
        self.scene.addItem(circle)
