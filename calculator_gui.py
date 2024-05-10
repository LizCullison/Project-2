from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from formulas import Formulas

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(300, 400)
        
        self.expression = ''
        
        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        # Buttons
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]
        
        grid_layout = QGridLayout()
        
        for row, row_buttons in enumerate(buttons):
            for col, button_text in enumerate(row_buttons):
                button = QPushButton(button_text)
                button.setFixedSize(50, 50)
                grid_layout.addWidget(button, row, col)
                button.clicked.connect(self.handle_button_click)
        
        # Mode Button
        self.mode_button = QPushButton('Mode')
        self.mode_button.clicked.connect(self.toggle_mode)
        grid_layout.addWidget(self.mode_button, 4, 0, 1, 2)
        
        # Clear and Delete Buttons
        clear_button = QPushButton('C')
        delete_button = QPushButton('DEL')
        clear_button.clicked.connect(self.clear)
        delete_button.clicked.connect(self.delete)
        
        grid_layout.addWidget(clear_button, 4, 2)
        grid_layout.addWidget(delete_button, 4, 3)
        
        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid_layout)
        
        # Shape inputs
        self.shape_label = QLabel('Shape:')
        self.shape_combo = QComboBox()
        self.shape_combo.addItems(['Rectangle', 'Triangle', 'Circle'])
        self.shape_combo.currentIndexChanged.connect(self.update_shape_inputs)
        
        self.base_label = QLabel('Base:')
        self.base_input = QLineEdit()
        self.base_submit = QPushButton('Submit')
        self.base_submit.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.base_submit.clicked.connect(self.calculate_area)
        
        self.height_label = QLabel('Height:')
        self.height_input = QLineEdit()
        self.height_submit = QPushButton('Submit')
        self.height_submit.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.height_submit.clicked.connect(self.calculate_area)
        
        self.radius_label = QLabel('Radius:')
        self.radius_input = QLineEdit()
        self.radius_submit = QPushButton('Submit')
        self.radius_submit.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.radius_submit.clicked.connect(self.calculate_area)
        
        self.update_shape_inputs()
        
        shape_layout = QFormLayout()
        shape_layout.addRow(self.shape_label, self.shape_combo)
        shape_layout.addRow(self.base_label, self.base_input)
        shape_layout.addRow(self.base_submit)
        shape_layout.addRow(self.height_label, self.height_input)
        shape_layout.addRow(self.height_submit)
        shape_layout.addRow(self.radius_label, self.radius_input)
        shape_layout.addRow(self.radius_submit)
        
        layout.addLayout(shape_layout)
        
        self.setLayout(layout)
        
        # Initially hide shape inputs
        self.hide_shape_inputs()
        
    def handle_button_click(self):
        button = self.sender()
        if button:
            text = button.text()
            if text == '=':
                self.calculate()
            else:
                self.expression += text
                self.display.setText(self.expression)
        
    def calculate(self):
        try:
            if self.mode_button.text() == 'Shape':
                area = self.calculate_area()
                self.display.setText(str(area))
            else:
                result = eval(self.expression)
                self.display.setText(str(result))
        except Exception as e:
            self.display.setText('Error')
            print(e)
        self.expression = ''
        
    def clear(self):
        self.expression = ''
        self.display.clear()
        
    def delete(self):
        self.expression = self.expression[:-1]
        self.display.setText(self.expression)
        
    def toggle_mode(self):
        if self.mode_button.text() == 'Mode':
            self.mode_button.setText('Shape')
            self.show_shape_inputs()
        else:
            self.mode_button.setText('Mode')
            self.hide_shape_inputs()
            
    def show_shape_inputs(self):
        self.shape_label.show()
        self.shape_combo.show()
        self.update_shape_inputs()
        
    def hide_shape_inputs(self):
        self.shape_label.hide()
        self.shape_combo.hide()
        self.base_label.hide()
        self.base_input.hide()
        self.base_submit.hide()
        self.height_label.hide()
        self.height_input.hide()
        self.height_submit.hide()
        self.radius_label.hide()
        self.radius_input.hide()
        self.radius_submit.hide()
        
    def update_shape_inputs(self):
        shape = self.shape_combo.currentText()
        if shape == 'Rectangle':
            self.base_label.show()
            self.base_input.show()
            self.base_submit.show()
            self.height_label.show()
            self.height_input.show()
            self.height_submit.show()
            self.radius_label.hide()
            self.radius_input.hide()
            self.radius_submit.hide()
        elif shape == 'Triangle':
            self.base_label.show()
            self.base_input.show()
            self.base_submit.show()
            self.height_label.show()
            self.height_input.show()
            self.height_submit.show()
            self.radius_label.hide()
            self.radius_input.hide()
            self.radius_submit.hide()
        elif shape == 'Circle':
            self.base_label.hide()
            self.base_input.hide()
            self.base_submit.hide()
            self.height_label.hide()
            self.height_input.hide()
            self.height_submit.hide()
            self.radius_label.show()
            self.radius_input.show()
            self.radius_submit.show()
            
    def calculate_area(self):
        shape = self.shape_combo.currentText()
        try:
            if shape == 'Rectangle':
                base = float(self.base_input.text())
                height = float(self.height_input.text())
                area = Formulas.rectangle_area(base, height)
            elif shape == 'Triangle':
                base = float(self.base_input.text())
                height = float(self.height_input.text())
                area = Formulas.triangle_area(base, height)
            elif shape == 'Circle':
                radius = float(self.radius_input.text())
                area = Formulas.circle_area(radius)
            self.display.setText(str(area))
        except ValueError:
            self.display.setText('Error: Invalid input')
