from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel) 

from PyQt5 import QtGui
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import pywinstyles


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

window.setStyleSheet("color:black;")
window.setWindowTitle("Манипулятор изображений")

window.setWindowIcon(QtGui.QIcon('fake.png'))
pywinstyles.apply_style(window, 'dark')

label_image_input = QLabel("Введите название изображения")
label_image_input.setStyleSheet("color:gray;font-size:14px;font-weight:600;")
layout.addWidget(label_image_input)

input_image = QLineEdit()
input_image.setPlaceholderText("изображение")
input_image.setStyleSheet("color:gray;border:3px solid gray;padding: 6px;")
layout.addWidget(input_image)



window.setLayout(layout)
window.show()
app.exec_()
