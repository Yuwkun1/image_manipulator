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
from mannnna import *


styles_for_btn = """
    QPushButton {
        color: black;
        border: 1px solid black;
        font-weight: 600;
    }
    QPushButton:hover {
        color: grey;
        border: 1px solid; 
        font-weight: 700;
    }
    QPushButton::focus {
        color: grey;
        border-color: black;
        font-size: 10px;
    }
    """
# QPushButton {} внутри описываем стили в обычном состоянии
# QPushButton:hover в момент наведения курсором 

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
input_image.setPlaceholderText("Изображение")
input_image.setStyleSheet("color:gray;border:3px solid gray;padding: 6px;")
layout.addWidget(input_image)

layout_v = QVBoxLayout()
layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()

layout_v.addLayout(layout_h1)
layout_v.addLayout(layout_h2)
layout.addLayout(layout_v)

btn_info = QPushButton("Информация \n о изображении")
btn_info.setStyleSheet(styles_for_btn)
layout_h1.addWidget(btn_info)

btn_MBW = QPushButton("сделать \n черно-белый")
btn_MBW.setStyleSheet(styles_for_btn)
btn_MBW.clicked.connect(
    lambda: emboss(input_image)
)
layout_h1.addWidget(btn_MBW)

btn_emboss = QPushButton("Сделать \n тиснение")
btn_emboss.setStyleSheet(styles_for_btn)
btn_emboss.clicked.connect(
    lambda: emboss(input_image)
)
layout_h2.addWidget(btn_emboss)

btn_pencil = QPushButton("Сделать \n карандашом")
btn_pencil.setStyleSheet(styles_for_btn)
btn_pencil.clicked.connect(
    lambda: contour(input_image)
)
layout_h1.addWidget(btn_pencil)

btn_flip = QPushButton("Сделать \n отзеркаливание")
btn_flip.setStyleSheet(styles_for_btn)
btn_flip.clicked.connect(
    lambda: emboss(input_image)
)
layout_h2.addWidget(btn_flip)

btn_rotate = QPushButton("Сделать \n разворот")
btn_rotate.setStyleSheet(styles_for_btn)
layout_h2.addWidget(btn_rotate)

window.setLayout(layout)
window.resize(350, 0)
window.show()
app.exec_()
