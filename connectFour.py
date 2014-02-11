"""
Connect 4 UI
Ensure 2 players

"""

from board import Board, Point
import sys

class ConnectFour:
    def __init__(self):
        self.board = Board()
        self.player1 = "X"
        self.player2 = "O"
        self.currentPlayer = "X"
        self.board.printBoard()
        self.playerMove()

    def switchPlayer(self):
        self.currentPlayer = self.player1 if self.currentPlayer != self.player1 else self.player2
        if self.board.complete != True:
            self.playerMove()

    def playerMove(self):
        print "Player " + self.currentPlayer + " please place a move.  Just enter the x-axis value"
        curr_move = int(raw_input())
        self.board.placeMove(curr_move, self.currentPlayer)
        self.switchPlayer()


newGame = ConnectFour()
