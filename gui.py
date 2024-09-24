import sys
import threading

from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QSlider,
    QWidget,
)
from time import sleep

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Autoclicker v0.1")
        self.setGeometry(100, 100, 300, 100)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)

        widget = ClickSpeedSlider()

        self.setCentralWidget(widget)


class ClickSpeedSlider(QWidget):
    def __init__(self):
        super().__init__()

        # click rate control
        click_rate = 10
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setSingleStep(10)
        self.slider.setValue(click_rate)

        # click rate label
        self.label = QLabel(f"Click rate: {click_rate:.2f}/cps")
        big_font = self.label.font()
        big_font.setPointSize(14)
        self.label.setFont(big_font)
        self.label.setAlignment(Qt.AlignCenter)
        
        # print value of slider
        self.slider.valueChanged.connect(self.update_label)  

        # defaults to right Alt because it's the most cross-platform 
        self.toggle_key = Key.alt_r 

        layout = QVBoxLayout()

        self.setLayout(layout)

        layout.addWidget(self.slider)
        layout.addWidget(self.label)
        

    def update_label(self, click_rate):
        # set label text to clicks_per_second in slider
        self.label.setText(f"Click rate: {click_rate:.2f}/cps")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
