from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
    def setappear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
app = QApplication([])
main_win = QWidget()
main_win.show()
app.exec_()
