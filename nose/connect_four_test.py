from nose import with_setup
from pdb import set_trace
from nose.plugins.attrib import attr
from connectFour import ConnectFour

def setup_func():
    global newGame
    newGame = ConnectFour()

@with_setup(setup_func)
def print_board_test():
    newGame.board.printBoard()

@with_setup(setup_func)
@attr("test")
def move_player_test():
    newGame.playerMove()
