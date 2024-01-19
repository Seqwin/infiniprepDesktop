from PyQt5.QtWidgets import QApplication, QSplashScreen, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import sys

class MainWindowWithSplash(QWidget):
    def __init__(self):
        super().__init__()

        # Splash screen setup
        splash_pixmap = QPixmap('Resources/testSplash.png')  # Replace with the actual path
        splash = QSplashScreen(splash_pixmap, Qt.WindowStaysOnTopHint)
        splash.show()

        # Main window setup
        self.setWindowTitle("Your Main Window")
        self.setGeometry(100, 100, 400, 300)

        # Create widgets
        label = QLabel("Hello, PyQt!")
        button = QPushButton("Click me!")

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        # Set the layout
        self.setLayout(layout)

        # Connect signals and slots
        button.clicked.connect(self.on_button_clicked)

        # Delay the splash screen for a few seconds (e.g., 3 seconds)
        QTimer.singleShot(3000, splash.close)

    def on_button_clicked(self):
        print("Button clicked!")

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindowWithSplash()
    main_window.show()
    sys.exit(app.exec_())