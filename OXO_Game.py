# main ui class
# Will Madikizela

import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class OxoGame(QWidget):
    def __init__ (self, parent = None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("O X O GAME")
        # backgroung color
        self.setPalette(QPalette(QColor("white")))
        # x, y, widgth and height
        self.setGeometry(550, 117, 500, 420)

        #Prepare to ddie
        # self.heading.setFont(QFont("impact", 12))


        # Declare
        self.heading  = QLabel("TenElevenGames OXO")
        self.server_input_label = QLabel("Server: ")
        self.server_url_input = QLineEdit()
        self.connect_button = QPushButton("Connect")


        self.messages_from_server_label = QLabel("---Messages from server---")
        self.messages_from_server = QTextEdit()

        self.player1_score_label = QLabel("Player 1:")
        self.player1_score_label.setStyleSheet("""
            border: 2px solid red;
            width: 40px;
            height: 40px;
        """)
        self.player2_score_label = QLabel("Player 2:")
        self.player1_score = QLabel("1")
        self.player2_score = QLabel("2")


        self.character_label = QLabel("Your Character:")
        self.character = QLabel("X")


        self.exit_button = QPushButton("Exit")
        self.new_game_button = QPushButton("New Game")

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.server_input_label)
        self.h_box.addWidget(self.server_url_input)
        self.h_box.addWidget(self.connect_button)
        h_box_widget = QWidget()
        h_box_widget.setLayout(self.h_box)



        # self.exit_button.setStyleSheet("QPushButton {background-color: black; color: white;}")
        # # new game buttonn
        # self.new_game_button.setStyleSheet("QPushButton {background-color: black; color: white;}")

        # Place widgets

        self.detail_grid = QGridLayout()
        self.detail_grid.addWidget(self.heading, 0, 0)
        self.detail_grid.addWidget(h_box_widget, 1, 0)

        self.detail_grid.addWidget(self.messages_from_server_label, 2, 0)
        self.detail_grid.addWidget(self.player1_score_label, 2, 1)
        self.detail_grid.addWidget(self.player1_score, 2, 2)
        self.detail_grid.addWidget(self.messages_from_server, 3, 0)
        self.detail_grid.addWidget(self.player2_score_label, 3, 1)
        self.detail_grid.addWidget(self.player2_score, 3, 2)


        self.detail_grid.addWidget(self.character_label, 4, 0)
        self.detail_grid.addWidget(self.character, 4, 1)

        detail_grid_widget = QWidget()
        detail_grid_widget.setLayout(self.detail_grid)

        # board grid
        self.button_1 = QPushButton()
        self.button_2 = QPushButton()
        self.button_3 = QPushButton()
        self.button_4 = QPushButton()
        self.button_5 = QPushButton()
        self.button_6 = QPushButton()
        self.button_7 = QPushButton()
        self.button_8 = QPushButton()
        self.button_9 = QPushButton()

        self.button_board_grid = QGridLayout()
        self.button_board_grid.addWidget(self.button_1, 0, 0)
        self.button_board_grid.addWidget(self.button_2, 0, 1)
        self.button_board_grid.addWidget(self.button_3, 0, 2)
        self.button_board_grid.addWidget(self.button_4, 1, 0)
        self.button_board_grid.addWidget(self.button_5, 1, 1)
        self.button_board_grid.addWidget(self.button_6, 1, 2)
        self.button_board_grid.addWidget(self.button_7, 2, 0)
        self.button_board_grid.addWidget(self.button_8, 2, 1)
        self.button_board_grid.addWidget(self.button_9, 2, 2)
        button_board_grid_widget = QWidget()
        button_board_grid_widget.setLayout(self.button_board_grid)

        # horintal box for exit and new game buttons

        hbox = QHBoxLayout()
        hbox.addWidget(self.new_game_button)
        hbox.addWidget(self.exit_button)
        hbox_widget = QWidget()
        hbox_widget.setLayout(hbox)

        # main layout management

        vbox = QVBoxLayout()
        vbox.addWidget(detail_grid_widget)
        vbox.addWidget(hbox_widget)
        #vbox.addWidget(button_board_grid_widget)
        vbox_widget  = QWidget()
        self.setLayout(vbox)

# Global styles
stylesheet = """
QLabel {
    /*  font-family: Roboto; */
    font-size: 12px;
}
QPushButton {
    background: #000;
    padding: 16px;
    color: #fff;
    /* font-family: Roboto; */
    font-size: 12px;
}
QTextEdit {
    height: 32px;
    background: #ECECEC;
    height: 32px !important;
}
QLineEdit {
    background: #ECECEC;
    padding: 16px;
}
"""


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    OXO = OxoGame()
    OXO.show()
    sys.exit(app.exec_())
main()
