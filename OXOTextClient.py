#WILL 
#OXO GameTextClient

from GameClient import *
from time import *

class OXOTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE
        
    def input_server(self):
        return input('enter server:')
     
    def input_move(self):
        return input('enter move(0-8):')
     
    def input_play_again(self):
        return input('play again(y/n):')
    
    
    def display_board(self):
        # display the board to the screen
        print('\n')
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2] + "     0 | 1 | 2")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5] + "     3 | 4 | 5")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8] + "     6 | 7 | 8")       
        print('\n')
    
    
    def handle_message(self,msg):
        
        # indicates the new game is about to start
        if msg[:msg.find(",")] == "new game":

            # gets the shape from the message
            self.shape = msg[-1]

            # a statement indicating the player's character
            print("The game is about to begin your character is " + self.shape)

            # display initial board
            self.display_board()
        
        # indicates its the clients move
        elif msg == "your move":

            # let the player know its their time to move
            print("It's your turn to move")
            
            # get the input from the player and send it to server
            self.send_message(self.input_move())
            
        # indicates its the opponents move
        elif msg == "opponents move":

            # let the player know, the opponent player is about to move
            print("Waiting for the opponent to move...")
            
        # possition choosen is valid 
        elif msg[:msg.find(",")] == "valid move":
            
            # get position from player
            self.position = int(msg[-1])

            # get the character of the player
            self.shape = msg[-3]

            # Put the game piece on the board
            self.board[self.position] = self.shape

            # Show the game board
            self.display_board()
            
        # position choosen is invalid
        elif msg == "invalid move":

            # position unavailable on the board
            print("You can't go there. Try again.")
            
        # indicates that the game is over
        elif msg[:msg.find(",")] == "game over":

            # get results for the winner
            self.winner = msg[-1]

            # check if the winner is X or O
            if self.winner == "O" or self.winner == "X":

                # return the winner
                print("Game Over!\nThank you for playing, the winner is " + self.winner)

            # if there is no winner - it's a Tie
            else: print("Game Over!\nThank you for playing, it's a Tie :)")
            
            
        # see if the player wants to play again
        elif msg == "play again":

            # get feedback, if the player still wants rematch
            self.feedback = self.input_play_again()

            # send feedback to the server
            self.send_message(self.feedback)

            # checks feedback
            if self.feedback.lower() == "y":
                
                # clear board for new game
                self.clear_board()
        
        # terminate the game
        elif msg == "exit game":

            # message displayed if the other player exit game or is taking too long to play
            print("One of the players does not wish to continue")

            # passage time
            sleep(5)
    
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.handle_message(msg)
            else: break
            
def main():
    otc = OXOTextClient()
    while True:
        try:
            otc.connect_to_server(otc.input_server())
            break
        except:
            print('Error connecting to server!')
    otc.play_loop()
    input('Press click to exit.')
        
main()
 