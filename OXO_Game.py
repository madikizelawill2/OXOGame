# main ui class
# Will Madikizela

import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from random import*
from stylesheet import css


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
        self.heading.setFont(QFont("Simplifica", 20, 10))
        self.heading.setStyleSheet("color: #4A586E ")
        # set the heading label to center
        self.heading.setAlignment(Qt.AlignCenter)
        
        # server label 
        self.server_input_label = QLabel("Server:") 
        # server input 
        self.server_url_input = QLineEdit()
        self.server_url_input.setClearButtonEnabled(True)
        self.server_url_input.setPlaceholderText("enter server name")
        # button to connect to server
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect)


        # labels indicating messages from server
        self.messages_from_server_label = QLabel("*** OXO GAME SERVER MESSAGES ***")
        self.messages_from_server_label.setAlignment(Qt.AlignCenter)
        # messages from the server 
        self.messages_from_server = QTextEdit("")
        self.messages_from_server.setReadOnly(True) # disable editing the textedit 





        # character of the player
        self.o = QIcon("nought.gif") # x character
        self.x = QIcon("cross.gif") # o character
        self.null = QIcon("blank.gif") # blank character
        self.lst = [self.x , self.o] # set alist of icons
        self.lst_choice = choice(self.lst) # randomize the icons that will dispaly

        # label indicating the players character
        self.character_label = QLabel("Your Shape:")
        self.character_label.setAlignment(Qt.AlignCenter)

        # the button to place the character
        self.character = QPushButton() 
        self.character.move(1, 80)
        self.character.setText("")
        self.character.setIconSize(QSize(45, 45))
        self.character.setFixedSize(45, 45)
        # temporal character
        self.character.setIcon(self.lst_choice)
        self.character.setStyleSheet("background-color: #ECECEC ")
        self.character.setEnabled(True)





        # button to exit the game 
        self.exit_button = QPushButton("Exit")




        # board buttons
        self.board = QGridLayout()
        #self.board.setSpacing(10)
        self.board.setHorizontalSpacing(7)
        self.board.setVerticalSpacing(7)
        self.counter = 0
        #self.board.setDefaultPositioning()
        for self.column in range(3):
            for self.row in range(3):
                self.board_play_button = QToolButton()
                self.board_play_button.setFixedSize(100, 100)
                self.board_play_button.setIconSize(QSize(150, 150))
                self.board_play_button.setIcon(self.lst_choice)
                self.board_play_button.setText("")
                self.board_play_button.setObjectName(str(self.counter))
                self.board.addWidget(self.board_play_button, self.column, self.row)
                self.counter += 1

        self.board_widget = QWidget()
        self.board_widget.setLayout(self.board)

        self.allButtons = self.board_widget.findChildren(QToolButton)

        for button in self.allButtons:
            button.clicked.connect(self.buttons)



        ########################## LAY OUT MANAGEMENT ##############################
        


        # server grid
        self.server_heading_grid = QGridLayout()
        self.server_heading_grid.addWidget(self.heading, 0, 1, 1, 1)
        self.server_heading_grid.addWidget(self.server_input_label, 1, 0)
        self.server_heading_grid.addWidget(self.server_url_input, 1, 1)
        self.server_heading_grid.addWidget(self.connect_button, 1, 2)
        self.server_heading_grid_widget = QWidget()
        self.server_heading_grid_widget.setLayout(self.server_heading_grid)




        # grid layout for player information
        self.detail_character_grid = QGridLayout()
        self.detail_character_grid.addWidget(self.messages_from_server_label, 2, 0)
        self.detail_character_grid.addWidget(self.messages_from_server, 3, 0)
        #self.detail_character_grid.addWidget(self.character_label, 4, 0)
        #self.detail_character_grid.addWidget(self.character, 4, 1)
        self.detail_character_grid_widget = QWidget()
        self.detail_character_grid_widget.setLayout(self.detail_character_grid)




        # character layout
        self.character_layout = QGridLayout()
        self.character_layout.addWidget(self.character_label, 0, 0)
        self.character_layout.addWidget(self.character, 1, 0)
        self.character_layout_widget  = QWidget()
        self.character_layout_widget.setLayout(self.character_layout)



        #hbox for detail and character
        self.detail = QHBoxLayout()
        self.detail.addWidget(self.detail_character_grid_widget)
        self.detail.addWidget(self.character_layout_widget)
        self.detail_widget = QWidget()
        self.detail_widget.setLayout(self.detail)

        # the exit and new game horizontal layout 
        self.button_horizontalBox = QHBoxLayout()
        self.button_horizontalBox.addWidget(self.exit_button)
        self.button_horizontalBox_widget = QWidget()
        self.button_horizontalBox_widget.setLayout(self.button_horizontalBox)

    

        # main layout

        vbox = QVBoxLayout()
        vbox.addWidget(self.server_heading_grid_widget)
        #vbox.addWidget(self.detail_character_grid_widget)
        vbox.addWidget(self.detail_widget)
        vbox.addWidget(self.button_horizontalBox_widget)
        vbox_widget  = QWidget()
        vbox_widget.setLayout(vbox)
        ########################################################################

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(vbox_widget)
        self.main_layout.addWidget(self.board_widget)
        self.main_layout_widget = QWidget()
        self.setLayout(self.main_layout)

    def buttons(self):
        self.button = self.sender()
        self.messages_from_server.append("button " + self.button.objectName() + " clicked")   

    def connect(self):
        self.messages_from_server.append("connect button clicked")     



def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(css())
    OXO = OxoGame()
    OXO.show()
    sys.exit(app.exec_())
main()
