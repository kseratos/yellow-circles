import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.circles = []  # Список для хранения информации о всех окружностях
        self.pushButton.clicked.connect(self.paint_yellow_circle)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for circle in self.circles:
            qp.setBrush(QColor(255, 255, 0))
            x, y, radius = circle
            qp.drawEllipse(x, y, radius, radius)
        qp.end()

    def paint_yellow_circle(self):
        # Генерируем случайные координаты и диаметр для новой окружности
        x = random.randint(0, self.centralWidget().size().width())
        y = random.randint(0, self.centralWidget().size().height())
        radius = random.randint(10, 100)

        # Добавляем информацию о новой окружности в список
        self.circles.append((x, y, radius))

        # Обновляем виджет
        self.update()


if __name__ == "__main__":
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
