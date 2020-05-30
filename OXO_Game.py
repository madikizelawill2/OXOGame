# main gui class
# Will Madikizela

import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from random import*


class OxoGame(QWidget): # inherits from QWidgets
    # parent difines parent widget
    def __init__ (self, parent = None):
        # super class constructor
        QWidget.__init__(self, parent)
        # window name
        self.setWindowTitle("TenElevenGames")
        # backgroung color of the window 
        self.setPalette(QPalette(QColor("white")))
        # x, y, widgth and height
        self.setGeometry(550, 117, 500, 350)
        # game icon
        self.setWindowIcon(QIcon("gameIcon.png"))
        # Disable maximizing window
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint)
    
        # Declare variables 
        # heading label
        self.heading  = QLabel("OXO Game")
        # set font of the heading label
        self.heading.setFont(QFont("Simplifica", 20, 10))
        # set color of the heading label to greyish blue 
        self.heading.setStyleSheet("color: #4A586E ")
        # set the heading label to center
        self.heading.setAlignment(Qt.AlignCenter)
        
        # server label 
        self.server_input_label = QLabel("Server:") 
        # server input 
        self.server_url_input = QLineEdit()
        # allow a button to clear all the text at once
        self.server_url_input.setClearButtonEnabled(True)
        # place holder in the input for server for more intructions
        self.server_url_input.setPlaceholderText("enter server name")
        # button to connect to server
        self.connect_button = QPushButton("Connect")
        # connect the button to report action when pressed
        self.connect_button.clicked.connect(self.connect)


        # labels indicating messages from server
        self.messages_from_server_label = QLabel("*** OXO GAME SERVER MESSAGES ***")
        # align the message label to centre
        self.messages_from_server_label.setAlignment(Qt.AlignCenter)
        # messages from the server 
        self.messages_from_server = QTextEdit("")
        # disable editing the textedit 
        self.messages_from_server.setReadOnly(True)

        # label indicating the players character
        self.character_label = QLabel("Your Shape:")
        # align the label to centre
        self.character_label.setAlignment(Qt.AlignCenter)

        # character of the player
        # x character
        self.o = QIcon("nought.gif")
        # o character
        self.x = QIcon("cross.gif")
        # blank character
        self.null = QIcon("blank.gif")
        # set alist of icons 
        self.lst = [self.x , self.o] 
        # randomize the icons that will dispaly
        self.lst_choice = choice(self.lst) 

        # the button to place the character
        self.character = QPushButton() 
        # set text to Fasle to allow icon to be inserted to the button
        self.character.setText("")
        # set the size of the icon to 45 heigth and 45 widgth
        self.character.setIconSize(QSize(45, 45))
        # set the size of the button to 45 height and 45 widgth
        self.character.setFixedSize(45, 45)
        # temporal character
        self.character.setIcon(self.lst_choice)
        self.character.setStyleSheet("background-color: #ECECEC ")
        self.character.setEnabled(True)

        # button to exit the game 
        self.exit_button = QPushButton("Exit")
        # connect the button to report action when pressed
        self.exit_button.clicked.connect(self.exit)

        # board buttons
        self.board = QGridLayout()
        # customize horizontal spacing between buttons to 7px
        self.board.setHorizontalSpacing(7)
        # customize vertical spacing between buttons to 7px
        self.board.setVerticalSpacing(7)
        self.counter = 0
        # iterate at a range of 3 to allow 3 columns
        for self.column in range(3):
            # iterate at a range of 3 to allow 3 rows
            for self.row in range(3):
                # set board button
                self.board_play_button = QToolButton()
                # Fixed size of the button to 100 height and 100 widgth
                self.board_play_button.setFixedSize(100, 100)
                # Fixed size of the icon in the button to 150 height and 150 widgth
                self.board_play_button.setIconSize(QSize(150, 150))
                # put icon to the button
                self.board_play_button.setIcon(self.lst_choice)
                # set text to Fasle to allow icon to be inserted to the button 
                self.board_play_button.setText("")
                # track each button by giving it, its object name 
                self.board_play_button.setObjectName(str(self.counter))
                self.board.addWidget(self.board_play_button, self.column, self.row)
                # increment counter
                self.counter += 1
        # create widget for the board game
        self.board_widget = QWidget()
        self.board_widget.setLayout(self.board)
        # get all the buttons in the board widget
        self.allButtons = self.board_widget.findChildren(QToolButton)
        # iterate each button
        for button in self.allButtons:
            # connect each button to report feedback when pressed
            button.clicked.connect(self.buttons)

        ########################## LAY OUT MANAGEMENT ##############################

        # input info grid
        self.server_heading_grid = QGridLayout()
        # heading
        self.server_heading_grid.addWidget(self.heading, 0, 1, 1, 1)
        # server input label
        self.server_heading_grid.addWidget(self.server_input_label, 1, 0)
        # server input
        self.server_heading_grid.addWidget(self.server_url_input, 1, 1)
        # connect button
        self.server_heading_grid.addWidget(self.connect_button, 1, 2)
        self.server_heading_grid_widget = QWidget()
        self.server_heading_grid_widget.setLayout(self.server_heading_grid)

        # grid layout for player information 
        self.detail_character_grid = QGridLayout()
        # label for messages from server
        self.detail_character_grid.addWidget(self.messages_from_server_label, 2, 0)
        # messages from server
        self.detail_character_grid.addWidget(self.messages_from_server, 3, 0)
        self.detail_character_grid_widget = QWidget()
        self.detail_character_grid_widget.setLayout(self.detail_character_grid)

        # character layout information
        self.character_layout = QGridLayout()
        # character display label
        self.character_layout.addWidget(self.character_label, 0, 0)
        # character of the player or user
        self.character_layout.addWidget(self.character, 1, 0)
        self.character_layout_widget  = QWidget()
        self.character_layout_widget.setLayout(self.character_layout)

        # layout for all the details of the user or player
        self.detail = QHBoxLayout()
        # layout for player information
        self.detail.addWidget(self.detail_character_grid_widget)
        # character layout information
        self.detail.addWidget(self.character_layout_widget)
        self.detail_widget = QWidget()
        self.detail_widget.setLayout(self.detail)

        # the exit layout 
        self.button_horizontalBox = QHBoxLayout()
        # exit button
        self.button_horizontalBox.addWidget(self.exit_button)
        self.button_horizontalBox_widget = QWidget()
        self.button_horizontalBox_widget.setLayout(self.button_horizontalBox)


        vbox = QVBoxLayout()
        vbox.addWidget(self.server_heading_grid_widget)
        vbox.addWidget(self.detail_widget)
        vbox.addWidget(self.button_horizontalBox_widget)
        vbox_widget  = QWidget()
        vbox_widget.setLayout(vbox)

        ##############################  MAIN LAYOUT  #################################

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(vbox_widget)
        self.main_layout.addWidget(self.board_widget)
        self.main_layout_widget = QWidget()
        self.setLayout(self.main_layout)

    # fuction for game board buttons        
    def buttons(self):
        self.button = self.sender()
        self.messages_from_server.append("button " + self.button.objectName() + " clicked") 

    # fuction for connect button
    def connect(self):
        self.messages_from_server.append("connect button clicked")
          
    # fuction for exit button
    def exit(self):
        self.messages_from_server.append("Exit button clicked")

# Global styles
stylesheet = """
QLabel {
    font-size: 12px;
}
QPushButton {
    background: #000;
    border: none;
    padding: 16px;
    color: #fff;
    font-size: 12px;
}
QPushButton:pressed {
    background: #ECECEC;
    padding: 16px;
    color: #000;
    font-size: 12px;
}
QToolButton {
    background: #ECECEC;
    padding: 16px;
    outline: none;
    border: none;

}
QToolButton:pressed {
    background: #D5D5D5;
    padding: 16px;
    outline: none;
}
QToolBuuton:checked {
    background: #ECECEC;
    padding: 16px;
    outline: none;

}
QTextEdit {
    height: 32px;
    background: #ECECEC; 
    height: 32px ;
    outline: none;
    border: none;
}
QLineEdit {
    background: #ECECEC;
    padding: 16px;
    outline: none;
    border: none;
}
"""

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    OXO = OxoGame()
    OXO.show()
    sys.exit(app.exec_())
main()
