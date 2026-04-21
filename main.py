import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

def on_button_click():
    label.setText("You clicked the button!")

# 1. Create the application (Required for any PyQt app)
app = QApplication(sys.vars) if hasattr(sys, 'vars') else QApplication(sys.argv)

# 2. Create the main window
window = QWidget()
window.setWindowTitle("My Fast App")

# 3. Create widgets
label = QLabel("Hello, PyQt!")
button = QPushButton("Click Me")

# 4. Connect Signal to Slot
button.clicked.connect(on_button_click)

# 5. Set up the Layout
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

# 6. Show the window and run the app
window.show()
sys.exit(app.exec())