# Allow access to command-line arguments
import sys
 

from PySide.QtCore import *
from PySide.QtGui import *

qt_app = QApplication(sys.argv)
 
class LayoutExample(QWidget):
    ''' An example of PySide/PyQt absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''
 
    def __init__(self):
        # Initialize the object as a QWidget and
        # set its title and minimum width
        QWidget.__init__(self)
        self.setWindowTitle('Show Image!')
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)

        self.image = QLabel()
        self.pixmap = QPixmap("planet.jpg")
        self.image.setPixmap(self.pixmap)

        # Create the QVBoxLayout that lays out the whole form
        self.layout = QVBoxLayout()

        self.image_layout = QHBoxLayout()
        self.image_layout.setAlignment(Qt.AlignCenter)
        self.image_layout.addWidget(self.image)

        self.layout.addLayout(self.image_layout)
 
        # Create a horizontal box layout to hold the button
        self.button_box = QHBoxLayout()
 
        # Create the build button with its caption
        self.build_button = QPushButton('Configurations', self)

        self.build_button.clicked.connect(lambda: self.qstack.setCurrentIndex(1)) 
 
        # Add it to the button box
        self.button_box.addWidget(self.build_button)
 
        # Add the button box to the bottom of the main VBox layout
        self.layout.addLayout(self.button_box)

        # Create widget for the first layout
        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.layout)


        ##### SECOND PAGE

        self.layout2 = QVBoxLayout()

        self.select_box = QFormLayout()

        self.select_label = QLabel('Select image:', self)

        self.current_dir = QDir.current()
        self.current_dir.setNameFilters(['*.jpg', '*.png'])

        self.image_options = QDir.entryList(self.current_dir)

        self.select_image = QComboBox()
        self.select_image.addItems(self.image_options)

        index = self.select_image.findText('planet.jpg', Qt.MatchFixedString)
        if index >= 0:
            self.select_image.setCurrentIndex(index)

        self.select_box.addRow(self.select_label, self.select_image)


        self.layout2.addLayout(self.select_box)

        self.select_box.setFormAlignment(Qt.AlignHCenter)

        self.save_box = QHBoxLayout()
 
        self.save_button = QPushButton('Save', self)

        self.save_button.clicked.connect(self.buttonClicked) 

        self.save_box.addWidget(self.save_button)

        self.layout2.addLayout(self.save_box)

        self.select_crop_widget2 = QWidget()
        self.select_crop_widget2.setLayout(self.layout2)

        #####
 
        self.qstack = QStackedLayout()
        self.qstack.addWidget(self.select_crop_widget)
        self.qstack.addWidget(self.select_crop_widget2)

        # Set the VBox layout as the window's main layout
        self.setLayout(self.qstack)

    def buttonClicked(self):
        self.qstack.setCurrentIndex(0)
        self.data = self.select_image.currentText()
        print self.data
        self.pixmap = QPixmap(self.data)
        self.image.setPixmap(self.pixmap)
 
    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()
 
# Create an instance of the application window and run it
app = LayoutExample()
app.run()