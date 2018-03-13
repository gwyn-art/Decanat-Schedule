import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui.windowSelectExcel import windowSelectExcel

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Розклад APP'
        self.left = 10
        self.top = 40
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        windowSelectExcel(self)
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())