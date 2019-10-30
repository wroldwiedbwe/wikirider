import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QTextBrowser, QLabel
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import pyqtSlot, QRegExp

from src.wikirider import WikiRider
from src.view import RidePrinter

class App(QMainWindow):
    """User interface for WikiRider"""
    def __init__(self):
        super().__init__()
        self.title = "WikiRider GUI"
        self.left = 50
        self.top = 50
        self.width = 800
        self.height = 650
        self.initUI()
    
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Logo
        self.logo = QLabel(self)
        logo_text = r"""
                     (_\
                    / \
           `== / /\=,_
    _-_-  ;--==\\  \\o
_-_-__   /____//__/__\
      _-_-  `(0)       (0)
   
             WikiRider
        """
        self.logo.setText(logo_text)
        self.logo.move(600, 10)
        self.logo.resize(120, 120)
        
        # Wiki page input textbox
        wiki_regex = QRegExp("[a-z]{4,5}\:\/\/[a-z]+\.[a-z]+\.[a-z]+\/wiki\/.[^:#]{3,}$")
        self.url_input = QLineEdit(self,
            placeholderText="Starting wikipedia URL goes here...")
        wiki_validator = QRegExpValidator(wiki_regex, self.url_input)
        self.url_input.setValidator(wiki_validator)
        self.url_input.move(20, 20)
        self.url_input.resize(320,20)
        
        # Integer input textbox
        int_regex = QRegExp("[+0-9]+")
        self.int_input = QLineEdit(self,
                                   placeholderText="# pages to ride")
        int_validator = QRegExpValidator(int_regex, self.int_input)
        self.int_input.setValidator(int_validator)
        self.int_input.move(20, 60)
        self.int_input.resize(100, 20)
        
        # Go button
        self.button = QPushButton("Ride", self)
        self.button.move(20,100)
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        
        # Output window (read-only, with hyperlinks)
        self.text_output = OutputTextbox(self)
        self.text_output.move(20, 150)
        self.text_output.resize(760,480)
        self.text_output.setAcceptRichText(True)
        self.text_output.setOpenExternalLinks(True)

        self.show()
        

    @pyqtSlot()
    def on_click(self):
        """Action to complete on click"""
        self.text_output.setText("")
        url_to_ride = self.url_input.text()
        number_of_pages = self.int_input.text()
        if url_to_ride and number_of_pages:
            self.start(url_to_ride, number_of_pages)
        else:
            self.text_output.setText("Please specify a valid wiki url and integer")
        self.url_input.setText("")
        self.int_input.setText("")

    def start(self, url=None, depth=None):
        """Runs the wikiride using the user-specified url and depth"""
        sys.stdout = self.text_output # Direct output to textbox
        self.printer = RidePrinter()
        depth = int(depth)
        rider = WikiRider(url, depth)
        self.printer.print_start()
        for rider_state in rider.run():
            self.printer.print_rider_location(rider_state)
        self.printer.print_end()


class OutputTextbox(QTextBrowser):
    def write(self, text):
        """Function used by stdout"""
        self.insertPlainText(text)
        
    def flush(self):
        """Passing this skips the terminal-based colouring"""
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())