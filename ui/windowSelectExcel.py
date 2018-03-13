from PyQt5.QtWidgets import QPushButton, QInputDialog, QLineEdit, QFileDialog, QLabel, QHBoxLayout, QGridLayout

class windowSelectExcel():
    def  __init__(self, window):
        self.window = window
        self.layout = QGridLayout(window)
        self.label = ''
        self.buttonInitFileDialog()

    def buttonInitFileDialog(self):
        button = QPushButton('Вибрати')
        button.setToolTip('Виберіть EXCEL файл')
        button.move(50,50)
        button.clicked.connect(lambda: self.openFileDialog())
        self.layout.addWidget(button, 0, 0)

    def labelFileName(self): 
        if self.label:
            print(self.label)
            label = QLabel('Вибрано файл: ' + self.label)
            button = QPushButton('Зберегти до бази')
            self.layout.addWidget(label, 1, 0)
            self.layout.addWidget(button,1,1)

    def openFileDialog(self):    
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self.window,"QFileDialog.getOpenFileName()", "","EXCEL Files (*.xls);;All Files (*)", options=options)
            if fileName:
                self.label = fileName
                self.labelFileName()